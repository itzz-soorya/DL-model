"""
Generate and Save Training Datasets as CSV Files
Creates comprehensive datasets for both CNN and RNN models
"""
import numpy as np
import pandas as pd
from datetime import datetime
import json

print("="*80)
print("GENERATING COMPREHENSIVE DATASETS FOR CNN AND RNN MODELS")
print("="*80)

np.random.seed(42)

# ============================================================================
# GENERATE CNN DATASET
# ============================================================================
print("\n[1/4] Generating CNN Training Dataset...")

# Define categories
fitness_levels = ['Beginner', 'Intermediate', 'Advanced']
goals = ['Weight Loss', 'Muscle Gain', 'General Fitness']

cnn_data = []

# Generate samples
for _ in range(5000):  # Generate 5000 samples
    # Random user profile
    age = np.random.randint(18, 65)
    weight = np.random.uniform(45, 120)  # kg
    height = np.random.uniform(150, 200)  # cm
    fitness_level = np.random.randint(0, 3)
    goal = np.random.randint(0, 3)
    
    # Calculate BMI
    bmi = weight / ((height/100) ** 2)
    
    # Determine category (0-8)
    category = fitness_level * 3 + goal
    
    # Category label
    category_label = f"{fitness_levels[fitness_level]} - {goals[goal]}"
    
    cnn_data.append({
        'age': age,
        'weight': round(weight, 2),
        'height': round(height, 2),
        'bmi': round(bmi, 2),
        'fitness_level': fitness_level,
        'fitness_level_name': fitness_levels[fitness_level],
        'goal': goal,
        'goal_name': goals[goal],
        'category': category,
        'category_label': category_label
    })

cnn_df = pd.DataFrame(cnn_data)
cnn_df.to_csv('cnn_training_dataset.csv', index=False)
print(f"✓ Saved: cnn_training_dataset.csv ({len(cnn_df)} samples)")

# Save summary
cnn_summary = {
    'dataset_name': 'CNN Fitness Classification Dataset',
    'total_samples': len(cnn_df),
    'features': ['age', 'weight', 'height', 'bmi', 'fitness_level', 'goal'],
    'target': 'category (0-8)',
    'classes': 9,
    'class_distribution': cnn_df['category_label'].value_counts().to_dict()
}

print(f"\nCNN Dataset Summary:")
print(f"  • Total Samples: {cnn_summary['total_samples']}")
print(f"  • Features: {len(cnn_summary['features'])}")
print(f"  • Output Classes: {cnn_summary['classes']}")

# ============================================================================
# GENERATE RNN DATASET
# ============================================================================
print("\n[2/4] Generating RNN Training Dataset...")

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

def generate_workout_sequence(level, goal):
    """Generate a weekly workout sequence"""
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

rnn_data = []

# Generate samples
for _ in range(10000):  # Generate 10000 samples
    level = np.random.randint(0, 3)
    goal = np.random.randint(0, 3)
    age = np.random.randint(18, 65)
    
    # Generate base sequence
    sequence = generate_workout_sequence(level, goal)
    
    # Add some randomness (10% chance to modify each workout)
    for i in range(len(sequence)):
        if np.random.random() < 0.1:
            sequence[i] = np.random.randint(0, 7)
    
    # Create training sample (first 6 days predict 7th day)
    rnn_data.append({
        'age': age,
        'fitness_level': level,
        'fitness_level_name': fitness_levels[level],
        'goal': goal,
        'goal_name': goals[goal],
        'day1_workout': sequence[0],
        'day1_workout_name': workout_names[sequence[0]],
        'day2_workout': sequence[1],
        'day2_workout_name': workout_names[sequence[1]],
        'day3_workout': sequence[2],
        'day3_workout_name': workout_names[sequence[2]],
        'day4_workout': sequence[3],
        'day4_workout_name': workout_names[sequence[3]],
        'day5_workout': sequence[4],
        'day5_workout_name': workout_names[sequence[4]],
        'day6_workout': sequence[5],
        'day6_workout_name': workout_names[sequence[5]],
        'day7_workout': sequence[6],
        'day7_workout_name': workout_names[sequence[6]],
        'target_workout': sequence[6]
    })

rnn_df = pd.DataFrame(rnn_data)
rnn_df.to_csv('rnn_training_dataset.csv', index=False)
print(f"✓ Saved: rnn_training_dataset.csv ({len(rnn_df)} samples)")

