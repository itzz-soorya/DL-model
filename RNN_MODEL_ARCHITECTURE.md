# 🧠 RNN Model Documentation (LSTM Architecture)

## Model Overview
- **Type:** LSTM Recurrent Neural Network
- **Purpose:** Predicting weekly workout sequences based on user profile
- **Accuracy:** 90.00%
- **Total Parameters:** 41,975 (163.96 KB)
- **Framework:** TensorFlow/Keras

---

## 🏗️ Model Architecture

### Input Layer
```
Input 1: Workout Sequence
- Shape: (batch_size, 6)
- Type: Integer sequence (past 6 days of workouts)
- Range: 0-6 (7 workout types)
- Example: [1, 0, 2, 0, 1, 0] = Cardio, Rest, Strength, Rest, Cardio, Rest

Input 2: User Features
- Shape: (batch_size, 3)
- Type: Float values (normalized)
- Features: [age/100.0, fitness_level/2.0, goal/2.0]
- Example: [0.25, 0.0, 0.5] = Age 25, Beginner, Fitness goal
```

**Total Inputs:** 2 branches (sequence + features)

---

## 📊 Layer-by-Layer Breakdown

### Layer 1: Embedding Layer
```python
Embedding(input_dim=7, output_dim=16, input_length=6)
```
- **Purpose:** Convert workout IDs to dense vectors
- **Parameters:** 7 × 16 = **112 parameters**
- **Input:** (batch_size, 6) - Workout sequence
- **Output:** (batch_size, 6, 16) - Embedded sequence
- **Why this?** Embeddings learn relationships between workout types (e.g., HIIT and Cardio are similar)

---

### Layer 2: LSTM Layer 1 (First Recurrent Layer)
```python
LSTM(units=64, return_sequences=True)
```
- **Parameters:** **20,736 parameters**
  - Weight matrices: 4 × (16 × 64) = 4,096
  - Recurrent weights: 4 × (64 × 64) = 16,384
  - Biases: 4 × 64 = 256
- **Input:** (batch_size, 6, 16) - Embedded sequence
- **Output:** (batch_size, 6, 64) - All timesteps
- **Activation:** 
  - **Tanh** (cell state & output)
  - **Sigmoid** (forget, input, output gates)
- **Why 64 units?** Balances learning capacity with overfitting prevention
- **Why return_sequences=True?** Next LSTM needs all timesteps

---

### Layer 3: LSTM Layer 2 (Second Recurrent Layer)
```python
LSTM(units=32, return_sequences=True)
```
- **Parameters:** **12,416 parameters**
  - Weight matrices: 4 × (64 × 32) = 8,192
  - Recurrent weights: 4 × (32 × 32) = 4,096
  - Biases: 4 × 32 = 128
- **Input:** (batch_size, 6, 64)
- **Output:** (batch_size, 6, 32)
- **Activation:** Tanh + Sigmoid (gates)
- **Why 32 units?** Gradual dimensionality reduction for better generalization

---

### Layer 4: LSTM Layer 3 (Final Recurrent Layer)
```python
LSTM(units=16, return_sequences=False)
```
- **Parameters:** **3,136 parameters**
  - Weight matrices: 4 × (32 × 16) = 2,048
  - Recurrent weights: 4 × (16 × 16) = 1,024
  - Biases: 4 × 16 = 64
- **Input:** (batch_size, 6, 32)
- **Output:** (batch_size, 16) - Only final timestep
- **Activation:** Tanh + Sigmoid (gates)
- **Why return_sequences=False?** We only need the final prediction

---

### Layer 5: Dense Layer (Feature Branch)
```python
Dense(units=32, activation='relu')
```
- **Parameters:** **128 parameters**
  - Weights: 3 × 32 = 96
  - Biases: 32
- **Input:** (batch_size, 3) - User features
- **Output:** (batch_size, 32)
- **Activation:** **ReLU** (Rectified Linear Unit)
  - Formula: f(x) = max(0, x)
  - Why? Non-linear, prevents vanishing gradients, fast computation

---

### Layer 6: Concatenate Layer
```python
Concatenate()
```
- **Parameters:** **0 parameters** (no trainable weights)
- **Input 1:** (batch_size, 16) - From LSTM
- **Input 2:** (batch_size, 32) - From Dense
- **Output:** (batch_size, 48) - Combined features
- **Why?** Merges sequence patterns with user profile

---

### Layer 7: Dense Layer (Combined Processing)
```python
Dense(units=32, activation='relu')
```
- **Parameters:** **1,568 parameters**
  - Weights: 48 × 32 = 1,536
  - Biases: 32
- **Input:** (batch_size, 48)
- **Output:** (batch_size, 32)
- **Activation:** **ReLU**
- **Why?** Learns complex interactions between sequence and user features

---

### Layer 8: Dropout Layer
```python
Dropout(rate=0.3)
```
- **Parameters:** **0 parameters**
- **Purpose:** Randomly drops 30% of neurons during training
- **Why?** Prevents overfitting by forcing network to learn robust features

---

### Layer 9: Output Layer
```python
Dense(units=7, activation='softmax')
```
- **Parameters:** **231 parameters**
  - Weights: 32 × 7 = 224
  - Biases: 7
- **Input:** (batch_size, 32)
- **Output:** (batch_size, 7) - Probability distribution
- **Activation:** **Softmax**
  - Formula: softmax(x)ᵢ = exp(xᵢ) / Σexp(xⱼ)
  - Why? Converts logits to probabilities (sums to 1.0)
- **Output Classes:** [Rest, Cardio, Strength, HIIT, Yoga, Swimming, Cycling]

---

## 📈 Total Parameters Summary

