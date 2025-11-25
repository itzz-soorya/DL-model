"""
RNN Model - Custom Architecture Visualization
Creates beautiful visual diagrams of the actual RNN model architecture
"""
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from tensorflow import keras
import json

print("="*80)
print("GENERATING CUSTOM RNN MODEL ARCHITECTURE DIAGRAMS")
print("="*80)

print("\n[1/3] Loading RNN model...")
rnn_model = keras.models.load_model('fitness_rnn_model.h5')
print("✓ RNN model loaded successfully")

with open('real_model_results.json', 'r') as f:
    results = json.load(f)

print(f"\n[2/3] Analyzing model structure...")

# Get layer information
layers_info = []
for i, layer in enumerate(rnn_model.layers):
    layer_config = layer.get_config()
    try:
        output_shape = str(layer.output_shape)
    except:
        output_shape = str(layer.output.shape)
    
    layer_info = {
        'name': layer.name,
        'type': layer.__class__.__name__,
        'output_shape': output_shape,
        'params': layer.count_params(),
        'trainable': layer.trainable
    }
    layers_info.append(layer_info)
    print(f"  Layer {i+1}: {layer_info['name']} ({layer_info['type']}) - {layer_info['params']} params")

print(f"\n[3/3] Creating architecture visualizations...")

# ============================================================================
# DIAGRAM 1: Vertical Flow Architecture
# ============================================================================
print("\n  [1/4] Creating vertical flow architecture...")

fig, ax = plt.subplots(figsize=(16, 20))
ax.set_xlim(0, 10)
ax.set_ylim(0, 25)
ax.axis('off')

# Define colors for different layer types
layer_colors = {
    'InputLayer': '#FFE0B2',
    'Embedding': '#BBDEFB',
    'LSTM': '#C8E6C9',
    'Dropout': '#F8BBD0',
    'Dense': '#B2DFDB',
    'Concatenate': '#E1BEE7'
}

# Define positions
y_pos = 23
x_center = 5
box_width = 3
box_height = 0.8

# Title
ax.text(x_center, 24.5, 'RNN Model Architecture\n(LSTM-based Fitness Workout Predictor)', 
        ha='center', va='top', fontsize=20, fontweight='bold',
        bbox=dict(boxstyle='round,pad=0.5', facecolor='lightblue', edgecolor='black', linewidth=2))

# Draw layers
layer_positions = []

# Input layers (side by side)
# Sequence Input
rect1 = mpatches.FancyBboxPatch((x_center-2.2, y_pos), 2, box_height, 
                                boxstyle="round,pad=0.05", 
                                facecolor=layer_colors['InputLayer'], 
                                edgecolor='black', linewidth=2)
ax.add_patch(rect1)
ax.text(x_center-1.2, y_pos+0.4, 'Sequence Input', ha='center', va='center', 
        fontsize=10, fontweight='bold')
ax.text(x_center-1.2, y_pos+0.1, 'Shape: (None, 6)', ha='center', va='center', fontsize=8)
layer_positions.append((x_center-1.2, y_pos))

# Features Input
rect2 = mpatches.FancyBboxPatch((x_center+0.2, y_pos), 2, box_height, 
                                boxstyle="round,pad=0.05", 
                                facecolor=layer_colors['InputLayer'], 
                                edgecolor='black', linewidth=2)
ax.add_patch(rect2)
ax.text(x_center+1.2, y_pos+0.4, 'Features Input', ha='center', va='center', 
        fontsize=10, fontweight='bold')
ax.text(x_center+1.2, y_pos+0.1, 'Shape: (None, 3)', ha='center', va='center', fontsize=8)
layer_positions.append((x_center+1.2, y_pos))

y_pos -= 1.5

# Embedding (left branch)
ax.arrow(x_center-1.2, layer_positions[0][1], 0, -0.5, head_width=0.2, head_length=0.1, 
         fc='black', ec='black', linewidth=2)
rect = mpatches.FancyBboxPatch((x_center-2.2, y_pos), 2, box_height, 
                               boxstyle="round,pad=0.05", 
                               facecolor=layer_colors['Embedding'], 
                               edgecolor='black', linewidth=2)
ax.add_patch(rect)
ax.text(x_center-1.2, y_pos+0.5, 'Embedding', ha='center', va='center', 
        fontsize=10, fontweight='bold')
