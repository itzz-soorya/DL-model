"""
RNN Model - Confusion Matrix and Heatmap Visualizations
Generates confusion matrices and performance heatmaps for the trained RNN model
"""
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from tensorflow import keras
from sklearn.metrics import confusion_matrix, classification_report, accuracy_score
from sklearn.metrics import precision_score, recall_score, f1_score
from sklearn.model_selection import train_test_split
import json

print("="*80)
print("RNN MODEL - CONFUSION MATRIX & HEATMAP GENERATION")
print("="*80)

# ============================================================================
# LOAD MODEL AND GENERATE TEST DATA
# ============================================================================
print("\n[1/5] Loading RNN model...")
rnn_model = keras.models.load_model('fitness_rnn_model.h5')
print("✓ RNN model loaded successfully")

print("\n[2/5] Generating test data...")

# Workout types
workout_types = {
    'Rest': 0,
    'Cardio': 1,
    'Strength': 2,
    'HIIT': 3,
    'Yoga': 4,
    'Swimming': 5,
    'Cycling': 6
}

workout_names = ['Rest', 'Cardio', 'Strength', 'HIIT', 'Yoga', 'Swimming', 'Cycling']

# Generate workout sequence based on level and goal
def generate_workout_sequence(level, goal):
    sequence = []
    
    if level == 0:  # Beginner
        if goal == 0:  # Weight loss
            sequence = [1, 0, 2, 0, 1, 0, 4]
        elif goal == 1:  # Muscle gain
            sequence = [2, 0, 2, 0, 2, 2, 0]
        else:  # Fitness
            sequence = [1, 2, 0, 3, 0, 1, 4]
    elif level == 1:  # Intermediate
        if goal == 0:
            sequence = [3, 1, 2, 1, 3, 6, 0]
        elif goal == 1:
            sequence = [2, 2, 0, 2, 2, 2, 0]
        else:
            sequence = [2, 3, 1, 2, 3, 5, 4]
    else:  # Advanced
        if goal == 0:
            sequence = [3, 3, 2, 3, 3, 6, 1]
        elif goal == 1:
            sequence = [2, 2, 2, 2, 2, 2, 0]
        else:
            sequence = [3, 2, 3, 2, 3, 5, 2]
    
    return sequence

# Create test data (larger dataset for better statistics)
np.random.seed(42)
test_sequences = []
test_labels = []
test_features = []

for _ in range(1000):  # Generate 1000 test samples
    level = np.random.randint(0, 3)
    goal = np.random.randint(0, 3)
    age = np.random.randint(18, 65)
    
    sequence = generate_workout_sequence(level, goal)
    
    # Add some randomness
    for i in range(len(sequence)):
        if np.random.random() < 0.15:  # 15% chance to modify
            sequence[i] = np.random.randint(0, 7)
    
    test_sequences.append(sequence[:6])
    test_labels.append(sequence[6])
    test_features.append([age / 100.0, level / 2.0, goal / 2.0])

X_seq_test = np.array(test_sequences)
X_feat_test = np.array(test_features)
y_test = np.array(test_labels)

print(f"✓ Generated {len(y_test)} test samples")

# ============================================================================
# MAKE PREDICTIONS
# ============================================================================
print("\n[3/5] Making predictions on test data...")
predictions = rnn_model.predict([X_seq_test, X_feat_test], verbose=0)
y_pred = np.argmax(predictions, axis=1)

# Calculate metrics
accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred, average='weighted', zero_division=0)
recall = recall_score(y_test, y_pred, average='weighted', zero_division=0)
f1 = f1_score(y_test, y_pred, average='weighted', zero_division=0)

print(f"✓ Predictions complete")
print(f"  • Accuracy: {accuracy*100:.2f}%")
print(f"  • Precision: {precision*100:.2f}%")
print(f"  • Recall: {recall*100:.2f}%")
print(f"  • F1-Score: {f1*100:.2f}%")

# ============================================================================
# GENERATE CONFUSION MATRIX
# ============================================================================
print("\n[4/5] Generating confusion matrix...")
cm = confusion_matrix(y_test, y_pred)

# ============================================================================
# DIAGRAM 1: Confusion Matrix with Counts
# ============================================================================
print("\n  [1/6] Creating confusion matrix with counts...")

