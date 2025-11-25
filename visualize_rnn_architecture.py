"""
RNN Model - Generate Actual Architecture Diagrams
Creates visual diagrams of the real trained model architecture
"""
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

import numpy as np
import matplotlib.pyplot as plt
from tensorflow import keras
from tensorflow.keras.utils import plot_model
import json

print("="*80)
print("GENERATING ACTUAL RNN MODEL ARCHITECTURE DIAGRAMS")
print("="*80)

print("\n[1/4] Loading RNN model...")
try:
    rnn_model = keras.models.load_model('fitness_rnn_model.h5')
    print("✓ RNN model loaded successfully")
except Exception as e:
    print(f"✗ Error loading model: {e}")
    exit(1)

# Load results
with open('real_model_results.json', 'r') as f:
    results = json.load(f)

print(f"\n[2/4] Model Information:")
print(f"  • Accuracy: {results['rnn_model']['real_accuracy']}%")
print(f"  • Parameters: {results['rnn_model']['parameters']:,}")
print(f"  • Architecture: {results['rnn_model']['architecture']}")

print(f"\n[3/4] Generating architecture diagrams...")

# ============================================================================
# DIAGRAM 1: Detailed Model Architecture (Vertical Layout)
# ============================================================================
print("\n  [1/5] Creating detailed vertical architecture diagram...")
try:
    plot_model(
        rnn_model,
        to_file='rnn_architecture_detailed.png',
        show_shapes=True,
        show_dtype=False,
        show_layer_names=True,
        rankdir='TB',  # Top to Bottom
        expand_nested=True,
        dpi=300,
        show_layer_activations=True
    )
    print("    ✓ Saved: rnn_architecture_detailed.png")
except Exception as e:
    print(f"    ✗ Error: {e}")

# ============================================================================
# DIAGRAM 2: Horizontal Model Architecture
# ============================================================================
print("  [2/5] Creating horizontal architecture diagram...")
try:
    plot_model(
        rnn_model,
        to_file='rnn_architecture_horizontal.png',
        show_shapes=True,
        show_dtype=False,
        show_layer_names=True,
        rankdir='LR',  # Left to Right
        expand_nested=True,
        dpi=300,
        show_layer_activations=True
    )
    print("    ✓ Saved: rnn_architecture_horizontal.png")
except Exception as e:
    print(f"    ✗ Error: {e}")

# ============================================================================
# DIAGRAM 3: Simple Architecture (No shapes)
# ============================================================================
print("  [3/5] Creating simple architecture diagram...")
try:
    plot_model(
        rnn_model,
        to_file='rnn_architecture_simple.png',
        show_shapes=False,
        show_dtype=False,
        show_layer_names=True,
        rankdir='TB',
        expand_nested=False,
        dpi=300
    )
    print("    ✓ Saved: rnn_architecture_simple.png")
except Exception as e:
    print(f"    ✗ Error: {e}")

# ============================================================================
# DIAGRAM 4: Model Summary Visualization
# ============================================================================
print("  [4/5] Creating model summary visualization...")

fig, ax = plt.subplots(figsize=(14, 12))
ax.axis('off')

# Get model summary as string
summary_lines = []
rnn_model.summary(print_fn=lambda x: summary_lines.append(x))
summary_text = '\n'.join(summary_lines)

# Create visualization
ax.text(0.5, 0.5, summary_text, ha='center', va='center',
        fontsize=8, family='monospace',
        bbox=dict(boxstyle='round', facecolor='#E8F5E9', alpha=0.9, linewidth=2))

plt.title('RNN Model Summary', fontsize=16, fontweight='bold', pad=20)
plt.tight_layout()
plt.savefig('rnn_model_summary.png', dpi=300, bbox_inches='tight')
print("    ✓ Saved: rnn_model_summary.png")
plt.close()

# ============================================================================
# DIAGRAM 5: Training History Visualization (if available)
# ============================================================================
print("  [5/5] Creating training history visualization...")