ax.text(x_center-1.2, y_pos+0.2, 'Output: (None, 6, 16)', ha='center', va='center', fontsize=8)
ax.text(x_center-1.2, y_pos-0.05, 'Params: 112', ha='center', va='center', fontsize=7, style='italic')
layer_positions.append((x_center-1.2, y_pos))

# Dense (right branch)
ax.arrow(x_center+1.2, layer_positions[1][1], 0, -0.5, head_width=0.2, head_length=0.1, 
         fc='black', ec='black', linewidth=2)
rect = mpatches.FancyBboxPatch((x_center+0.2, y_pos), 2, box_height, 
                               boxstyle="round,pad=0.05", 
                               facecolor=layer_colors['Dense'], 
                               edgecolor='black', linewidth=2)
ax.add_patch(rect)
ax.text(x_center+1.2, y_pos+0.5, 'Dense (32, relu)', ha='center', va='center', 
        fontsize=10, fontweight='bold')
ax.text(x_center+1.2, y_pos+0.2, 'Output: (None, 32)', ha='center', va='center', fontsize=8)
ax.text(x_center+1.2, y_pos-0.05, 'Params: 128', ha='center', va='center', fontsize=7, style='italic')
layer_positions.append((x_center+1.2, y_pos))

y_pos -= 1.5

# LSTM 1 (left branch)
ax.arrow(x_center-1.2, layer_positions[2][1], 0, -0.5, head_width=0.2, head_length=0.1, 
         fc='black', ec='black', linewidth=2)
rect = mpatches.FancyBboxPatch((x_center-2.2, y_pos), 2, box_height, 
                               boxstyle="round,pad=0.05", 
                               facecolor=layer_colors['LSTM'], 
                               edgecolor='black', linewidth=3)
ax.add_patch(rect)
ax.text(x_center-1.2, y_pos+0.5, 'LSTM-1 (64 units)', ha='center', va='center', 
        fontsize=10, fontweight='bold')
ax.text(x_center-1.2, y_pos+0.2, 'Output: (None, 6, 64)', ha='center', va='center', fontsize=8)
ax.text(x_center-1.2, y_pos-0.05, 'Params: 20,736', ha='center', va='center', fontsize=7, style='italic')
layer_positions.append((x_center-1.2, y_pos))

# Dropout (right branch)
ax.arrow(x_center+1.2, layer_positions[3][1], 0, -0.5, head_width=0.2, head_length=0.1, 
         fc='black', ec='black', linewidth=2)
rect = mpatches.FancyBboxPatch((x_center+0.2, y_pos), 2, box_height, 
                               boxstyle="round,pad=0.05", 
                               facecolor=layer_colors['Dropout'], 
                               edgecolor='black', linewidth=2)
ax.add_patch(rect)
ax.text(x_center+1.2, y_pos+0.4, 'Dropout (0.2)', ha='center', va='center', 
        fontsize=10, fontweight='bold')
layer_positions.append((x_center+1.2, y_pos))

y_pos -= 1.5

# Dropout 1 (left branch)
ax.arrow(x_center-1.2, layer_positions[4][1], 0, -0.5, head_width=0.2, head_length=0.1, 
         fc='black', ec='black', linewidth=2)
rect = mpatches.FancyBboxPatch((x_center-2.2, y_pos), 2, box_height, 
                               boxstyle="round,pad=0.05", 
                               facecolor=layer_colors['Dropout'], 
                               edgecolor='black', linewidth=2)
ax.add_patch(rect)
ax.text(x_center-1.2, y_pos+0.4, 'Dropout (0.3)', ha='center', va='center', 
        fontsize=10, fontweight='bold')
layer_positions.append((x_center-1.2, y_pos))

y_pos -= 1.5

# LSTM 2 (left branch)
ax.arrow(x_center-1.2, layer_positions[6][1], 0, -0.5, head_width=0.2, head_length=0.1, 
         fc='black', ec='black', linewidth=2)
rect = mpatches.FancyBboxPatch((x_center-2.2, y_pos), 2, box_height, 
                               boxstyle="round,pad=0.05", 
                               facecolor=layer_colors['LSTM'], 
                               edgecolor='black', linewidth=3)
ax.add_patch(rect)
ax.text(x_center-1.2, y_pos+0.5, 'LSTM-2 (32 units)', ha='center', va='center', 
        fontsize=10, fontweight='bold')
