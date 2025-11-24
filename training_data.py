"""
Training Data and Exercise Database
Contains all workout exercises and diet plan templates
"""

# Workout type names (expanded from 7 to 12 types)
workout_names = [
    'Rest', 'Cardio', 'Strength', 'HIIT', 'Yoga', 'Swimming', 
    'Cycling', 'Pilates', 'CrossFit', 'Boxing', 'Dancing', 'Sports'
]

# Exercise database by workout type and fitness level
exercises_db = {
    0: {  # Rest
        "day": "Rest Day",
        "routines": [
            {"name": "Light Stretching", "sets": 1, "reps": 15},
            {"name": "Walking", "sets": 1, "reps": 20},
        ]
    },
    1: {  # Cardio
        "beginner": [
            {"name": "Brisk Walking", "sets": 1, "reps": 30},
            {"name": "Jumping Jacks", "sets": 3, "reps": 20},
            {"name": "High Knees", "sets": 3, "reps": 30},
            {"name": "Cycling", "sets": 1, "reps": 20},
        ],
        "intermediate": [
            {"name": "Running", "sets": 1, "reps": 30},
            {"name": "Jump Rope", "sets": 5, "reps": 60},
            {"name": "Mountain Climbers", "sets": 4, "reps": 30},
            {"name": "Burpees", "sets": 4, "reps": 15},
        ],
        "advanced": [
            {"name": "Sprint Intervals", "sets": 8, "reps": 30},
            {"name": "Box Jumps", "sets": 5, "reps": 20},
            {"name": "Battle Ropes", "sets": 6, "reps": 45},
            {"name": "Rowing Machine", "sets": 5, "reps": 10},
        ]
    },
    2: {  # Strength
        "beginner": [
            {"name": "Bodyweight Squats", "sets": 3, "reps": 15},
            {"name": "Push-ups", "sets": 3, "reps": 10},
            {"name": "Dumbbell Rows", "sets": 3, "reps": 12},
            {"name": "Plank", "sets": 3, "reps": 30},
        ],
        "intermediate": [
            {"name": "Barbell Squats", "sets": 4, "reps": 10},
            {"name": "Bench Press", "sets": 4, "reps": 10},
            {"name": "Deadlifts", "sets": 3, "reps": 8},
            {"name": "Pull-ups", "sets": 3, "reps": 12},
        ],
        "advanced": [
            {"name": "Heavy Squats", "sets": 5, "reps": 5},
            {"name": "Weighted Bench Press", "sets": 5, "reps": 6},
            {"name": "Deadlifts (heavy)", "sets": 5, "reps": 5},
            {"name": "Weighted Pull-ups", "sets": 4, "reps": 8},
        ]
    },
    3: {  # HIIT
        "beginner": [
            {"name": "Burpees", "sets": 3, "reps": 8},
            {"name": "Jump Squats", "sets": 3, "reps": 12},
            {"name": "High Knees", "sets": 3, "reps": 30},
            {"name": "Plank Jacks", "sets": 3, "reps": 15},
        ],
        "intermediate": [
            {"name": "Burpee Box Jumps", "sets": 4, "reps": 12},
            {"name": "Kettlebell Swings", "sets": 4, "reps": 20},
            {"name": "Thrusters", "sets": 4, "reps": 15},
            {"name": "Battle Ropes", "sets": 4, "reps": 45},
        ],
        "advanced": [
            {"name": "Clean and Jerk", "sets": 5, "reps": 8},
            {"name": "Prowler Push", "sets": 6, "reps": 30},
            {"name": "Box Jump Overs", "sets": 5, "reps": 15},
            {"name": "Assault Bike Sprints", "sets": 8, "reps": 30},
        ]
    },
    4: {  # Yoga
        "beginner": [
            {"name": "Sun Salutations", "sets": 3, "reps": 5},
            {"name": "Downward Dog", "sets": 3, "reps": 30},
            {"name": "Warrior Pose", "sets": 3, "reps": 30},
            {"name": "Child's Pose", "sets": 3, "reps": 60},
        ],
        "intermediate": [
            {"name": "Vinyasa Flow", "sets": 1, "reps": 45},
            {"name": "Tree Pose", "sets": 3, "reps": 60},
            {"name": "Crow Pose", "sets": 3, "reps": 30},
            {"name": "Headstand", "sets": 3, "reps": 30},
        ],
        "advanced": [
            {"name": "Ashtanga Yoga", "sets": 1, "reps": 60},
            {"name": "Handstand", "sets": 3, "reps": 60},
            {"name": "Scorpion Pose", "sets": 3, "reps": 30},
            {"name": "Advanced Flow", "sets": 1, "reps": 45},
        ]
    },
    5: {  # Swimming
        "beginner": [
            {"name": "Freestyle (easy)", "sets": 4, "reps": 10},
            {"name": "Backstroke", "sets": 3, "reps": 5},
            {"name": "Water Jogging", "sets": 1, "reps": 15},
        ],
        "intermediate": [
            {"name": "Freestyle Laps", "sets": 6, "reps": 10},
            {"name": "Butterfly", "sets": 4, "reps": 5},
            {"name": "Interval Training", "sets": 8, "reps": 2},
        ],
        "advanced": [
            {"name": "Sprint Laps", "sets": 10, "reps": 5},
            {"name": "Butterfly (fast)", "sets": 6, "reps": 5},
            {"name": "Underwater Training", "sets": 5, "reps": 3},
        ]
    },
    6: {  # Cycling
        "beginner": [
            {"name": "Flat Road Cycling", "sets": 1, "reps": 30},
            {"name": "Easy Hills", "sets": 3, "reps": 10},
            {"name": "Stationary Bike", "sets": 1, "reps": 25},
            {"name": "Leisure Ride", "sets": 1, "reps": 40},
        ],
        "intermediate": [
            {"name": "Hill Intervals", "sets": 6, "reps": 5},
            {"name": "Tempo Ride", "sets": 1, "reps": 45},
            {"name": "Spin Class", "sets": 1, "reps": 50},
            {"name": "Road Cycling", "sets": 1, "reps": 60},
        ],
        "advanced": [
            {"name": "Sprint Intervals", "sets": 10, "reps": 3},
            {"name": "Mountain Climbing", "sets": 1, "reps": 60},
            {"name": "Criterium Training", "sets": 8, "reps": 5},
            {"name": "Time Trial", "sets": 1, "reps": 90},
        ]
    },
    7: {  # Pilates
        "beginner": [
            {"name": "The Hundred", "sets": 3, "reps": 10},
            {"name": "Rolling Like a Ball", "sets": 3, "reps": 12},
            {"name": "Single Leg Circles", "sets": 3, "reps": 10},
            {"name": "Spine Stretch", "sets": 3, "reps": 8},
            {"name": "Pelvic Curl", "sets": 3, "reps": 15},
        ],
        "intermediate": [
            {"name": "Criss-Cross", "sets": 4, "reps": 20},
            {"name": "Swan Dive", "sets": 4, "reps": 12},
            {"name": "Teaser", "sets": 3, "reps": 10},
            {"name": "Side Kick Series", "sets": 4, "reps": 15},
            {"name": "Shoulder Bridge", "sets": 3, "reps": 12},
        ],
        "advanced": [
            {"name": "Advanced Teaser", "sets": 5, "reps": 8},
            {"name": "Control Balance", "sets": 4, "reps": 10},
            {"name": "Jackknife", "sets": 4, "reps": 12},
            {"name": "Boomerang", "sets": 3, "reps": 8},
            {"name": "Reformer Series", "sets": 1, "reps": 45},
        ]
    },
    8: {  # CrossFit
        "beginner": [
            {"name": "Air Squats", "sets": 4, "reps": 15},
            {"name": "Push-ups", "sets": 4, "reps": 10},
            {"name": "Sit-ups", "sets": 4, "reps": 20},
            {"name": "Lunges", "sets": 3, "reps": 12},
            {"name": "Ring Rows", "sets": 3, "reps": 10},
        ],
        "intermediate": [
            {"name": "Wall Balls", "sets": 5, "reps": 20},
            {"name": "Box Jumps", "sets": 4, "reps": 15},
            {"name": "Kettlebell Swings", "sets": 5, "reps": 25},
            {"name": "Pull-ups", "sets": 4, "reps": 12},
            {"name": "Double Unders", "sets": 5, "reps": 50},
        ],
        "advanced": [
            {"name": "Muscle-ups", "sets": 5, "reps": 8},
            {"name": "Snatch", "sets": 5, "reps": 5},
            {"name": "Clean and Jerk", "sets": 5, "reps": 5},
            {"name": "Handstand Push-ups", "sets": 4, "reps": 10},
            {"name": "WOD Fran", "sets": 1, "reps": 1},
        ]
    },
    9: {  # Boxing
        "beginner": [
            {"name": "Jab-Cross Combo", "sets": 5, "reps": 20},
            {"name": "Shadow Boxing", "sets": 3, "reps": 3},
            {"name": "Heavy Bag Work", "sets": 4, "reps": 2},
            {"name": "Jump Rope", "sets": 3, "reps": 3},
            {"name": "Footwork Drills", "sets": 4, "reps": 5},
        ],
        "intermediate": [
            {"name": "Combination Punches", "sets": 6, "reps": 3},
            {"name": "Speed Bag", "sets": 5, "reps": 3},
            {"name": "Mitt Work", "sets": 5, "reps": 3},
            {"name": "Sparring", "sets": 4, "reps": 3},
            {"name": "Core Conditioning", "sets": 4, "reps": 20},
        ],
        "advanced": [
            {"name": "Advanced Combos", "sets": 8, "reps": 3},
            {"name": "Power Bag Work", "sets": 6, "reps": 3},
            {"name": "Competitive Sparring", "sets": 6, "reps": 3},
            {"name": "Plyometric Drills", "sets": 5, "reps": 15},
            {"name": "High-Intensity Rounds", "sets": 10, "reps": 3},
        ]
    },
    10: {  # Dancing
        "beginner": [
            {"name": "Basic Zumba", "sets": 1, "reps": 30},
            {"name": "Hip Hop Basics", "sets": 3, "reps": 10},
            {"name": "Salsa Steps", "sets": 4, "reps": 15},
            {"name": "Stretching Routine", "sets": 2, "reps": 10},
        ],
        "intermediate": [
            {"name": "Cardio Dance", "sets": 1, "reps": 45},
            {"name": "Ballet Barre", "sets": 4, "reps": 20},
            {"name": "Jazz Dance", "sets": 3, "reps": 15},
            {"name": "Contemporary Flow", "sets": 1, "reps": 30},
        ],
        "advanced": [
            {"name": "Advanced Choreography", "sets": 1, "reps": 60},
            {"name": "Power Dance", "sets": 5, "reps": 10},
            {"name": "Dance HIIT Fusion", "sets": 6, "reps": 5},
            {"name": "Performance Training", "sets": 1, "reps": 90},
        ]
    },
    11: {  # Sports
        "beginner": [
            {"name": "Basketball Shooting", "sets": 5, "reps": 10},
            {"name": "Soccer Dribbling", "sets": 4, "reps": 15},
            {"name": "Tennis Rally", "sets": 3, "reps": 20},
            {"name": "Volleyball Practice", "sets": 4, "reps": 15},
        ],
        "intermediate": [
            {"name": "Basketball Scrimmage", "sets": 4, "reps": 10},
            {"name": "Soccer Match Play", "sets": 2, "reps": 30},
            {"name": "Tennis Match", "sets": 3, "reps": 15},
            {"name": "Badminton Games", "sets": 5, "reps": 10},
        ],
        "advanced": [
            {"name": "Competitive Basketball", "sets": 1, "reps": 60},
            {"name": "Soccer Tournament", "sets": 1, "reps": 90},
            {"name": "Tennis Competition", "sets": 5, "reps": 12},
            {"name": "Multi-Sport Training", "sets": 1, "reps": 120},
        ]
    }
}