fig, ax = plt.subplots(figsize=(12, 10))

sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', 
            xticklabels=workout_names, yticklabels=workout_names,
            cbar_kws={'label': 'Number of Samples'},
            linewidths=1, linecolor='black',
            annot_kws={'size': 12, 'weight': 'bold'})

plt.title('RNN Model - Confusion Matrix (Sample Counts)', 
          fontsize=16, fontweight='bold', pad=20)
plt.xlabel('Predicted Workout Type', fontsize=14, fontweight='bold')
plt.ylabel('Actual Workout Type', fontsize=14, fontweight='bold')
plt.xticks(rotation=45, ha='right')
plt.yticks(rotation=0)

# Add accuracy text
textstr = f'Accuracy: {accuracy*100:.2f}%\nSamples: {len(y_test)}'
props = dict(boxstyle='round', facecolor='wheat', alpha=0.8)
ax.text(0.02, 0.98, textstr, transform=ax.transAxes, fontsize=12,
        verticalalignment='top', bbox=props)

plt.tight_layout()
plt.savefig('rnn_confusion_matrix_counts.png', dpi=300, bbox_inches='tight')
print("    ✓ Saved: rnn_confusion_matrix_counts.png")
plt.close()

# ============================================================================
# DIAGRAM 2: Normalized Confusion Matrix (Percentages)
# ============================================================================
print("  [2/6] Creating normalized confusion matrix...")

# Normalize by row (actual class)
cm_normalized = cm.astype('float') / cm.sum(axis=1)[:, np.newaxis]
cm_normalized = np.nan_to_num(cm_normalized)  # Replace NaN with 0

fig, ax = plt.subplots(figsize=(12, 10))

sns.heatmap(cm_normalized, annot=True, fmt='.2%', cmap='RdYlGn',
            xticklabels=workout_names, yticklabels=workout_names,
            cbar_kws={'label': 'Percentage', 'format': '%.0f%%'},
            linewidths=1, linecolor='black',
            annot_kws={'size': 11, 'weight': 'bold'},
            vmin=0, vmax=1)

plt.title('RNN Model - Confusion Matrix (Normalized by True Label)', 
          fontsize=16, fontweight='bold', pad=20)
plt.xlabel('Predicted Workout Type', fontsize=14, fontweight='bold')
plt.ylabel('Actual Workout Type', fontsize=14, fontweight='bold')
plt.xticks(rotation=45, ha='right')
plt.yticks(rotation=0)

# Add metrics text
textstr = f'Overall Accuracy: {accuracy*100:.2f}%\nF1-Score: {f1*100:.2f}%'
props = dict(boxstyle='round', facecolor='lightblue', alpha=0.8)
ax.text(0.02, 0.98, textstr, transform=ax.transAxes, fontsize=12,
        verticalalignment='top', bbox=props)

plt.tight_layout()
plt.savefig('rnn_confusion_matrix_normalized.png', dpi=300, bbox_inches='tight')
print("    ✓ Saved: rnn_confusion_matrix_normalized.png")
plt.close()

# ============================================================================
# DIAGRAM 3: Per-Class Performance Heatmap
# ============================================================================
print("  [3/6] Creating per-class performance heatmap...")

# Calculate per-class metrics
class_metrics = []
for i in range(7):
    tp = cm[i, i]
    fp = cm[:, i].sum() - tp
    fn = cm[i, :].sum() - tp
    tn = cm.sum() - tp - fp - fn
    
    class_precision = tp / (tp + fp) if (tp + fp) > 0 else 0
    class_recall = tp / (tp + fn) if (tp + fn) > 0 else 0
    class_f1 = 2 * (class_precision * class_recall) / (class_precision + class_recall) if (class_precision + class_recall) > 0 else 0
    class_support = cm[i, :].sum()
    
    class_metrics.append([class_precision, class_recall, class_f1, class_support])

class_metrics = np.array(class_metrics)

fig, ax = plt.subplots(figsize=(10, 10))