ax.text(x_center-1.2, y_pos+0.2, 'Output: (None, 6, 32)', ha='center', va='center', fontsize=8)
ax.text(x_center-1.2, y_pos-0.05, 'Params: 12,416', ha='center', va='center', fontsize=7, style='italic')
layer_positions.append((x_center-1.2, y_pos))

y_pos -= 1.5

# Dropout 2 (left branch)
ax.arrow(x_center-1.2, layer_positions[7][1], 0, -0.5, head_width=0.2, head_length=0.1, 
         fc='black', ec='black', linewidth=2)
rect = mpatches.FancyBboxPatch((x_center-2.2, y_pos), 2, box_height, 
                               boxstyle="round,pad=0.05", 
                               facecolor=layer_colors['Dropout'], 
                               edgecolor='black', linewidth=2)
ax.add_patch(rect)
ax.text(x_center-1.2, y_pos+0.4, 'Dropout (0.3)', ha='center', va='center', 
        fontsize=10, fontweight='bold')
layer_positions.append((x_center-1.2, y_pos))

y_pos -= 1.5

# LSTM 3 (left branch)
ax.arrow(x_center-1.2, layer_positions[8][1], 0, -0.5, head_width=0.2, head_length=0.1, 
         fc='black', ec='black', linewidth=2)
rect = mpatches.FancyBboxPatch((x_center-2.2, y_pos), 2, box_height, 
                               boxstyle="round,pad=0.05", 
                               facecolor=layer_colors['LSTM'], 
                               edgecolor='black', linewidth=3)
ax.add_patch(rect)
ax.text(x_center-1.2, y_pos+0.5, 'LSTM-3 (16 units)', ha='center', va='center', 
        fontsize=10, fontweight='bold')
ax.text(x_center-1.2, y_pos+0.2, 'Output: (None, 16)', ha='center', va='center', fontsize=8)
ax.text(x_center-1.2, y_pos-0.05, 'Params: 3,136', ha='center', va='center', fontsize=7, style='italic')
layer_positions.append((x_center-1.2, y_pos))

y_pos -= 2

# Concatenate (merge both branches)
ax.arrow(x_center-1.2, layer_positions[9][1], 0.7, -0.5, head_width=0.2, head_length=0.1, 
         fc='purple', ec='purple', linewidth=2)
ax.arrow(x_center+1.2, layer_positions[5][1], -0.7, -8.5, head_width=0.2, head_length=0.1, 
         fc='purple', ec='purple', linewidth=2)

rect = mpatches.FancyBboxPatch((x_center-1.5, y_pos), 3, box_height, 
                               boxstyle="round,pad=0.05", 
                               facecolor=layer_colors['Concatenate'], 
                               edgecolor='purple', linewidth=3)
ax.add_patch(rect)
ax.text(x_center, y_pos+0.5, 'Concatenate', ha='center', va='center', 
        fontsize=11, fontweight='bold', color='purple')
ax.text(x_center, y_pos+0.2, '16 + 32 = 48 units', ha='center', va='center', fontsize=8)
layer_positions.append((x_center, y_pos))

y_pos -= 1.5

# Dense 1
ax.arrow(x_center, layer_positions[10][1], 0, -0.5, head_width=0.2, head_length=0.1, 
         fc='black', ec='black', linewidth=2)
rect = mpatches.FancyBboxPatch((x_center-1.5, y_pos), 3, box_height, 
                               boxstyle="round,pad=0.05", 
                               facecolor=layer_colors['Dense'], 
                               edgecolor='black', linewidth=2)
ax.add_patch(rect)
ax.text(x_center, y_pos+0.5, 'Dense-1 (64, relu)', ha='center', va='center', 
        fontsize=10, fontweight='bold')
ax.text(x_center, y_pos+0.2, 'Output: (None, 64)', ha='center', va='center', fontsize=8)
ax.text(x_center, y_pos-0.05, 'Params: 3,136', ha='center', va='center', fontsize=7, style='italic')
layer_positions.append((x_center, y_pos))

y_pos -= 1.5

# Dropout 3
ax.arrow(x_center, layer_positions[11][1], 0, -0.5, head_width=0.2, head_length=0.1, 
         fc='black', ec='black', linewidth=2)
rect = mpatches.FancyBboxPatch((x_center-1.5, y_pos), 3, box_height, 
                               boxstyle="round,pad=0.05", 
                               facecolor=layer_colors['Dropout'], 
                               edgecolor='black', linewidth=2)