# Save summary
rnn_summary = {
    'dataset_name': 'RNN Workout Sequence Prediction Dataset',
    'total_samples': len(rnn_df),
    'sequence_length': 6,
    'prediction_target': 'day 7 workout',
    'features': ['age', 'fitness_level', 'goal', 'past_6_days_workouts'],
    'target': 'next_workout (0-6)',
    'classes': 7,
    'class_distribution': rnn_df['day7_workout_name'].value_counts().to_dict()
}

print(f"\nRNN Dataset Summary:")
print(f"  • Total Samples: {rnn_summary['total_samples']}")
print(f"  • Sequence Length: {rnn_summary['sequence_length']} days")
print(f"  • Output Classes: {rnn_summary['classes']}")

# ============================================================================
# CREATE SAMPLE DATASETS (First 100 rows for documentation)
# ============================================================================
print("\n[3/4] Creating sample datasets...")

cnn_df.head(100).to_csv('cnn_dataset_sample.csv', index=False)
print(f"✓ Saved: cnn_dataset_sample.csv (100 samples)")

rnn_df.head(100).to_csv('rnn_dataset_sample.csv', index=False)
print(f"✓ Saved: rnn_dataset_sample.csv (100 samples)")

# ============================================================================
# CREATE DATASET DOCUMENTATION
# ============================================================================
print("\n[4/4] Creating dataset documentation...")

documentation = {
    'project': 'Fitness Plan Generator - Deep Learning Models',
    'created_date': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
    'datasets': {
        'cnn_dataset': {
            'filename': 'cnn_training_dataset.csv',
            'description': 'User profile classification dataset for CNN model',
            'total_samples': len(cnn_df),
            'features': {
                'age': 'User age (18-65 years)',
                'weight': 'User weight in kg (45-120 kg)',
                'height': 'User height in cm (150-200 cm)',
                'bmi': 'Body Mass Index calculated from weight and height',
                'fitness_level': 'Encoded fitness level (0=Beginner, 1=Intermediate, 2=Advanced)',
                'fitness_level_name': 'Human-readable fitness level',
                'goal': 'Encoded fitness goal (0=Weight Loss, 1=Muscle Gain, 2=General Fitness)',
                'goal_name': 'Human-readable fitness goal',
                'category': 'Target classification (0-8)',
                'category_label': 'Human-readable category label'
            },
            'output_classes': 9,
            'class_labels': [
                'Beginner - Weight Loss',
                'Beginner - Muscle Gain',
                'Beginner - General Fitness',
                'Intermediate - Weight Loss',
                'Intermediate - Muscle Gain',
                'Intermediate - General Fitness',
                'Advanced - Weight Loss',
                'Advanced - Muscle Gain',
                'Advanced - General Fitness'
            ],
            'model': 'Convolutional Neural Network (CNN)',
            'purpose': 'Classify users into fitness categories based on their profile'
        },
        'rnn_dataset': {
            'filename': 'rnn_training_dataset.csv',
            'description': 'Sequential workout prediction dataset for RNN model',
            'total_samples': len(rnn_df),
            'features': {
                'age': 'User age (18-65 years)',
                'fitness_level': 'Encoded fitness level (0-2)',
                'fitness_level_name': 'Human-readable fitness level',
                'goal': 'Encoded fitness goal (0-2)',
                'goal_name': 'Human-readable fitness goal',
                'day1_workout to day6_workout': 'Encoded workout types for past 6 days (0-6)',
                'day1_workout_name to day6_workout_name': 'Human-readable workout names',
                'day7_workout': 'Target workout for day 7 (encoded)',
                'day7_workout_name': 'Target workout for day 7 (human-readable)',
                'target_workout': 'Same as day7_workout (for model training)'
            },
            'output_classes': 7,
            'class_labels': [
                'Rest',
                'Cardio',
                'Strength',
                'HIIT',
                'Yoga',
                'Swimming',
                'Cycling'
            ],
            'model': 'Recurrent Neural Network (LSTM-based RNN)',
            'purpose': 'Predict next day workout based on past 6 days and user profile'
        }
    },
    'data_generation_method': 'Synthetic data generated using rule-based patterns with 10% randomness',
    'usage': 'These datasets are used to train deep learning models for personalized fitness recommendations'
}