# Create heatmap for precision, recall, f1
metrics_data = class_metrics[:, :3]
sns.heatmap(metrics_data.T, annot=True, fmt='.3f', cmap='YlOrRd',
            xticklabels=workout_names, 
            yticklabels=['Precision', 'Recall', 'F1-Score'],
            cbar_kws={'label': 'Score'},
            linewidths=2, linecolor='black',
            annot_kws={'size': 12, 'weight': 'bold'},
            vmin=0, vmax=1)

plt.title('RNN Model - Per-Class Performance Metrics', 
          fontsize=16, fontweight='bold', pad=20)
plt.xlabel('Workout Type', fontsize=14, fontweight='bold')
plt.ylabel('Metric', fontsize=14, fontweight='bold')
plt.xticks(rotation=45, ha='right')

plt.tight_layout()
plt.savefig('rnn_per_class_performance.png', dpi=300, bbox_inches='tight')
print("    ✓ Saved: rnn_per_class_performance.png")
plt.close()

# ============================================================================
# DIAGRAM 4: Prediction Confidence Heatmap
# ============================================================================
print("  [4/6] Creating prediction confidence heatmap...")

# Calculate average confidence for each true-pred pair
confidence_matrix = np.zeros((7, 7))
count_matrix = np.zeros((7, 7))

for i in range(len(y_test)):
    true_label = y_test[i]
    pred_label = y_pred[i]
    confidence = predictions[i][pred_label]
    
    confidence_matrix[true_label, pred_label] += confidence
    count_matrix[true_label, pred_label] += 1

# Average confidence
avg_confidence = np.divide(confidence_matrix, count_matrix, 
                          where=count_matrix!=0, 
                          out=np.zeros_like(confidence_matrix))

fig, ax = plt.subplots(figsize=(12, 10))

sns.heatmap(avg_confidence, annot=True, fmt='.3f', cmap='viridis',
            xticklabels=workout_names, yticklabels=workout_names,
            cbar_kws={'label': 'Average Confidence'},
            linewidths=1, linecolor='white',
            annot_kws={'size': 10, 'weight': 'bold'},
            vmin=0, vmax=1)

plt.title('RNN Model - Average Prediction Confidence', 
          fontsize=16, fontweight='bold', pad=20)
plt.xlabel('Predicted Workout Type', fontsize=14, fontweight='bold')
plt.ylabel('Actual Workout Type', fontsize=14, fontweight='bold')
plt.xticks(rotation=45, ha='right')
plt.yticks(rotation=0)

plt.tight_layout()
plt.savefig('rnn_prediction_confidence_heatmap.png', dpi=300, bbox_inches='tight')
print("    ✓ Saved: rnn_prediction_confidence_heatmap.png")
plt.close()

# ============================================================================
# DIAGRAM 5: Error Analysis Heatmap
# ============================================================================
print("  [5/6] Creating error analysis heatmap...")

# Calculate error rates (normalized by true class)
error_matrix = cm.copy().astype('float')
for i in range(7):
    row_sum = error_matrix[i, :].sum()
    if row_sum > 0:
        error_matrix[i, i] = 0  # Set diagonal to 0 (correct predictions)
        error_matrix[i, :] = error_matrix[i, :] / row_sum

fig, ax = plt.subplots(figsize=(12, 10))

sns.heatmap(error_matrix, annot=True, fmt='.2%', cmap='Reds',
            xticklabels=workout_names, yticklabels=workout_names,
            cbar_kws={'label': 'Error Rate'},
            linewidths=1, linecolor='black',
            annot_kws={'size': 10, 'weight': 'bold'},
            vmin=0, vmax=0.3)

plt.title('RNN Model - Misclassification Error Rates\n(Diagonal = 0 for Correct Predictions)', 
          fontsize=16, fontweight='bold', pad=20)
plt.xlabel('Predicted Workout Type', fontsize=14, fontweight='bold')
plt.ylabel('Actual Workout Type', fontsize=14, fontweight='bold')
plt.xticks(rotation=45, ha='right')
plt.yticks(rotation=0)

# Add note
note = "Higher values indicate more frequent misclassifications"
ax.text(0.5, -0.12, note, transform=ax.transAxes, fontsize=11,
        ha='center', style='italic', color='red')