# Initial workout sequences based on fitness level and goal
workout_patterns = {
    # Beginner patterns
    (0, 0): [1, 0],  # Beginner, Weight loss: Cardio, Rest
    (0, 1): [2, 0],  # Beginner, Muscle gain: Strength, Rest
    (0, 2): [1, 2],  # Beginner, Fitness: Cardio, Strength
    
    # Intermediate patterns
    (1, 0): [3, 1],  # Intermediate, Weight loss: HIIT, Cardio
    (1, 1): [2, 2],  # Intermediate, Muscle gain: Strength, Strength
    (1, 2): [2, 3],  # Intermediate, Fitness: Strength, HIIT
    
    # Advanced patterns
    (2, 0): [3, 3],  # Advanced, Weight loss: HIIT, HIIT
    (2, 1): [2, 2],  # Advanced, Muscle gain: Strength, Strength
    (2, 2): [3, 2],  # Advanced, Fitness: HIIT, Strength
}

# Meal templates for diet plan generation (expanded with more variety)
meal_options = {
    "breakfast": [
        ["Oatmeal with berries", "Scrambled eggs", "Whole wheat toast", "Orange juice"],
        ["Greek yogurt with granola", "Banana", "Almonds", "Green tea"],
        ["Protein smoothie", "Whole grain cereal", "Milk", "Apple"],
        ["Egg white omelette", "Avocado toast", "Fresh fruit", "Coffee"],
        ["Quinoa porridge", "Boiled eggs", "Mixed berries", "Herbal tea"],
        ["Protein pancakes", "Turkey bacon", "Strawberries", "Black coffee"],
        ["Overnight oats", "Peanut butter", "Sliced banana", "Almond milk"],
        ["Veggie omelette", "Whole grain bagel", "Grapefruit", "Green smoothie"],
        ["Chia pudding", "Walnuts", "Blueberries", "Coconut water"],
        ["Cottage cheese bowl", "Honey", "Peaches", "Matcha latte"],
    ],
    "lunch": [
        ["Grilled chicken breast", "Brown rice", "Steamed broccoli", "Olive oil"],
        ["Salmon fillet", "Quinoa", "Mixed vegetables", "Lemon water"],
        ["Turkey wrap", "Sweet potato", "Side salad", "Green tea"],
        ["Lean beef stir-fry", "Brown rice", "Bell peppers", "Ginger tea"],
        ["Tuna salad", "Whole wheat pita", "Cucumber", "Tomato juice"],
        ["Chicken Caesar salad", "Chickpeas", "Cherry tomatoes", "Sparkling water"],
        ["Grilled fish tacos", "Black beans", "Corn salsa", "Lime water"],
        ["Lean pork tenderloin", "Roasted vegetables", "Couscous", "Iced tea"],
        ["Shrimp bowl", "Cauliflower rice", "Edamame", "Miso soup"],
        ["Turkey burger", "Sweet potato fries", "Coleslaw", "Protein shake"],
    ],
    "dinner": [
        ["Baked cod", "Asparagus", "Wild rice", "Sparkling water"],
        ["Grilled chicken", "Roasted vegetables", "Quinoa", "Herbal tea"],
        ["Lean steak", "Green beans", "Mashed sweet potato", "Water"],
        ["Shrimp stir-fry", "Brown rice", "Mixed veggies", "Lemon water"],
        ["Baked salmon", "Brussels sprouts", "Farro", "Cucumber water"],
        ["Chicken breast", "Zucchini noodles", "Marinara sauce", "Green tea"],
        ["Turkey meatballs", "Spaghetti squash", "Side salad", "Herbal infusion"],
        ["Grilled tilapia", "Quinoa salad", "Roasted cauliflower", "Mint tea"],
        ["Beef and broccoli", "Jasmine rice", "Bok choy", "White tea"],
        ["Chicken fajitas", "Bell peppers", "Whole wheat tortilla", "Agua fresca"],
    ],
    "snacks": [
        ["Apple with almond butter", "Protein bar"],
        ["Mixed nuts", "Greek yogurt"],
        ["Cottage cheese", "Berries"],
        ["Protein shake", "Banana"],
        ["Hummus", "Carrot sticks"],
        ["Rice cakes", "Peanut butter"],
        ["Trail mix", "String cheese"],
        ["Hard-boiled eggs", "Cherry tomatoes"],
        ["Edamame", "Seaweed snacks"],
        ["Protein smoothie", "Granola"],
        ["Celery sticks", "Almond butter"],
        ["Turkey roll-ups", "Bell pepper slices"],
    ]
}

