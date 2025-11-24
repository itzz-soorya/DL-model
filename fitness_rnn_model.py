"""
Fitness Plan Generator - RNN Model
Recurrent Neural Network for sequential fitness plan generation
"""

import numpy as np
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers, models
from tensorflow.keras.preprocessing.sequence import pad_sequences
from sklearn.model_selection import train_test_split
import json

# Generate synthetic sequential training data
# Each sequence represents a week of workouts
np.random.seed(42)

# Workout types encoded as numbers
workout_types = {
    'rest': 0,
    'cardio': 1,
    'strength': 2,
    'hiit': 3,
    'yoga': 4,
    'swimming': 5,
    'cycling': 6
}

# Generate training sequences
def generate_workout_sequence(level, goal):
    """Generate a weekly workout sequence"""
    sequence = []
    
    if level == 0:  # Beginner
        if goal == 0:  # Weight loss
            sequence = [1, 0, 2, 0, 1, 0, 4]  # Cardio, rest, strength, rest, cardio, rest, yoga
        elif goal == 1:  # Muscle gain
            sequence = [2, 0, 2, 0, 2, 2, 0]
        else:  # Fitness
            sequence = [1, 2, 0, 3, 0, 1, 4]
    elif level == 1:  # Intermediate
        if goal == 0:  # Weight loss
            sequence = [3, 1, 2, 1, 3, 6, 0]
        elif goal == 1:  # Muscle gain
            sequence = [2, 2, 0, 2, 2, 2, 0]
        else:  # Fitness
            sequence = [2, 3, 1, 2, 3, 5, 4]
    else:  # Advanced
        if goal == 0:  # Weight loss
            sequence = [3, 3, 2, 3, 3, 6, 1]
        elif goal == 1:  # Muscle gain
            sequence = [2, 2, 2, 2, 2, 2, 0]
        else:  # Fitness
            sequence = [3, 2, 3, 2, 3, 5, 2]
    
    return sequence

# Create training data
training_sequences = []
training_labels = []
user_features = []

for _ in range(2000):
    level = np.random.randint(0, 3)
    goal = np.random.randint(0, 3)
    age = np.random.randint(18, 65)
    
    # Generate sequence
    sequence = generate_workout_sequence(level, goal)
    
    # Add some randomness
    for i in range(len(sequence)):
        if np.random.random() < 0.1:  # 10% chance to modify
            sequence[i] = np.random.randint(0, 7)
    
    # Use first 6 days to predict 7th day
    training_sequences.append(sequence[:6])
    training_labels.append(sequence[6])
    user_features.append([age / 100.0, level / 2.0, goal / 2.0])  # Normalized

# Convert to numpy arrays
X_seq = np.array(training_sequences)
X_features = np.array(user_features)
y = np.array(training_labels)

# Split data
X_seq_train, X_seq_test, X_feat_train, X_feat_test, y_train, y_test = train_test_split(
    X_seq, X_features, y, test_size=0.2, random_state=42
)

# Build RNN Model with LSTM
def create_rnn_model():
    # Sequence input
    sequence_input = layers.Input(shape=(6,), name='sequence_input')
    
    # Embedding layer
    embedded = layers.Embedding(input_dim=7, output_dim=16)(sequence_input)
    
    # LSTM layers
    lstm_out = layers.LSTM(64, return_sequences=True)(embedded)
    lstm_out = layers.Dropout(0.3)(lstm_out)
    lstm_out = layers.LSTM(32, return_sequences=True)(lstm_out)
    lstm_out = layers.Dropout(0.3)(lstm_out)
    lstm_out = layers.LSTM(16)(lstm_out)
    
    # User features input
    features_input = layers.Input(shape=(3,), name='features_input')
    features_dense = layers.Dense(32, activation='relu')(features_input)
    features_dense = layers.Dropout(0.2)(features_dense)
    
    # Concatenate LSTM output with user features
    combined = layers.concatenate([lstm_out, features_dense])
    
    # Dense layers
    dense = layers.Dense(64, activation='relu')(combined)
    dense = layers.Dropout(0.3)(dense)
    dense = layers.Dense(32, activation='relu')(dense)
    
    # Output layer (7 workout types)
    output = layers.Dense(7, activation='softmax', name='output')(dense)
    
    # Create model
    model = models.Model(
        inputs=[sequence_input, features_input],
        outputs=output
    )
    
    return model