plt.tight_layout()
plt.savefig('rnn_error_analysis_heatmap.png', dpi=300, bbox_inches='tight')
print("    ✓ Saved: rnn_error_analysis_heatmap.png")
plt.close()

# ============================================================================
# DIAGRAM 6: Comprehensive Metrics Dashboard
# ============================================================================
print("  [6/6] Creating comprehensive metrics dashboard...")

fig = plt.figure(figsize=(20, 12))
gs = fig.add_gridspec(3, 3, hspace=0.3, wspace=0.3)

# 1. Confusion Matrix (top-left, larger)
ax1 = fig.add_subplot(gs[0:2, 0:2])
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues',
            xticklabels=workout_names, yticklabels=workout_names,
            ax=ax1, cbar_kws={'label': 'Count'},
            linewidths=1, linecolor='black',
            annot_kws={'size': 11, 'weight': 'bold'})
ax1.set_title('Confusion Matrix', fontsize=14, fontweight='bold')
ax1.set_xlabel('Predicted', fontsize=12, fontweight='bold')
ax1.set_ylabel('Actual', fontsize=12, fontweight='bold')
ax1.tick_params(axis='x', rotation=45)

# 2. Per-Class Accuracy Bar Chart
ax2 = fig.add_subplot(gs[0, 2])
class_accuracies = np.diag(cm) / cm.sum(axis=1)
colors_bar = ['green' if acc > 0.8 else 'orange' if acc > 0.6 else 'red' for acc in class_accuracies]
bars = ax2.barh(workout_names, class_accuracies, color=colors_bar, edgecolor='black', linewidth=1.5)
ax2.set_xlabel('Accuracy', fontsize=11, fontweight='bold')
ax2.set_title('Per-Class Accuracy', fontsize=12, fontweight='bold')
ax2.set_xlim([0, 1])
ax2.grid(True, alpha=0.3, axis='x')
for i, (bar, acc) in enumerate(zip(bars, class_accuracies)):
    ax2.text(acc + 0.02, bar.get_y() + bar.get_height()/2, 
             f'{acc:.1%}', va='center', fontsize=10, fontweight='bold')

# 3. F1-Score per Class
ax3 = fig.add_subplot(gs[1, 2])
class_f1_scores = class_metrics[:, 2]
colors_f1 = ['green' if f1 > 0.8 else 'orange' if f1 > 0.6 else 'red' for f1 in class_f1_scores]
bars = ax3.barh(workout_names, class_f1_scores, color=colors_f1, edgecolor='black', linewidth=1.5)
ax3.set_xlabel('F1-Score', fontsize=11, fontweight='bold')
ax3.set_title('Per-Class F1-Score', fontsize=12, fontweight='bold')
ax3.set_xlim([0, 1])
ax3.grid(True, alpha=0.3, axis='x')
for i, (bar, f1_val) in enumerate(zip(bars, class_f1_scores)):
    ax3.text(f1_val + 0.02, bar.get_y() + bar.get_height()/2, 
             f'{f1_val:.1%}', va='center', fontsize=10, fontweight='bold')

# 4. Overall Metrics Text Box
ax4 = fig.add_subplot(gs[2, 0])
ax4.axis('off')
metrics_text = f"""
╔══════════════════════════════════════════╗
║       OVERALL MODEL PERFORMANCE          ║
╚══════════════════════════════════════════╝

Accuracy:           {accuracy*100:.2f}%
Precision (Weighted): {precision*100:.2f}%
Recall (Weighted):    {recall*100:.2f}%
F1-Score (Weighted):  {f1*100:.2f}%

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Test Samples:       {len(y_test):,}
Correct Predictions: {(y_test == y_pred).sum():,}
Wrong Predictions:   {(y_test != y_pred).sum():,}

Model: fitness_rnn_model.h5
Parameters: 41,975
Architecture: LSTM RNN
"""
ax4.text(0.5, 0.5, metrics_text, ha='center', va='center',
         fontsize=10, family='monospace',
         bbox=dict(boxstyle='round', facecolor='#E8F5E9', alpha=0.9, linewidth=2))

# 5. Classification Report Table
ax5 = fig.add_subplot(gs[2, 1:3])
ax5.axis('off')