# Activity multipliers for BMR calculation
activity_multipliers = {
    0: 1.3,    # Beginner (light activity)
    1: 1.55,   # Intermediate (moderate activity)
    2: 1.725   # Advanced (very active)
}

# Level names mapping
level_names = ['beginner', 'intermediate', 'advanced']

# Goal names mapping
goal_names = ['weight loss', 'build muscle', 'improve fitness']

# Days of the week
days_of_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

# Additional nutritional data for comprehensive diet planning
nutrition_targets = {
    "weight_loss": {
        "protein_ratio": 0.30,  # 30% of calories from protein
        "carb_ratio": 0.40,     # 40% from carbs
        "fat_ratio": 0.30,      # 30% from fats
        "calorie_deficit": -500  # 500 calorie deficit
    },
    "muscle_gain": {
        "protein_ratio": 0.35,  # 35% from protein
        "carb_ratio": 0.45,     # 45% from carbs
        "fat_ratio": 0.20,      # 20% from fats
        "calorie_surplus": 300  # 300 calorie surplus
    },
    "maintenance": {
        "protein_ratio": 0.25,  # 25% from protein
        "carb_ratio": 0.50,     # 50% from carbs
        "fat_ratio": 0.25,      # 25% from fats
        "calorie_adjustment": 0  # No adjustment
    }
}