with open('dataset_documentation.json', 'w') as f:
    json.dump(documentation, f, indent=2)

print(f"✓ Saved: dataset_documentation.json")

# ============================================================================
# CREATE README FOR DATASETS
# ============================================================================
readme_content = f"""# Fitness Plan Generator - Training Datasets

## Overview
This directory contains the training datasets used for the Fitness Plan Generator deep learning models.

**Created:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

---

## 📊 Datasets

### 1. CNN Training Dataset
**File:** `cnn_training_dataset.csv`

- **Samples:** {len(cnn_df):,}
- **Purpose:** User profile classification
- **Model:** Convolutional Neural Network (CNN)
- **Output:** 9 fitness categories

#### Features:
| Column | Type | Description | Range |
|--------|------|-------------|-------|
| age | int | User age | 18-65 years |
| weight | float | User weight | 45-120 kg |
| height | float | User height | 150-200 cm |
| bmi | float | Body Mass Index | Calculated |
| fitness_level | int | Fitness level (encoded) | 0-2 |
| fitness_level_name | str | Fitness level (readable) | Beginner/Intermediate/Advanced |
| goal | int | Fitness goal (encoded) | 0-2 |
| goal_name | str | Fitness goal (readable) | Weight Loss/Muscle Gain/General Fitness |
| category | int | **Target variable** | 0-8 |
| category_label | str | Category description | Combined level + goal |

#### Output Classes (9 categories):
0. Beginner - Weight Loss
1. Beginner - Muscle Gain
2. Beginner - General Fitness
3. Intermediate - Weight Loss
4. Intermediate - Muscle Gain
5. Intermediate - General Fitness
6. Advanced - Weight Loss
7. Advanced - Muscle Gain
8. Advanced - General Fitness

---

### 2. RNN Training Dataset
**File:** `rnn_training_dataset.csv`

- **Samples:** {len(rnn_df):,}
- **Purpose:** Sequential workout prediction
- **Model:** LSTM Recurrent Neural Network (RNN)
- **Output:** 7 workout types

#### Features:
| Column | Type | Description | Range |
|--------|------|-------------|-------|
| age | int | User age | 18-65 years |
| fitness_level | int | Fitness level (encoded) | 0-2 |
| fitness_level_name | str | Fitness level (readable) | Beginner/Intermediate/Advanced |
| goal | int | Fitness goal (encoded) | 0-2 |
| goal_name | str | Fitness goal (readable) | Weight Loss/Muscle Gain/General Fitness |
| day1_workout | int | Day 1 workout (encoded) | 0-6 |
| day1_workout_name | str | Day 1 workout (readable) | Workout type name |
| day2_workout | int | Day 2 workout (encoded) | 0-6 |
| day2_workout_name | str | Day 2 workout (readable) | Workout type name |
| day3_workout | int | Day 3 workout (encoded) | 0-6 |
| day3_workout_name | str | Day 3 workout (readable) | Workout type name |
| day4_workout | int | Day 4 workout (encoded) | 0-6 |
| day4_workout_name | str | Day 4 workout (readable) | Workout type name |
| day5_workout | int | Day 5 workout (encoded) | 0-6 |
| day5_workout_name | str | Day 5 workout (readable) | Workout type name |
| day6_workout | int | Day 6 workout (encoded) | 0-6 |
| day6_workout_name | str | Day 6 workout (readable) | Workout type name |
| day7_workout | int | **Target variable** | 0-6 |
| day7_workout_name | str | Target workout (readable) | Workout type name |
| target_workout | int | Same as day7_workout | 0-6 |

#### Output Classes (7 workout types):
0. Rest
1. Cardio
2. Strength
3. HIIT (High-Intensity Interval Training)
4. Yoga
5. Swimming
6. Cycling

---

## 📁 Sample Datasets

For quick preview and documentation purposes:
- `cnn_dataset_sample.csv` - First 100 rows of CNN dataset
- `rnn_dataset_sample.csv` - First 100 rows of RNN dataset

---

## 🔧 Data Generation

### Method
Synthetic data generated using rule-based patterns that follow fitness principles:

1. **Base Patterns**: Created based on fitness level and goal combinations
2. **Randomization**: 10% random variation added to simulate real-world diversity
3. **Validation**: Patterns follow standard fitness training principles

### Why Synthetic Data?
- **Perfect Alignment**: Matches exact model requirements
- **Controlled Quality**: Clean, labeled data without missing values
- **Privacy**: No personal data collection needed
- **Reproducibility**: Consistent for research and demonstration
- **Scalability**: Easy to generate more samples as needed

---

## 📊 Statistics

### CNN Dataset Distribution
```
Total Samples: {len(cnn_df):,}
Features: 6 (age, weight, height, bmi, fitness_level, goal)
Target Classes: 9
```

### RNN Dataset Distribution
```
Total Samples: {len(rnn_df):,}
Sequence Length: 6 days input → 1 day prediction
Features: 3 user features + 6 workout sequences
Target Classes: 7
```

---

## 🚀 Usage

### Loading CNN Dataset (Python)
```python
import pandas as pd

# Load full dataset
cnn_df = pd.read_csv('cnn_training_dataset.csv')

# Features
X = cnn_df[['age', 'weight', 'height', 'fitness_level', 'goal']].values

# Target
y = cnn_df['category'].values
```

### Loading RNN Dataset (Python)
```python
import pandas as pd
import numpy as np

# Load full dataset
rnn_df = pd.read_csv('rnn_training_dataset.csv')

# Sequence features (past 6 days)
X_seq = rnn_df[['day1_workout', 'day2_workout', 'day3_workout', 
                'day4_workout', 'day5_workout', 'day6_workout']].values

# User features
X_feat = rnn_df[['age', 'fitness_level', 'goal']].values

# Target (day 7 workout)
y = rnn_df['target_workout'].values
```

---

## 📝 Citation

If you use these datasets in your research or project, please cite:

```
Fitness Plan Generator Dataset
Generated: {datetime.now().strftime('%Y-%m-%d')}
Purpose: Deep Learning Models for Personalized Fitness Recommendations
Models: CNN (9-class classification) and RNN (7-class sequence prediction)
```

---

## 📄 Additional Files

- `dataset_documentation.json` - Complete technical documentation in JSON format
- `cnn_dataset_sample.csv` - Sample preview of CNN data
- `rnn_dataset_sample.csv` - Sample preview of RNN data

---

## ⚠️ Notes

- All data is synthetically generated for training purposes
- Patterns are based on standard fitness training principles
- BMI values are automatically calculated from weight and height
- Workout sequences follow progression patterns suitable for each fitness level
- Random variations ensure model generalization

---

## 📧 Contact

For questions about the datasets or models, refer to the main project documentation.
"""