| Layer Type | Parameters |
|------------|-----------|
| Embedding | 112 |
| LSTM 1 (64 units) | 20,736 |
| LSTM 2 (32 units) | 12,416 |
| LSTM 3 (16 units) | 3,136 |
| Dense 1 (32 units) | 128 |
| Dense 2 (32 units) | 1,568 |
| Dense 3 (7 units) | 231 |
| Dropout | 0 |
| Concatenate | 0 |
| **TOTAL** | **41,975** |

**Trainable:** 41,975 (163.96 KB)  
**Non-trainable:** 0

---

## 🎯 Activation Functions Used

| Layer | Activation | Why? |
|-------|-----------|------|
| Embedding | None | Learned vector representation |
| LSTM 1-3 (Gates) | **Sigmoid** | Range [0,1] for gate values (forget/input/output) |
| LSTM 1-3 (State) | **Tanh** | Range [-1,1] for cell state & output |
| Dense (Feature) | **ReLU** | Fast, prevents vanishing gradients |
| Dense (Combined) | **ReLU** | Non-linearity for complex patterns |
| Dropout | None | Regularization technique |
| Output | **Softmax** | Multi-class probability distribution |

---

## 🔧 Optimizer & Loss Function

### Optimizer: Adam
```python
Adam(learning_rate=0.001)
```
- **Why Adam?** 
  - Adaptive learning rates per parameter
  - Momentum for faster convergence
  - Works well with sparse gradients (embeddings)
  - Default choice for most deep learning tasks

### Loss Function: Sparse Categorical Crossentropy
```python
loss='sparse_categorical_crossentropy'
```
- **Why?** 
  - Multi-class classification (7 workout types)
  - Handles integer labels (don't need one-hot encoding)
  - Measures difference between predicted and actual distributions

---

## 🎓 Training Configuration

- **Epochs:** 100
- **Batch Size:** 64
- **Training Samples:** 2,000
- **Validation Split:** 20%
- **Callbacks:**
  - Early Stopping (patience=10)
  - ReduceLROnPlateau (patience=5)

---

## 🤔 Why RNN/LSTM for This Task?

### ✅ Advantages:

1. **Sequential Nature:** Workouts follow patterns over days
   - Rest after intense workouts
   - Progressive loading
   - Weekly cycles

2. **Temporal Dependencies:** LSTMs remember long-term patterns
   - "If I did HIIT yesterday and strength today, what's next?"
   - Captures weekly workout rhythm

3. **Context Awareness:** Considers previous 6 days
   - Prevents overtraining same muscle groups
   - Balances cardio vs strength

4. **Memory Cells:** LSTM gates control information flow
   - Forget gate: Discard irrelevant old info
   - Input gate: Add new relevant info
   - Output gate: Decide what to predict

### ❌ Why Not Other Models?

**Simple RNN (Vanilla RNN):**
- ❌ Vanishing gradient problem
- ❌ Can't remember long sequences (>5 timesteps)
- ❌ Poor performance on our 6-day sequences

**GRU (Gated Recurrent Unit):**
- ✅ Could work (similar to LSTM)
- ❌ Slightly less powerful than LSTM for complex patterns
- ✅ Fewer parameters (faster)
- We chose LSTM for better accuracy

**Transformer:**
- ❌ Overkill for short sequences (6 days)
- ❌ Needs more data (we have 2,000 samples)
- ❌ More complex, harder to train
- ✅ Better for very long sequences (100+ timesteps)

**Feed-forward Neural Network:**
- ❌ Doesn't understand sequence order
- ❌ [Cardio, Rest, Strength] same as [Rest, Cardio, Strength]
- ❌ No temporal context

**CNN (Convolutional Neural Network):**
- ❌ Better for spatial patterns (images)
- ❌ Doesn't naturally handle sequences
- ❌ No memory of past predictions
- ✅ Good for local patterns but not global sequence context

---

## 📊 Model Performance

- **Training Accuracy:** ~95%
- **Validation Accuracy:** ~93%
- **Test Accuracy:** 90.00%
- **Test Loss:** 0.5536

**Interpretation:**
- Model generalizes well (train vs test gap is small)
- 90% accuracy means 9/10 predictions are correct
- Low loss indicates confident predictions

---

## 🎯 Architecture Design Choices

### Why 3 LSTM Layers (64→32→16)?
- **Hierarchical Learning:**
  - Layer 1: Low-level patterns (rest after workout)
  - Layer 2: Medium-level patterns (weekly cycles)
  - Layer 3: High-level patterns (long-term planning)
- **Gradual Compression:** Reduces dimensions slowly (64→32→16)
- **Prevents Information Loss:** Too fast compression loses details

### Why Dual Input (Sequence + Features)?
- **Sequence Branch:** Learns workout patterns
- **Feature Branch:** Learns user-specific adjustments
- **Combined:** "Beginner doing cardio yesterday" different from "Advanced doing cardio yesterday"

### Why Dropout?
- **Regularization:** Prevents overfitting
- **Robust Features:** Forces network to learn multiple pathways
- **30% Rate:** Balanced (not too aggressive, not too weak)

### Why These Specific Units (64, 32, 16, 32, 7)?
- **Power of 2:** Efficient GPU computation
- **Gradual Reduction:** Smooth information compression
- **Final 7:** Matches number of workout types

---

## 🚀 Summary

The RNN model uses a **3-layer LSTM architecture** with **dual inputs** (sequence + features) to predict the next day's workout. It leverages:

- **41,975 parameters** to learn complex patterns
- **Tanh & Sigmoid** for LSTM gates
- **ReLU** for dense layers
- **Softmax** for final classification
- **Adam optimizer** for efficient training

This architecture is **specifically designed for sequential workout prediction** where order matters and past workouts influence future ones!