# Hydration recommendations (in liters per day)
hydration_targets = {
    0: 2.0,    # Beginner
    1: 2.5,    # Intermediate
    2: 3.5,    # Advanced
    3: 4.0     # Elite athlete
}

# Workout duration targets (in minutes)
workout_durations = {
    "beginner": {
        "cardio": 30,
        "strength": 40,
        "hiit": 20,
        "yoga": 45,
        "swimming": 30,
        "cycling": 35,
        "pilates": 40,
        "crossfit": 30,
        "boxing": 30,
        "dancing": 35,
        "sports": 45
    },
    "intermediate": {
        "cardio": 45,
        "strength": 60,
        "hiit": 30,
        "yoga": 60,
        "swimming": 45,
        "cycling": 50,
        "pilates": 50,
        "crossfit": 45,
        "boxing": 45,
        "dancing": 50,
        "sports": 60
    },
    "advanced": {
        "cardio": 60,
        "strength": 90,
        "hiit": 45,
        "yoga": 75,
        "swimming": 60,
        "cycling": 75,
        "pilates": 60,
        "crossfit": 60,
        "boxing": 60,
        "dancing": 60,
        "sports": 90
    }
}

# Recovery recommendations
recovery_activities = {
    "light": ["Walking", "Gentle stretching", "Foam rolling", "Light yoga"],
    "moderate": ["Swimming (easy)", "Cycling (easy)", "Pilates", "Massage"],
    "active": ["Yoga", "Light jogging", "Dynamic stretching", "Mobility work"]
}

# Supplement recommendations (basic fitness supplements)
supplements_db = {
    "weight_loss": ["Protein powder", "Green tea extract", "BCAAs", "Multivitamin"],
    "muscle_gain": ["Whey protein", "Creatine", "BCAAs", "Pre-workout", "Multivitamin"],
    "endurance": ["Electrolytes", "Beta-alanine", "Protein powder", "Omega-3", "Multivitamin"],
    "general_health": ["Multivitamin", "Vitamin D", "Omega-3", "Magnesium"]
}

# Equipment needed for different workouts
equipment_requirements = {
    "bodyweight": ["Yoga mat", "None"],
    "beginner": ["Dumbbells (5-15 lbs)", "Resistance bands", "Yoga mat"],
    "intermediate": ["Dumbbells (15-30 lbs)", "Barbell", "Bench", "Pull-up bar", "Yoga mat"],
    "advanced": ["Full gym access", "Olympic barbell", "Power rack", "Cable machine", "Specialized equipment"],
    "home_gym": ["Adjustable dumbbells", "Resistance bands", "Pull-up bar", "Yoga mat", "Jump rope"]
}