# Create and compile model
model = create_rnn_model()
model.compile(
    optimizer='adam',
    loss='sparse_categorical_crossentropy',
    metrics=['accuracy']
)

# Model summary
print("=" * 60)
print("FITNESS PLAN RNN MODEL ARCHITECTURE")
print("=" * 60)
model.summary()

# Train the model
print("\n" + "=" * 60)
print("TRAINING RNN MODEL")
print("=" * 60)

history = model.fit(
    [X_seq_train, X_feat_train],
    y_train,
    epochs=100,
    batch_size=64,
    validation_split=0.2,
    verbose=1
)

# Evaluate model
print("\n" + "=" * 60)
print("MODEL EVALUATION")
print("=" * 60)
test_loss, test_accuracy = model.evaluate(
    [X_seq_test, X_feat_test],
    y_test,
    verbose=0
)
print(f"Test Accuracy: {test_accuracy * 100:.2f}%")
print(f"Test Loss: {test_loss:.4f}")

# Save model
model.save('fitness_rnn_model.h5')
print("\n✅ Model saved as 'fitness_rnn_model.h5'")

# Prediction function
def predict_next_workout(past_week, age, level, goal):
    """
    Predict next day's workout based on past week
    
    Args:
        past_week: List of 6 workout types (encoded as numbers)
        age: User age
        level: 0 (beginner), 1 (intermediate), 2 (advanced)
        goal: 0 (weight loss), 1 (muscle gain), 2 (fitness)
    """
    workout_names = ['Rest', 'Cardio', 'Strength', 'HIIT', 'Yoga', 'Swimming', 'Cycling']
    
    # Prepare input
    seq_input = np.array([past_week])
    feat_input = np.array([[age / 100.0, level / 2.0, goal / 2.0]])
    
    # Predict
    prediction = model.predict([seq_input, feat_input], verbose=0)
    predicted_class = np.argmax(prediction)
    confidence = np.max(prediction) * 100
    
    print(f"\n🎯 Prediction Results:")
    print(f"   Past Week: {[workout_names[i] for i in past_week]}")
    print(f"   Next Workout: {workout_names[predicted_class]}")
    print(f"   Confidence: {confidence:.2f}%")
    
    return predicted_class, confidence

# Generate complete week prediction
def generate_weekly_plan(age, level, goal):
    """Generate a complete weekly workout plan"""
    workout_names = ['Rest', 'Cardio', 'Strength', 'HIIT', 'Yoga', 'Swimming', 'Cycling']
    
    # Start with initial pattern
    week = generate_workout_sequence(level, goal)[:2]  # First 2 days
    
    # Predict remaining days
    for day in range(5):  # Predict days 3-7
        if len(week) >= 6:
            past_week = week[-6:]
        else:
            past_week = week + [0] * (6 - len(week))
        
        seq_input = np.array([past_week])
        feat_input = np.array([[age / 100.0, level / 2.0, goal / 2.0]])
        
        prediction = model.predict([seq_input, feat_input], verbose=0)
        next_workout = np.argmax(prediction)
        week.append(next_workout)
    
    print(f"\n📅 Weekly Workout Plan:")
    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    for i, (day, workout) in enumerate(zip(days, week)):
        print(f"   {day}: {workout_names[workout]}")
    
    return week

# Test predictions
print("\n" + "=" * 60)
print("SAMPLE PREDICTION - Next Workout")
print("=" * 60)
print("Input: Past week=[Cardio, Rest, Strength, Rest, Cardio, Rest]")
print("       Age=30, Level=Intermediate, Goal=Weight Loss")
predict_next_workout([1, 0, 2, 0, 1, 0], 30, 1, 0)

print("\n" + "=" * 60)
print("SAMPLE PREDICTION - Full Week Plan")
print("=" * 60)
print("Input: Age=25, Level=Beginner, Goal=Muscle Gain")
generate_weekly_plan(25, 0, 1)

print("\n" + "=" * 60)
print("TRAINING COMPLETE!")
print("=" * 60)