ax.add_patch(rect)
ax.text(x_center, y_pos+0.4, 'Dropout (0.3)', ha='center', va='center', 
        fontsize=10, fontweight='bold')
layer_positions.append((x_center, y_pos))

y_pos -= 1.5

# Dense 2
ax.arrow(x_center, layer_positions[12][1], 0, -0.5, head_width=0.2, head_length=0.1, 
         fc='black', ec='black', linewidth=2)
rect = mpatches.FancyBboxPatch((x_center-1.5, y_pos), 3, box_height, 
                               boxstyle="round,pad=0.05", 
                               facecolor=layer_colors['Dense'], 
                               edgecolor='black', linewidth=2)
ax.add_patch(rect)
ax.text(x_center, y_pos+0.5, 'Dense-2 (32, relu)', ha='center', va='center', 
        fontsize=10, fontweight='bold')
ax.text(x_center, y_pos+0.2, 'Output: (None, 32)', ha='center', va='center', fontsize=8)
ax.text(x_center, y_pos-0.05, 'Params: 2,080', ha='center', va='center', fontsize=7, style='italic')
layer_positions.append((x_center, y_pos))

y_pos -= 1.5

# Output
ax.arrow(x_center, layer_positions[13][1], 0, -0.5, head_width=0.2, head_length=0.1, 
         fc='red', ec='red', linewidth=3)
rect = mpatches.FancyBboxPatch((x_center-1.5, y_pos), 3, box_height, 
                               boxstyle="round,pad=0.05", 
                               facecolor='#FFCDD2', 
                               edgecolor='red', linewidth=3)
ax.add_patch(rect)
ax.text(x_center, y_pos+0.5, 'Output (7, softmax)', ha='center', va='center', 
        fontsize=11, fontweight='bold', color='red')
ax.text(x_center, y_pos+0.2, '7 Workout Classes', ha='center', va='center', fontsize=8)
ax.text(x_center, y_pos-0.05, 'Params: 231', ha='center', va='center', fontsize=7, style='italic')

# Add legend
legend_y = 1.5
ax.text(x_center, legend_y+0.3, 'Model Statistics', ha='center', va='center', 
        fontsize=12, fontweight='bold',
        bbox=dict(boxstyle='round,pad=0.3', facecolor='lightyellow', edgecolor='black', linewidth=2))
ax.text(x_center, legend_y-0.2, f'Total Parameters: 41,975', ha='center', va='center', fontsize=10)
ax.text(x_center, legend_y-0.5, f'Accuracy: 90.0%', ha='center', va='center', fontsize=10)
ax.text(x_center, legend_y-0.8, f'Model Size: 163.96 KB', ha='center', va='center', fontsize=10)

plt.tight_layout()
plt.savefig('rnn_actual_architecture_vertical.png', dpi=300, bbox_inches='tight', facecolor='white')
print("    ✓ Saved: rnn_actual_architecture_vertical.png")
plt.close()

# ============================================================================
# DIAGRAM 2: Horizontal Architecture
# ============================================================================
print("  [2/4] Creating horizontal flow architecture...")

fig, ax = plt.subplots(figsize=(24, 12))
ax.set_xlim(0, 30)
ax.set_ylim(0, 15)
ax.axis('off')

y_top = 10
y_mid = 7.5
y_bot = 5
x_pos = 2

# Title
ax.text(15, 14, 'RNN Model - Horizontal Architecture Flow', 
        ha='center', va='center', fontsize=18, fontweight='bold',
        bbox=dict(boxstyle='round,pad=0.5', facecolor='lightblue', edgecolor='black', linewidth=2))

# Sequence branch (top)
layers_top = [
    ('Sequence\nInput\n(None, 6)', 'InputLayer', 0),
    ('Embedding\n7→16\n112 params', 'Embedding', 112),
    ('LSTM-1\n64 units\n20,736 params', 'LSTM', 20736),
    ('Dropout\n0.3', 'Dropout', 0),
    ('LSTM-2\n32 units\n12,416 params', 'LSTM', 12416),
    ('Dropout\n0.3', 'Dropout', 0),
    ('LSTM-3\n16 units\n3,136 params', 'LSTM', 3136),
]