# Training intensity zones (percentage of max heart rate)
intensity_zones = {
    "recovery": {"min_hr": 50, "max_hr": 60, "description": "Very light activity, active recovery"},
    "aerobic": {"min_hr": 60, "max_hr": 70, "description": "Fat burning, base building"},
    "tempo": {"min_hr": 70, "max_hr": 80, "description": "Moderate intensity, endurance"},
    "threshold": {"min_hr": 80, "max_hr": 90, "description": "High intensity, performance improvement"},
    "vo2max": {"min_hr": 90, "max_hr": 100, "description": "Maximum effort, peak performance"}
}

# Warm-up routines
warmup_routines = {
    "dynamic": [
        {"name": "Arm Circles", "duration": 30},
        {"name": "Leg Swings", "duration": 30},
        {"name": "Hip Circles", "duration": 30},
        {"name": "Torso Twists", "duration": 30},
        {"name": "Light Jogging", "duration": 120}
    ],
    "strength": [
        {"name": "Jump Rope", "duration": 180},
        {"name": "Dynamic Stretching", "duration": 120},
        {"name": "Mobility Drills", "duration": 120},
        {"name": "Light Cardio", "duration": 180}
    ],
    "yoga": [
        {"name": "Cat-Cow Stretches", "duration": 60},
        {"name": "Gentle Sun Salutations", "duration": 180},
        {"name": "Breathing Exercises", "duration": 120}
    ]
}

# Cool-down routines
cooldown_routines = {
    "static_stretching": [
        {"name": "Hamstring Stretch", "duration": 45},
        {"name": "Quad Stretch", "duration": 45},
        {"name": "Shoulder Stretch", "duration": 30},
        {"name": "Calf Stretch", "duration": 30},
        {"name": "Hip Flexor Stretch", "duration": 45}
    ],
    "foam_rolling": [
        {"name": "IT Band Roll", "duration": 60},
        {"name": "Quad Roll", "duration": 60},
        {"name": "Back Roll", "duration": 60},
        {"name": "Calf Roll", "duration": 45}
    ],
    "yoga": [
        {"name": "Child's Pose", "duration": 90},
        {"name": "Pigeon Pose", "duration": 60},
        {"name": "Savasana", "duration": 180}
    ]
}

# Fitness assessment metrics
fitness_metrics = {
    "beginner_benchmarks": {
        "pushups": 10,
        "situps": 20,
        "plank_seconds": 30,
        "mile_time_minutes": 12,
        "bodyweight_squat": 15
    },
    "intermediate_benchmarks": {
        "pushups": 25,
        "situps": 40,
        "plank_seconds": 60,
        "mile_time_minutes": 9,
        "bodyweight_squat": 30
    },
    "advanced_benchmarks": {
        "pushups": 50,
        "situps": 60,
        "plank_seconds": 120,
        "mile_time_minutes": 7,
        "bodyweight_squat": 50
    }
}

# Weekly workout split templates
workout_splits = {
    "beginner_full_body": {
        "frequency": 3,
        "schedule": ["Full Body A", "Rest", "Full Body B", "Rest", "Full Body C", "Rest", "Rest"]
    },
    "intermediate_upper_lower": {
        "frequency": 4,
        "schedule": ["Upper Body", "Lower Body", "Rest", "Upper Body", "Lower Body", "Rest", "Rest"]
    },
    "advanced_push_pull_legs": {
        "frequency": 6,
        "schedule": ["Push", "Pull", "Legs", "Push", "Pull", "Legs", "Rest"]
    },
    "athlete_split": {
        "frequency": 5,
        "schedule": ["Strength", "Cardio", "HIIT", "Sport-Specific", "Recovery", "Competition/Test", "Rest"]
    }
}

# Body composition targets by goal
body_composition_targets = {
    "weight_loss": {
        "weekly_loss_lbs": 1.5,
        "body_fat_reduction_percent": 1.0,
        "muscle_retention_priority": "high"
    },
    "muscle_gain": {
        "weekly_gain_lbs": 0.5,
        "body_fat_gain_percent": 0.3,
        "lean_mass_priority": "maximum"
    },
    "recomposition": {
        "weekly_change_lbs": 0.0,
        "body_fat_reduction_percent": 0.5,
        "muscle_gain_priority": "moderate"
    },
    "cutting": {
        "weekly_loss_lbs": 1.0,
        "body_fat_reduction_percent": 0.8,
        "muscle_retention_priority": "maximum"
    },
    "bulking": {
        "weekly_gain_lbs": 1.0,
        "body_fat_gain_percent": 0.5,
        "lean_mass_priority": "high"
    }
}

