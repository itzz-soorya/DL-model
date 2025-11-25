# Fitness Plan Generator - Training Datasets

## Overview
This directory contains the training datasets used for the Fitness Plan Generator deep learning models.

**Created:** 2025-11-25 21:18:02

---

## 📊 Datasets

### 1. CNN Training Dataset
**File:** `cnn_training_dataset.csv`

- **Samples:** 5,000
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

- **Samples:** 10,000
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
Total Samples: 5,000
Features: 6 (age, weight, height, bmi, fitness_level, goal)
Target Classes: 9
```

### RNN Dataset Distribution
```
Total Samples: 10,000
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
Generated: 2025-11-25
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