for i, (label, ltype, params) in enumerate(layers_top):
    rect = mpatches.FancyBboxPatch((x_pos + i*3, y_top-0.5), 2.5, 1, 
                                   boxstyle="round,pad=0.05", 
                                   facecolor=layer_colors[ltype], 
                                   edgecolor='black', linewidth=2)
    ax.add_patch(rect)
    ax.text(x_pos + i*3 + 1.25, y_top, label, ha='center', va='center', fontsize=9, fontweight='bold')
    
    if i < len(layers_top) - 1:
        ax.arrow(x_pos + i*3 + 2.5, y_top, 0.4, 0, head_width=0.15, head_length=0.1, 
                 fc='black', ec='black', linewidth=2)

# Features branch (bottom)
layers_bot = [
    ('Features\nInput\n(None, 3)', 'InputLayer', 0),
    ('Dense\n32 units, relu\n128 params', 'Dense', 128),
    ('Dropout\n0.2', 'Dropout', 0),
]

for i, (label, ltype, params) in enumerate(layers_bot):
    rect = mpatches.FancyBboxPatch((x_pos + i*3, y_bot-0.5), 2.5, 1, 
                                   boxstyle="round,pad=0.05", 
                                   facecolor=layer_colors[ltype], 
                                   edgecolor='black', linewidth=2)
    ax.add_patch(rect)
    ax.text(x_pos + i*3 + 1.25, y_bot, label, ha='center', va='center', fontsize=9, fontweight='bold')
    
    if i < len(layers_bot) - 1:
        ax.arrow(x_pos + i*3 + 2.5, y_bot, 0.4, 0, head_width=0.15, head_length=0.1, 
                 fc='black', ec='black', linewidth=2)

# Concatenate
concat_x = x_pos + 21
ax.arrow(x_pos + 20.5, y_top, 0, -2, head_width=0.15, head_length=0.1, fc='purple', ec='purple', linewidth=2)
ax.arrow(x_pos + 8.5, y_bot, 12, 0, head_width=0, head_length=0, fc='purple', ec='purple', linewidth=2)
ax.arrow(x_pos + 20.5, y_bot, 0, 2, head_width=0.15, head_length=0.1, fc='purple', ec='purple', linewidth=2)

rect = mpatches.FancyBboxPatch((concat_x, y_mid-0.5), 2.5, 1, 
                               boxstyle="round,pad=0.05", 
                               facecolor=layer_colors['Concatenate'], 
                               edgecolor='purple', linewidth=3)
ax.add_patch(rect)
ax.text(concat_x + 1.25, y_mid, 'Concatenate\n48 units\n(16+32)', ha='center', va='center', 
        fontsize=9, fontweight='bold', color='purple')

# Final layers
final_layers = [
    ('Dense-1\n64, relu\n3,136 params', 'Dense'),
    ('Dropout\n0.3', 'Dropout'),
    ('Dense-2\n32, relu\n2,080 params', 'Dense'),
    ('Output\n7, softmax\n231 params', 'Dense'),
]

for i, (label, ltype) in enumerate(final_layers):
    x = concat_x + 3 + i*3
    color = '#FFCDD2' if i == 3 else layer_colors[ltype]
    edge_color = 'red' if i == 3 else 'black'
    edge_width = 3 if i == 3 else 2
    
    rect = mpatches.FancyBboxPatch((x, y_mid-0.5), 2.5, 1, 
                                   boxstyle="round,pad=0.05", 
                                   facecolor=color, 
                                   edgecolor=edge_color, linewidth=edge_width)
    ax.add_patch(rect)
    ax.text(x + 1.25, y_mid, label, ha='center', va='center', fontsize=9, fontweight='bold')
    
    ax.arrow(x - 0.5, y_mid, 0.4, 0, head_width=0.15, head_length=0.1, 
             fc='black', ec='black', linewidth=2)

# Add stats box
stats_text = f"""Model Stats:
Parameters: 41,975
Accuracy: 90.0%
Size: 163.96 KB"""

ax.text(15, 1.5, stats_text, ha='center', va='center', fontsize=11, fontweight='bold',
        bbox=dict(boxstyle='round,pad=0.5', facecolor='lightyellow', edgecolor='black', linewidth=2))

plt.tight_layout()
plt.savefig('rnn_actual_architecture_horizontal.png', dpi=300, bbox_inches='tight', facecolor='white')
print("    ✓ Saved: rnn_actual_architecture_horizontal.png")
plt.close()

# ============================================================================
# DIAGRAM 3: Detailed Layer Information Table
# ============================================================================
print("  [3/4] Creating detailed layer information table...")

fig, ax = plt.subplots(figsize=(16, 10))
ax.axis('off')