# Progressive overload strategies
progressive_overload_methods = {
    "increase_weight": {
        "increment": "5-10 lbs for compound lifts, 2.5-5 lbs for isolation",
        "frequency": "weekly or bi-weekly",
        "best_for": "strength and muscle gain"
    },
    "increase_reps": {
        "increment": "1-2 reps per set",
        "frequency": "each workout",
        "best_for": "muscular endurance and hypertrophy"
    },
    "increase_sets": {
        "increment": "1 set per exercise",
        "frequency": "every 2-3 weeks",
        "best_for": "volume accumulation"
    },
    "decrease_rest": {
        "increment": "15-30 seconds reduction",
        "frequency": "weekly",
        "best_for": "metabolic conditioning"
    },
    "increase_frequency": {
        "increment": "1 additional session per week",
        "frequency": "monthly",
        "best_for": "advanced trainees"
    },
    "improve_form": {
        "increment": "tempo manipulation, ROM increase",
        "frequency": "continuous",
        "best_for": "all levels, injury prevention"
    }
}

# Common fitness mistakes and corrections
fitness_mistakes = {
    "overtraining": {
        "symptoms": ["Persistent fatigue", "Decreased performance", "Sleep issues", "Mood changes"],
        "solution": "Increase rest days, reduce volume by 30-40%, focus on recovery",
        "prevention": "Follow periodization, listen to body signals"
    },
    "undertraining": {
        "symptoms": ["No progress", "Easy workouts", "No muscle soreness"],
        "solution": "Increase intensity, add progressive overload, track workouts",
        "prevention": "Set measurable goals, use training logs"
    },
    "poor_nutrition": {
        "symptoms": ["No muscle gain", "Constant hunger", "Low energy"],
        "solution": "Calculate TDEE, track macros, meal prep",
        "prevention": "Plan nutrition like training, use food scale"
    },
    "inconsistency": {
        "symptoms": ["Irregular training", "Yo-yo dieting", "No routine"],
        "solution": "Schedule workouts, find accountability partner, set specific times",
        "prevention": "Build habits, start small, be realistic"
    }
}

# Rest and recovery protocols
recovery_protocols = {
    "sleep_optimization": {
        "recommended_hours": {"beginner": 7, "intermediate": 8, "advanced": 8.5, "athlete": 9},
        "quality_tips": ["Dark room", "Cool temperature (65-68°F)", "No screens 1hr before", "Consistent schedule"],
        "importance": "critical for muscle growth and performance"
    },
    "active_recovery": {
        "activities": ["Light swimming", "Easy cycling", "Yoga", "Walking", "Foam rolling"],
        "duration": "20-30 minutes",
        "frequency": "1-2 times per week",
        "benefits": "Increased blood flow, reduced soreness, mental refresh"
    },
    "nutrition_timing": {
        "pre_workout": {"timing": "30-60 min before", "foods": ["Banana", "Oatmeal", "Rice cakes"]},
        "post_workout": {"timing": "within 30-60 min", "foods": ["Protein shake", "Chicken and rice", "Greek yogurt"]},
        "importance": "Optimizes performance and recovery"
    },
    "stress_management": {
        "techniques": ["Meditation", "Deep breathing", "Journaling", "Nature walks", "Massage"],
        "frequency": "daily practice recommended",
        "impact": "Reduces cortisol, improves recovery, enhances performance"
    }
}

# Training periodization models
periodization_models = {
    "linear": {
        "description": "Gradual increase in intensity, decrease in volume",
        "phases": ["Hypertrophy (8-12 reps)", "Strength (4-6 reps)", "Power (1-3 reps)", "Deload"],
        "duration": "12-16 weeks per cycle",
        "best_for": "Beginners to intermediate"
    },
    "undulating": {
        "description": "Varies intensity and volume within the week",
        "phases": ["Heavy day", "Light day", "Medium day"],
        "duration": "Weekly micro-cycles",
        "best_for": "Intermediate to advanced"
    },
    "block": {
        "description": "Focus on one attribute per block",
        "phases": ["Accumulation", "Intensification", "Realization", "Deload"],
        "duration": "4-6 weeks per block",
        "best_for": "Advanced athletes"
    },
    "conjugate": {
        "description": "Train all qualities simultaneously",
        "phases": ["Max effort day", "Dynamic effort day", "Repetition day"],
        "duration": "Continuous rotation",
        "best_for": "Powerlifters and athletes"
    }
}

# Injury prevention strategies
injury_prevention = {
    "proper_warmup": {
        "components": ["General warmup (5-10 min cardio)", "Dynamic stretching", "Movement prep", "Activation exercises"],
        "time": "10-15 minutes",
        "importance": "Reduces injury risk by 50%+"
    },
    "mobility_work": {
        "exercises": ["Hip flexor stretches", "Thoracic spine mobility", "Ankle mobility", "Shoulder mobility"],
        "frequency": "Daily, especially before workouts",
        "benefits": "Improved ROM, better movement patterns"
    },
    "proper_form": {
        "tips": ["Start with lighter weights", "Use mirrors or record yourself", "Hire a coach initially", "Focus on eccentric control"],
        "common_issues": "Ego lifting, momentum usage, poor posture",
        "solution": "Quality over quantity, master basics first"
    },
    "load_management": {
        "principles": ["10% rule (increase volume by max 10% per week)", "Deload every 4-6 weeks", "Listen to pain signals"],
        "monitoring": "Track volume, intensity, recovery status",
        "red_flags": ["Sharp pain", "Chronic soreness", "Joint pain", "Movement limitations"]
    }
}

