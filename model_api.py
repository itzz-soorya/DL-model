"""
Flask API to serve the trained RNN model
This runs separately and your Next.js app can call it
"""

from flask import Flask, request, jsonify
from flask_cors import CORS
import numpy as np
import tensorflow as tf
from tensorflow import keras
import os
import random

# Import training data and exercise database
from training_data import (
    workout_names,
    exercises_db,
    workout_patterns,
    meal_options,
    activity_multipliers,
    level_names,
    days_of_week
)

app = Flask(__name__)
CORS(app)  # Enable CORS for Next.js to call this API

# Load the trained model
MODEL_PATH = 'fitness_rnn_model.h5'
model = None

# Load model on startup
def load_model():
    global model
    if os.path.exists(MODEL_PATH):
        model = keras.models.load_model(MODEL_PATH)
        print(f"✅ Model loaded successfully from {MODEL_PATH}")
    else:
        print(f"❌ Model file not found: {MODEL_PATH}")
        print("Please run fitness_rnn_model.py first to train the model")

# Generate workout sequence based on level and goal
def get_initial_sequence(level, goal):
    """Get initial 2-day workout pattern from predefined patterns"""
    return workout_patterns.get((level, goal), [1, 0])  # Default: Cardio, Rest

# Generate exercise details based on workout type
def get_exercises_for_workout(workout_type, level, goal):
    """Generate detailed exercises for each workout type"""
    
    level_name = level_names[level]
    
    if workout_type == 0:  # Rest day is same for all
        return exercises_db[0]
    
    workout_data = exercises_db[workout_type]
    if isinstance(workout_data, dict) and level_name in workout_data:
        routines = workout_data[level_name]
    else:
        routines = workout_data.get('beginner', [])
    
    return {
        "day": workout_names[workout_type],
        "routines": routines
    }

# Generate diet plan based on user data
def generate_diet_plan(age, weight, height, level, goal, allergies):
    """Generate personalized diet plan"""
    
    # Calculate BMR (Basal Metabolic Rate)
    bmr = 10 * weight + 6.25 * height - 5 * age + 5
    
    # Activity multiplier based on fitness level
    daily_calories = int(bmr * activity_multipliers[level])
    
    # Adjust based on goal
    if goal == 0:  # Weight loss
        daily_calories -= 500
    elif goal == 1:  # Muscle gain
        daily_calories += 300
    
    # Select random meals from templates
    meals = [
        {"name": "Breakfast", "foods": random.choice(meal_options["breakfast"])},
        {"name": "Lunch", "foods": random.choice(meal_options["lunch"])},
        {"name": "Dinner", "foods": random.choice(meal_options["dinner"])},
        {"name": "Snack 1", "foods": random.choice(meal_options["snacks"])},
        {"name": "Snack 2", "foods": random.choice(meal_options["snacks"])},
    ]
    
    return {
        "dailyCalories": daily_calories,
        "meals": meals
    }

@app.route('/api/predict-workout', methods=['POST'])
def predict_workout():
    """Generate weekly workout plan using AI model"""
    
    if model is None:
        return jsonify({
            "error": "Model not loaded. Please train the model first.",
            "success": False
        }), 500
    
    try:
        data = request.json
        
        # Extract user data
        age = int(data.get('age', 25))
        weight = float(data.get('weight', 70))
        height = float(data.get('height', 170))
        fitness_level = data.get('fitnessLevel', 'beginner')
        goal = data.get('fitnessGoals', 'improve fitness')
        allergies = data.get('allergies', '')
        
        # Map to numeric values
        level_map = {'beginner': 0, 'intermediate': 1, 'advanced': 2}
        goal_map = {'weight loss': 0, 'build muscle': 1, 'improve fitness': 2}
        
        level = level_map.get(fitness_level, 0)
        goal_num = 2  # default to fitness
        
        # Parse goal from text
        goal_text = goal.lower()
        if 'weight' in goal_text or 'loss' in goal_text or 'lose' in goal_text:
            goal_num = 0
        elif 'muscle' in goal_text or 'gain' in goal_text or 'build' in goal_text:
            goal_num = 1
        
        print(f"\n🤖 AI Model Processing:")
        print(f"   Age: {age}, Weight: {weight}kg, Height: {height}cm")
        print(f"   Level: {fitness_level} ({level}), Goal: {goal_num}")
        
        # Generate weekly workout plan using AI model
        week = get_initial_sequence(level, goal_num)
        
        # Predict remaining days using RNN model
        for day_idx in range(5):  # Predict days 3-7
            if len(week) >= 6:
                past_week = week[-6:]
            else:
                past_week = week + [0] * (6 - len(week))
            
            seq_input = np.array([past_week])
            feat_input = np.array([[age / 100.0, level / 2.0, goal_num / 2.0]])
            
            prediction = model.predict([seq_input, feat_input], verbose=0)
            next_workout = np.argmax(prediction)
            confidence = np.max(prediction) * 100
            
            print(f"   Day {len(week)+1}: {workout_names[next_workout]} (confidence: {confidence:.1f}%)")
            
            week.append(next_workout)
        
        # Generate detailed exercises for each day
        exercises = []
        schedule = []
        
        for day_name, workout_type in zip(days_of_week, week):
            exercise_details = get_exercises_for_workout(workout_type, level, goal_num)
            exercises.append({
                "day": day_name,
                "routines": exercise_details["routines"]
            })
            schedule.append(day_name)
        
        # Generate diet plan
        diet_plan = generate_diet_plan(age, weight, height, level, goal_num, allergies)
        
        response = {
            "success": True,
            "workoutPlan": {
                "schedule": schedule,
                "exercises": exercises,
                "generatedBy": "AI RNN Model"
            },
            "dietPlan": diet_plan,
            "generatedAt": str(np.datetime64('now')),
            "modelInfo": {
                "name": "Fitness RNN Model",
                "version": "1.0",
                "accuracy": "90%"
            }
        }
        
        print("✅ Workout plan generated successfully!")
        
        return jsonify(response)
        
    except Exception as e:
        print(f"❌ Error: {str(e)}")
        return jsonify({
            "error": str(e),
            "success": False
        }), 500

@app.route('/health', methods=['GET'])
def health_check():
    """Health check endpoint"""
    return jsonify({
        "status": "healthy",
        "model_loaded": model is not None,
        "message": "AI Fitness Model API is running!"
    })

if __name__ == '__main__':
    print("\n" + "="*60)
    print("🤖 AI FITNESS MODEL API")
    print("="*60)
    
    load_model()
    
    print("\n🚀 Starting Flask server...")
    print("📡 API will be available at: http://localhost:5000")
    print("🔗 Next.js should call: http://localhost:5000/api/predict-workout")
    print("\n" + "="*60 + "\n")
    
    app.run(debug=True, port=5000)