try:
    with open('training_history.json', 'r') as f:
        history_data = json.load(f)
    
    if 'rnn' in history_data:
        rnn_history = history_data['rnn']
        
        fig, axes = plt.subplots(2, 2, figsize=(16, 12))
        fig.suptitle('RNN Model Training History', fontsize=18, fontweight='bold')
        
        # Plot 1: Training & Validation Accuracy
        ax1 = axes[0, 0]
        if 'accuracy' in rnn_history:
            epochs = range(1, len(rnn_history['accuracy']) + 1)
            ax1.plot(epochs, rnn_history['accuracy'], 'b-', label='Training Accuracy', linewidth=2)
            if 'val_accuracy' in rnn_history:
                ax1.plot(epochs, rnn_history['val_accuracy'], 'r--', label='Validation Accuracy', linewidth=2)
            ax1.set_title('Model Accuracy', fontsize=14, fontweight='bold')
            ax1.set_xlabel('Epoch')
            ax1.set_ylabel('Accuracy')
            ax1.legend()
            ax1.grid(True, alpha=0.3)
        
        # Plot 2: Training & Validation Loss
        ax2 = axes[0, 1]
        if 'loss' in rnn_history:
            epochs = range(1, len(rnn_history['loss']) + 1)
            ax2.plot(epochs, rnn_history['loss'], 'b-', label='Training Loss', linewidth=2)
            if 'val_loss' in rnn_history:
                ax2.plot(epochs, rnn_history['val_loss'], 'r--', label='Validation Loss', linewidth=2)
            ax2.set_title('Model Loss', fontsize=14, fontweight='bold')
            ax2.set_xlabel('Epoch')
            ax2.set_ylabel('Loss')
            ax2.legend()
            ax2.grid(True, alpha=0.3)
        
        # Plot 3: Learning Progress
        ax3 = axes[1, 0]
        if 'accuracy' in rnn_history:
            epochs = range(1, len(rnn_history['accuracy']) + 1)
            ax3.plot(epochs, rnn_history['accuracy'], 'g-', linewidth=2)
            ax3.fill_between(epochs, rnn_history['accuracy'], alpha=0.3)
            ax3.set_title('Training Progress', fontsize=14, fontweight='bold')
            ax3.set_xlabel('Epoch')
            ax3.set_ylabel('Training Accuracy')
            ax3.grid(True, alpha=0.3)
            
            # Add final accuracy annotation
            final_acc = rnn_history['accuracy'][-1]
            ax3.annotate(f'Final: {final_acc:.4f}',
                        xy=(len(epochs), final_acc),
                        xytext=(len(epochs)*0.7, final_acc-0.1),
                        arrowprops=dict(arrowstyle='->', color='red', lw=2),
                        fontsize=12, fontweight='bold')
        
        # Plot 4: Overfitting Analysis
        ax4 = axes[1, 1]
        if 'accuracy' in rnn_history and 'val_accuracy' in rnn_history:
            epochs = range(1, len(rnn_history['accuracy']) + 1)
            gap = [abs(t - v) for t, v in zip(rnn_history['accuracy'], rnn_history['val_accuracy'])]
            ax4.plot(epochs, gap, 'orange', linewidth=2)
            ax4.fill_between(epochs, gap, alpha=0.3, color='orange')
            ax4.set_title('Train-Val Accuracy Gap (Overfitting Check)', fontsize=14, fontweight='bold')
            ax4.set_xlabel('Epoch')
            ax4.set_ylabel('Accuracy Difference')
            ax4.grid(True, alpha=0.3)
            ax4.axhline(y=0.05, color='green', linestyle='--', label='Good (<5%)', alpha=0.5)
            ax4.axhline(y=0.10, color='red', linestyle='--', label='Warning (>10%)', alpha=0.5)
            ax4.legend()
        
        plt.tight_layout()
        plt.savefig('rnn_training_history.png', dpi=300, bbox_inches='tight')
        print("    ✓ Saved: rnn_training_history.png")
        plt.close()
    else:
        print("    ⚠ RNN training history not found in training_history.json")
        
except FileNotFoundError:
    print("    ⚠ training_history.json not found, skipping training history visualization")
except Exception as e:
    print(f"    ⚠ Error creating training history: {e}")

# ============================================================================
# Print Model Summary to Console
# ============================================================================
print("\n[4/4] Model Architecture Summary:")
print("="*80)
rnn_model.summary()
print("="*80)

# ============================================================================
# SUMMARY
# ============================================================================
print("\n" + "="*80)
print("RNN ARCHITECTURE DIAGRAM GENERATION COMPLETE!")
print("="*80)
print("\n📊 Generated architecture diagrams:")
print("   1. rnn_architecture_detailed.png   - Full architecture with shapes (vertical)")
print("   2. rnn_architecture_horizontal.png - Full architecture with shapes (horizontal)")
print("   3. rnn_architecture_simple.png     - Simplified architecture diagram")
print("   4. rnn_model_summary.png           - Model summary as image")
print("   5. rnn_training_history.png        - Training history plots (if available)")
print("\n💡 These are the ACTUAL model architecture diagrams from your trained model!")
print("="*80 + "\n")