# Cardio training zones and benefits
cardio_training_zones = {
    "zone_1_recovery": {
        "intensity": "50-60% max HR",
        "duration": "30-60 minutes",
        "benefits": "Active recovery, base building",
        "examples": ["Easy walk", "Light cycling", "Gentle swim"],
        "frequency": "Daily if desired"
    },
    "zone_2_aerobic": {
        "intensity": "60-70% max HR",
        "duration": "45-90 minutes",
        "benefits": "Fat burning, endurance base, mitochondrial development",
        "examples": ["Easy jog", "Moderate cycling", "Swimming laps"],
        "frequency": "3-5 times per week"
    },
    "zone_3_tempo": {
        "intensity": "70-80% max HR",
        "duration": "30-45 minutes",
        "benefits": "Lactate threshold improvement, race pace training",
        "examples": ["Tempo runs", "Steady state cardio", "Sustained efforts"],
        "frequency": "1-2 times per week"
    },
    "zone_4_threshold": {
        "intensity": "80-90% max HR",
        "duration": "10-30 minutes total",
        "benefits": "VO2 max improvement, performance gains",
        "examples": ["Interval training", "Hill repeats", "Track workouts"],
        "frequency": "1-2 times per week"
    },
    "zone_5_maximum": {
        "intensity": "90-100% max HR",
        "duration": "1-5 minutes intervals",
        "benefits": "Peak power, sprint speed, anaerobic capacity",
        "examples": ["All-out sprints", "HIIT intervals", "Max effort bursts"],
        "frequency": "1 time per week max"
    }
}

# Strength training rep ranges and goals
rep_range_goals = {
    "strength": {
        "rep_range": "1-5 reps",
        "sets": "4-6 sets",
        "rest": "3-5 minutes",
        "load": "85-100% 1RM",
        "adaptations": "Neural efficiency, max force production"
    },
    "hypertrophy": {
        "rep_range": "6-12 reps",
        "sets": "3-5 sets",
        "rest": "60-90 seconds",
        "load": "70-85% 1RM",
        "adaptations": "Muscle size, metabolic stress, mechanical tension"
    },
    "muscular_endurance": {
        "rep_range": "12-20+ reps",
        "sets": "2-4 sets",
        "rest": "30-60 seconds",
        "load": "50-70% 1RM",
        "adaptations": "Local muscular endurance, work capacity"
    },
    "power": {
        "rep_range": "1-5 reps",
        "sets": "3-5 sets",
        "rest": "3-5 minutes",
        "load": "30-60% 1RM (explosive)",
        "adaptations": "Rate of force development, speed"
    }
}

# Exercise substitutions and alternatives
exercise_alternatives = {
    "barbell_squat": ["Front squat", "Goblet squat", "Bulgarian split squat", "Leg press", "Hack squat"],
    "bench_press": ["Dumbbell press", "Push-ups", "Dips", "Cable chest press", "Floor press"],
    "deadlift": ["Romanian deadlift", "Trap bar deadlift", "Sumo deadlift", "Rack pulls", "Good mornings"],
    "pull_ups": ["Lat pulldown", "Assisted pull-ups", "Inverted rows", "Cable rows", "Band pull-aparts"],
    "overhead_press": ["Dumbbell press", "Arnold press", "Pike push-ups", "Landmine press", "Machine press"],
    "running": ["Cycling", "Swimming", "Rowing", "Elliptical", "Stair climber", "Jump rope"],
    "planks": ["Dead bugs", "Bird dogs", "Pallof press", "Ab wheel", "Hollow holds"]
}

# Muscle group training frequency
training_frequency = {
    "beginner": {
        "full_body": "3 times per week",
        "muscle_groups": {"per_week": 1, "rest_between": "48-72 hours"},
        "rationale": "Need more recovery, learning movement patterns"
    },
    "intermediate": {
        "upper_lower": "4 times per week",
        "muscle_groups": {"per_week": 2, "rest_between": "48 hours"},
        "rationale": "Better recovery capacity, can handle more volume"
    },
    "advanced": {
        "ppl_or_bro_split": "5-6 times per week",
        "muscle_groups": {"per_week": 2, "rest_between": "24-48 hours"},
        "rationale": "High work capacity, optimized recovery strategies"
    }
}

# Common exercise form cues
form_cues = {
    "squat": {
        "setup": ["Feet shoulder-width", "Toes slightly out", "Bar on traps or front delts"],
        "execution": ["Chest up", "Knees track over toes", "Break at hips and knees", "Depth to parallel or below"],
        "common_errors": ["Knees caving in", "Forward lean", "Heels lifting", "Partial ROM"]
    },
    "deadlift": {
        "setup": ["Bar over mid-foot", "Shoulder blades over bar", "Neutral spine", "Arms straight"],
        "execution": ["Drive through heels", "Hips and shoulders rise together", "Full hip extension", "Control descent"],
        "common_errors": ["Rounded back", "Hips shooting up first", "Jerking the bar", "Hyperextension at top"]
    },
    "bench_press": {
        "setup": ["Eyes under bar", "Feet flat on floor", "Shoulder blades retracted", "Slight arch"],
        "execution": ["Lower to chest", "Elbows 45 degrees", "Press in slight arc", "Full lockout"],
        "common_errors": ["Flared elbows", "Bouncing off chest", "No leg drive", "Uneven press"]
    },
    "overhead_press": {
        "setup": ["Bar at clavicle", "Grip just outside shoulders", "Core braced", "Glutes tight"],
        "execution": ["Press straight up", "Move head back", "Full lockout", "Controlled descent"],
        "common_errors": ["Leaning back excessively", "No head movement", "Partial ROM", "Poor core stability"]
    }
}