report_data = []
report_data.append(['Class', 'Precision', 'Recall', 'F1-Score', 'Support'])
report_data.append(['━'*10, '━'*9, '━'*9, '━'*9, '━'*8])

for i, name in enumerate(workout_names):
    report_data.append([
        name,
        f'{class_metrics[i, 0]:.3f}',
        f'{class_metrics[i, 1]:.3f}',
        f'{class_metrics[i, 2]:.3f}',
        f'{int(class_metrics[i, 3])}'
    ])

report_data.append(['━'*10, '━'*9, '━'*9, '━'*9, '━'*8])
report_data.append([
    'Weighted Avg',
    f'{precision:.3f}',
    f'{recall:.3f}',
    f'{f1:.3f}',
    f'{len(y_test)}'
])

table = ax5.table(cellText=report_data, cellLoc='center', loc='center',
                  colWidths=[0.25, 0.18, 0.18, 0.18, 0.15])
table.auto_set_font_size(False)
table.set_fontsize(9)
table.scale(1, 2)

# Style header
for i in range(5):
    table[(0, i)].set_facecolor('#2c3e50')
    table[(0, i)].set_text_props(weight='bold', color='white')

# Style rows
for i in range(2, len(report_data)-2):
    for j in range(5):
        if i % 2 == 0:
            table[(i, j)].set_facecolor('#f8f9fa')

# Style totals row
for i in range(5):
    table[(len(report_data)-1, i)].set_facecolor('#ffffcc')
    table[(len(report_data)-1, i)].set_text_props(weight='bold')

plt.suptitle('RNN Model - Comprehensive Performance Dashboard', 
             fontsize=18, fontweight='bold', y=0.98)
plt.savefig('rnn_comprehensive_metrics_dashboard.png', dpi=300, bbox_inches='tight')
print("    ✓ Saved: rnn_comprehensive_metrics_dashboard.png")
plt.close()

# ============================================================================
# SAVE METRICS TO JSON
# ============================================================================
print("\n[5/5] Saving metrics to JSON...")

metrics_dict = {
    'overall_metrics': {
        'accuracy': float(accuracy),
        'precision': float(precision),
        'recall': float(recall),
        'f1_score': float(f1),
        'test_samples': int(len(y_test)),
        'correct_predictions': int((y_test == y_pred).sum()),
        'wrong_predictions': int((y_test != y_pred).sum())
    },
    'per_class_metrics': {}
}

for i, name in enumerate(workout_names):
    metrics_dict['per_class_metrics'][name] = {
        'precision': float(class_metrics[i, 0]),
        'recall': float(class_metrics[i, 1]),
        'f1_score': float(class_metrics[i, 2]),
        'support': int(class_metrics[i, 3]),
        'accuracy': float(class_accuracies[i])
    }

metrics_dict['confusion_matrix'] = cm.tolist()

with open('rnn_evaluation_metrics.json', 'w') as f:
    json.dump(metrics_dict, f, indent=2)

print("✓ Saved: rnn_evaluation_metrics.json")

# ============================================================================
# SUMMARY
# ============================================================================
print("\n" + "="*80)
print("RNN CONFUSION MATRIX & HEATMAP GENERATION COMPLETE!")
print("="*80)
print("\n📊 Generated Visualizations:")
print("   1. rnn_confusion_matrix_counts.png          - Sample counts")
print("   2. rnn_confusion_matrix_normalized.png      - Normalized percentages")
print("   3. rnn_per_class_performance.png            - Per-class metrics heatmap")
print("   4. rnn_prediction_confidence_heatmap.png    - Confidence scores")
print("   5. rnn_error_analysis_heatmap.png           - Misclassification rates")
print("   6. rnn_comprehensive_metrics_dashboard.png  - Complete dashboard")
print("\n📄 Data Files:")
print("   • rnn_evaluation_metrics.json               - All metrics in JSON")
print("\n📈 Overall Performance:")
print(f"   • Accuracy:  {accuracy*100:.2f}%")
print(f"   • Precision: {precision*100:.2f}%")
print(f"   • Recall:    {recall*100:.2f}%")
print(f"   • F1-Score:  {f1*100:.2f}%")
print(f"   • Test Samples: {len(y_test):,}")
print("="*80 + "\n")