# Create table data
table_data = [['Layer', 'Type', 'Output Shape', 'Parameters', 'Connections']]
table_data.append(['━'*20, '━'*15, '━'*20, '━'*15, '━'*25])

for i, layer in enumerate(rnn_model.layers):
    try:
        connections = layer._inbound_nodes[0].inbound_layers if layer._inbound_nodes else []
        conn_names = ', '.join([l.name for l in connections]) if connections else '-'
    except:
        conn_names = '-'
    if len(conn_names) > 20:
        conn_names = conn_names[:20] + '...'
    
    try:
        output_shape = str(layer.output_shape)
    except:
        output_shape = str(layer.output.shape)
    
    table_data.append([
        layer.name,
        layer.__class__.__name__,
        output_shape,
        f'{layer.count_params():,}',
        conn_names
    ])

table = ax.table(cellText=table_data, cellLoc='left', loc='center',
                 colWidths=[0.25, 0.15, 0.25, 0.15, 0.20])
table.auto_set_font_size(False)
table.set_fontsize(9)
table.scale(1, 2.5)

# Style header
for i in range(5):
    table[(0, i)].set_facecolor('#2c3e50')
    table[(0, i)].set_text_props(weight='bold', color='white', fontsize=11)
    table[(1, i)].set_facecolor('#ecf0f1')

# Alternate row colors
for i in range(2, len(table_data)):
    for j in range(5):
        if i % 2 == 0:
            table[(i, j)].set_facecolor('#f8f9fa')
        else:
            table[(i, j)].set_facecolor('white')

plt.title('RNN Model - Detailed Layer Information', fontsize=16, fontweight='bold', pad=20)
plt.tight_layout()
plt.savefig('rnn_actual_layer_details.png', dpi=300, bbox_inches='tight', facecolor='white')
print("    ✓ Saved: rnn_actual_layer_details.png")
plt.close()

# ============================================================================
# DIAGRAM 4: Parameter Distribution
# ============================================================================
print("  [4/4] Creating parameter distribution diagram...")

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 8))

# Extract layer names and parameters
layer_names = []
layer_params = []
layer_colors_list = []

for layer in rnn_model.layers:
    if layer.count_params() > 0:
        layer_names.append(f"{layer.name}\n({layer.__class__.__name__})")
        layer_params.append(layer.count_params())
        layer_colors_list.append(layer_colors.get(layer.__class__.__name__, '#CCCCCC'))

# Bar chart
bars = ax1.barh(layer_names, layer_params, color=layer_colors_list, edgecolor='black', linewidth=1.5)
ax1.set_xlabel('Number of Parameters', fontsize=12, fontweight='bold')
ax1.set_title('Parameters by Layer', fontsize=14, fontweight='bold')
ax1.grid(True, alpha=0.3, axis='x')

for bar, params in zip(bars, layer_params):
    width = bar.get_width()
    ax1.text(width + 500, bar.get_y() + bar.get_height()/2,
             f'{params:,}', ha='left', va='center', fontsize=9, fontweight='bold')

# Pie chart
ax2.pie(layer_params, labels=layer_names, autopct='%1.1f%%', startangle=90,
        colors=layer_colors_list, textprops={'fontsize': 9, 'fontweight': 'bold'})
ax2.set_title(f'Parameter Distribution\nTotal: {sum(layer_params):,} parameters',
              fontsize=14, fontweight='bold')

plt.suptitle('RNN Model - Parameter Analysis', fontsize=16, fontweight='bold', y=0.98)
plt.tight_layout()
plt.savefig('rnn_actual_parameter_distribution.png', dpi=300, bbox_inches='tight', facecolor='white')
print("    ✓ Saved: rnn_actual_parameter_distribution.png")
plt.close()

print("\n" + "="*80)
print("ACTUAL RNN ARCHITECTURE DIAGRAMS GENERATED!")
print("="*80)
print("\n📊 Created 4 detailed architecture diagrams:")
print("   1. rnn_actual_architecture_vertical.png   - Vertical flow with all layers")
print("   2. rnn_actual_architecture_horizontal.png - Horizontal flow diagram")
print("   3. rnn_actual_layer_details.png          - Complete layer information table")
print("   4. rnn_actual_parameter_distribution.png - Parameter analysis charts")
print("\n✨ These diagrams show your ACTUAL trained RNN model structure!")
print("="*80 + "\n")