# Deload week protocols
deload_protocols = {
    "reduce_volume": {
        "method": "Keep intensity, reduce sets/reps by 40-50%",
        "example": "If normally 4x8, do 2x8 at same weight",
        "best_for": "Advanced lifters, high volume programs"
    },
    "reduce_intensity": {
        "method": "Keep volume, reduce weight by 30-40%",
        "example": "If normally 4x8 at 200 lbs, do 4x8 at 130 lbs",
        "best_for": "Beginners, technique refinement"
    },
    "active_recovery": {
        "method": "Replace training with light activities",
        "example": "Yoga, swimming, walking, mobility work",
        "best_for": "Those feeling very fatigued or minor injuries"
    },
    "complete_rest": {
        "method": "No structured training for 5-7 days",
        "example": "Focus on sleep, nutrition, life activities",
        "best_for": "Post-competition, severe fatigue, injury recovery"
    }
}

# Fitness tracking metrics
tracking_metrics = {
    "body_measurements": {
        "frequency": "Weekly or bi-weekly",
        "key_measures": ["Weight", "Body fat %", "Waist", "Hips", "Arms", "Thighs", "Chest"],
        "timing": "Same day/time each week, ideally morning before eating",
        "tools": ["Scale", "Tape measure", "Calipers or DEXA scan"]
    },
    "performance_metrics": {
        "frequency": "Each workout",
        "key_measures": ["Weight lifted", "Reps completed", "Total volume", "Workout duration", "RPE (Rate of Perceived Exertion)"],
        "tracking": "Workout journal or app",
        "purpose": "Progressive overload tracking"
    },
    "recovery_metrics": {
        "frequency": "Daily",
        "key_measures": ["Sleep quality/duration", "Muscle soreness (1-10)", "Energy levels", "Mood", "Resting heart rate"],
        "tracking": "Simple journal or app",
        "purpose": "Ensure adequate recovery"
    },
    "progress_photos": {
        "frequency": "Every 2-4 weeks",
        "angles": ["Front", "Side", "Back"],
        "consistency": "Same lighting, time of day, clothing, pose",
        "purpose": "Visual progress tracking"
    }
}

# Sample weekly workout schedules
sample_weekly_schedules = {
    "beginner_3day": {
        "monday": {"workout": "Full Body A", "focus": "Compound movements", "duration": 45},
        "tuesday": {"workout": "Rest or Light Cardio", "focus": "Recovery", "duration": 30},
        "wednesday": {"workout": "Full Body B", "focus": "Compound + accessories", "duration": 45},
        "thursday": {"workout": "Rest or Yoga", "focus": "Flexibility", "duration": 30},
        "friday": {"workout": "Full Body C", "focus": "Compound movements", "duration": 45},
        "saturday": {"workout": "Active Recovery", "focus": "Walking, stretching", "duration": 30},
        "sunday": {"workout": "Complete Rest", "focus": "Recovery", "duration": 0}
    },
    "intermediate_4day": {
        "monday": {"workout": "Upper Body", "focus": "Push/Pull balance", "duration": 60},
        "tuesday": {"workout": "Lower Body", "focus": "Squats, deadlifts", "duration": 60},
        "wednesday": {"workout": "Rest or Cardio", "focus": "Recovery/Conditioning", "duration": 30},
        "thursday": {"workout": "Upper Body", "focus": "Different exercises", "duration": 60},
        "friday": {"workout": "Lower Body", "focus": "Variations", "duration": 60},
        "saturday": {"workout": "Active Recovery or HIIT", "focus": "Conditioning", "duration": 30},
        "sunday": {"workout": "Complete Rest", "focus": "Recovery", "duration": 0}
    },
    "advanced_6day": {
        "monday": {"workout": "Push (Chest, Shoulders, Triceps)", "focus": "Pressing movements", "duration": 75},
        "tuesday": {"workout": "Pull (Back, Biceps)", "focus": "Pulling movements", "duration": 75},
        "wednesday": {"workout": "Legs", "focus": "Squats, leg accessories", "duration": 90},
        "thursday": {"workout": "Push", "focus": "Volume day", "duration": 75},
        "friday": {"workout": "Pull", "focus": "Deadlift variations", "duration": 75},
        "saturday": {"workout": "Legs", "focus": "Posterior chain", "duration": 90},
        "sunday": {"workout": "Complete Rest or Active Recovery", "focus": "Full recovery", "duration": 30}
    }
}