with open('DATASET_README.md', 'w', encoding='utf-8') as f:
    f.write(readme_content)

print(f"✓ Saved: DATASET_README.md")

# ============================================================================
# STATISTICS SUMMARY
# ============================================================================
print("\n" + "="*80)
print("DATASET GENERATION COMPLETE!")
print("="*80)
print(f"\n📊 Generated Files:")
print(f"   1. cnn_training_dataset.csv      - {len(cnn_df):,} samples")
print(f"   2. rnn_training_dataset.csv      - {len(rnn_df):,} samples")
print(f"   3. cnn_dataset_sample.csv        - 100 sample rows")
print(f"   4. rnn_dataset_sample.csv        - 100 sample rows")
print(f"   5. dataset_documentation.json    - Technical documentation")
print(f"   6. DATASET_README.md             - Complete dataset guide")

print(f"\n📈 Dataset Statistics:")
print(f"\n   CNN Dataset:")
print(f"   • Total Samples: {len(cnn_df):,}")
print(f"   • Features: 6 (age, weight, height, bmi, fitness_level, goal)")
print(f"   • Target: category (9 classes)")
print(f"   • File Size: {cnn_df.memory_usage(deep=True).sum() / 1024:.2f} KB")

print(f"\n   RNN Dataset:")
print(f"   • Total Samples: {len(rnn_df):,}")
print(f"   • Sequence Length: 6 days → predict day 7")
print(f"   • Features: 3 user + 6 workout sequence")
print(f"   • Target: next_workout (7 classes)")
print(f"   • File Size: {rnn_df.memory_usage(deep=True).sum() / 1024:.2f} KB")

print(f"\n✅ All datasets saved successfully!")
print("="*80 + "\n")
