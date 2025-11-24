import { NextRequest, NextResponse } from "next/server";

// AI Model API endpoint (Python Flask server)
const AI_MODEL_API = process.env.AI_MODEL_API_URL || "http://localhost:5000/api/predict-workout";

// Additional specialized meal plans
const specializedDiets: any = {
  vegetarian: true,
  vegan: true,
  keto: true,
  lowCarb: true,
  highProtein: true,
  paleo: true,
  mediterranean: true,
};

// Workout intensity modifiers
const intensityLevels = {
  light: 0.7,
  moderate: 1.0,
  high: 1.3,
  extreme: 1.6
};

// Validate workout plan
function validateWorkoutPlan(plan: any) {
  return {
    schedule: plan.schedule,
    exercises: plan.exercises.map((exercise: any) => ({
      day: exercise.day,
      routines: exercise.routines.map((routine: any) => ({
        name: routine.name,
        sets: typeof routine.sets === "number" ? routine.sets : parseInt(routine.sets) || 1,
        reps: typeof routine.reps === "number" ? routine.reps : parseInt(routine.reps) || 10,
      })),
    })),
  };
}

// Validate diet plan
function validateDietPlan(plan: any) {
  return {
    dailyCalories: plan.dailyCalories,
    meals: plan.meals.map((meal: any) => ({
      name: meal.name,
      foods: meal.foods,
    })),
  };
}

// Comprehensive fallback function to generate workout plan based on user data
function generateWorkoutPlanFallback(formData: any) {
  const { fitnessGoals, fitnessLevel, age, weight, height, injuries } = formData;
  const ageNum = parseInt(age) || 25;
  const weightNum = parseInt(weight) || 70;
  
  // Define workout databases
  const workoutDatabase = {
    beginner: {
      'weight loss': {
        schedule: ["Monday", "Wednesday", "Friday"],
        exercises: [
          {
            day: "Monday",
            routines: [
              { name: "Brisk Walking", sets: 1, reps: 30 },
              { name: "Bodyweight Squats", sets: 3, reps: 12 },
              { name: "Wall Push-ups", sets: 3, reps: 10 },
              { name: "Standing Calf Raises", sets: 3, reps: 15 },
              { name: "Plank Hold", sets: 3, reps: 20 },
            ]
          },
          {
            day: "Wednesday",
            routines: [
              { name: "Jumping Jacks", sets: 3, reps: 20 },
              { name: "Lunges", sets: 3, reps: 10 },
              { name: "Knee Push-ups", sets: 3, reps: 12 },
              { name: "Bicycle Crunches", sets: 3, reps: 15 },
              { name: "High Knees", sets: 3, reps: 30 },
            ]
          },
          {
            day: "Friday",
            routines: [
              { name: "Jump Rope", sets: 3, reps: 60 },
              { name: "Mountain Climbers", sets: 3, reps: 15 },
              { name: "Burpees", sets: 3, reps: 8 },
              { name: "Leg Raises", sets: 3, reps: 12 },
              { name: "Side Plank", sets: 3, reps: 20 },
            ]
          }
        ]
      },
      'build muscle': {
        schedule: ["Monday", "Wednesday", "Friday"],
        exercises: [
          {
            day: "Monday",
            routines: [
              { name: "Push-ups", sets: 4, reps: 10 },
              { name: "Dumbbell Chest Press", sets: 3, reps: 12 },
              { name: "Dumbbell Shoulder Press", sets: 3, reps: 10 },
              { name: "Tricep Dips", sets: 3, reps: 10 },
              { name: "Plank", sets: 3, reps: 30 },
            ]
          },
          {
            day: "Wednesday",
            routines: [
              { name: "Bodyweight Squats", sets: 4, reps: 15 },
              { name: "Lunges", sets: 3, reps: 12 },
              { name: "Glute Bridges", sets: 3, reps: 15 },
              { name: "Calf Raises", sets: 4, reps: 20 },
              { name: "Dead Bug", sets: 3, reps: 15 },
            ]
          },
          {
            day: "Friday",
            routines: [
              { name: "Pull-ups (Assisted)", sets: 3, reps: 8 },
              { name: "Dumbbell Rows", sets: 4, reps: 12 },
              { name: "Bicep Curls", sets: 3, reps: 12 },
              { name: "Hammer Curls", sets: 3, reps: 10 },
              { name: "Russian Twists", sets: 3, reps: 20 },
            ]
          }
        ]
      },
      'improve fitness': {
        schedule: ["Monday", "Wednesday", "Friday"],
        exercises: [
          {
            day: "Monday",
            routines: [
              { name: "Jogging", sets: 1, reps: 20 },
              { name: "Squats", sets: 3, reps: 15 },
              { name: "Push-ups", sets: 3, reps: 12 },
              { name: "Lunges", sets: 3, reps: 10 },
              { name: "Plank", sets: 3, reps: 30 },
            ]
          },
          {
            day: "Wednesday",
            routines: [
              { name: "Cycling", sets: 1, reps: 25 },
              { name: "Step-ups", sets: 3, reps: 12 },
              { name: "Dumbbell Press", sets: 3, reps: 10 },
              { name: "Crunches", sets: 3, reps: 20 },
              { name: "Jumping Jacks", sets: 3, reps: 30 },
            ]
          },
          {
            day: "Friday",
            routines: [
              { name: "Swimming", sets: 1, reps: 30 },
              { name: "Burpees", sets: 3, reps: 10 },
              { name: "Mountain Climbers", sets: 3, reps: 15 },
              { name: "Leg Raises", sets: 3, reps: 15 },
              { name: "Side Plank", sets: 3, reps: 25 },
            ]
          }
        ]
      }
    },
    intermediate: {
      'weight loss': {
        schedule: ["Monday", "Tuesday", "Thursday", "Friday"],
        exercises: [
          {
            day: "Monday",
            routines: [
              { name: "Running", sets: 1, reps: 30 },
              { name: "Jump Squats", sets: 4, reps: 15 },
              { name: "Push-ups", sets: 4, reps: 20 },
              { name: "Burpees", sets: 4, reps: 12 },
              { name: "Mountain Climbers", sets: 4, reps: 20 },
            ]
          },
          {
            day: "Tuesday",
            routines: [
              { name: "HIIT Intervals", sets: 5, reps: 3 },
              { name: "Box Jumps", sets: 4, reps: 12 },
              { name: "Kettlebell Swings", sets: 4, reps: 15 },
              { name: "Battle Ropes", sets: 4, reps: 30 },
              { name: "Plank to Push-up", sets: 3, reps: 12 },
            ]
          },
          {
            day: "Thursday",
            routines: [
              { name: "Cycling Intervals", sets: 1, reps: 40 },
              { name: "Jump Lunges", sets: 4, reps: 12 },
              { name: "Dumbbell Thrusters", sets: 4, reps: 15 },
              { name: "High Knees", sets: 4, reps: 30 },
              { name: "Russian Twists", sets: 4, reps: 25 },
            ]
          },
          {
            day: "Friday",
            routines: [
              { name: "Rowing Machine", sets: 1, reps: 25 },
              { name: "Tuck Jumps", sets: 4, reps: 10 },
              { name: "Dumbbell Snatch", sets: 4, reps: 12 },
              { name: "Plyo Push-ups", sets: 3, reps: 10 },
              { name: "V-ups", sets: 4, reps: 15 },
            ]
          }
        ]
      },
      'build muscle': {
        schedule: ["Monday", "Tuesday", "Thursday", "Friday"],
        exercises: [
          {
            day: "Monday",
            routines: [
              { name: "Barbell Bench Press", sets: 4, reps: 10 },
              { name: "Incline Dumbbell Press", sets: 4, reps: 12 },
              { name: "Cable Flyes", sets: 3, reps: 15 },
              { name: "Overhead Press", sets: 4, reps: 10 },
              { name: "Lateral Raises", sets: 3, reps: 15 },
            ]
          },
          {
            day: "Tuesday",
            routines: [
              { name: "Barbell Squats", sets: 5, reps: 8 },
              { name: "Romanian Deadlifts", sets: 4, reps: 10 },
              { name: "Leg Press", sets: 4, reps: 12 },
              { name: "Leg Curls", sets: 3, reps: 15 },
              { name: "Calf Raises", sets: 4, reps: 20 },
            ]
          },
          {
            day: "Thursday",
            routines: [
              { name: "Pull-ups", sets: 4, reps: 10 },
              { name: "Barbell Rows", sets: 4, reps: 10 },
              { name: "Lat Pulldowns", sets: 4, reps: 12 },
              { name: "Face Pulls", sets: 3, reps: 15 },
              { name: "Barbell Curls", sets: 4, reps: 12 },
            ]
          },
          {
            day: "Friday",
            routines: [
              { name: "Deadlifts", sets: 5, reps: 6 },
              { name: "Front Squats", sets: 4, reps: 10 },
              { name: "Walking Lunges", sets: 3, reps: 12 },
              { name: "Cable Woodchoppers", sets: 3, reps: 15 },
              { name: "Hanging Leg Raises", sets: 4, reps: 12 },
            ]
          }
        ]
      },
      'improve fitness': {
        schedule: ["Monday", "Wednesday", "Friday", "Saturday"],
        exercises: [
          {
            day: "Monday",
            routines: [
              { name: "Interval Running", sets: 1, reps: 35 },
              { name: "Goblet Squats", sets: 4, reps: 15 },
              { name: "Push-ups", sets: 4, reps: 20 },
              { name: "Dumbbell Rows", sets: 4, reps: 12 },
              { name: "Plank", sets: 3, reps: 60 },
            ]
          },
          {
            day: "Wednesday",
            routines: [
              { name: "Swimming", sets: 1, reps: 40 },
              { name: "Box Jumps", sets: 4, reps: 12 },
              { name: "Bench Dips", sets: 4, reps: 15 },
              { name: "Bicycle Crunches", sets: 4, reps: 25 },
              { name: "Burpees", sets: 3, reps: 15 },
            ]
          },
          {
            day: "Friday",
            routines: [
              { name: "Cycling", sets: 1, reps: 45 },
              { name: "Lunges", sets: 4, reps: 15 },
              { name: "Shoulder Press", sets: 4, reps: 12 },
              { name: "Pull-ups", sets: 3, reps: 10 },
              { name: "Russian Twists", sets: 4, reps: 30 },
            ]
          },
          {
            day: "Saturday",
            routines: [
              { name: "Hiking/Walking", sets: 1, reps: 60 },
              { name: "Bodyweight Circuit", sets: 3, reps: 15 },
              { name: "Core Work", sets: 4, reps: 20 },
              { name: "Stretching", sets: 1, reps: 15 },
            ]
          }
        ]
      }
    },
    advanced: {
      'weight loss': {
        schedule: ["Monday", "Tuesday", "Wednesday", "Friday", "Saturday"],
        exercises: [
          {
            day: "Monday",
            routines: [
              { name: "Sprint Intervals", sets: 8, reps: 2 },
              { name: "Box Jump Burpees", sets: 5, reps: 15 },
              { name: "Kettlebell Clean & Press", sets: 5, reps: 12 },
              { name: "Battle Ropes", sets: 5, reps: 45 },
              { name: "Plank Variations", sets: 4, reps: 60 },
            ]
          },
          {
            day: "Tuesday",
            routines: [
              { name: "Assault Bike", sets: 10, reps: 1 },
              { name: "Barbell Complexes", sets: 5, reps: 10 },
              { name: "Sled Push/Pull", sets: 6, reps: 30 },
              { name: "Tire Flips", sets: 4, reps: 10 },
              { name: "Hanging Leg Raises", sets: 4, reps: 15 },
            ]
          },
          {
            day: "Wednesday",
            routines: [
              { name: "Rowing Sprints", sets: 8, reps: 2 },
              { name: "Olympic Lifts", sets: 5, reps: 8 },
              { name: "Prowler Sprints", sets: 6, reps: 20 },
              { name: "Medicine Ball Slams", sets: 5, reps: 15 },
              { name: "Ab Wheel Rollouts", sets: 4, reps: 12 },
            ]
          },
          {
            day: "Friday",
            routines: [
              { name: "Jump Rope Double Unders", sets: 5, reps: 50 },
              { name: "Snatch Pulls", sets: 5, reps: 8 },
              { name: "Box Jumps", sets: 5, reps: 15 },
              { name: "Farmer's Walks", sets: 4, reps: 60 },
              { name: "Dragon Flags", sets: 3, reps: 10 },
            ]
          },
          {
            day: "Saturday",
            routines: [
              { name: "Long Distance Run", sets: 1, reps: 60 },
              { name: "Circuit Training", sets: 5, reps: 20 },
              { name: "HIIT Finisher", sets: 4, reps: 5 },
            ]
          }
        ]
      },
      'build muscle': {
        schedule: ["Monday", "Tuesday", "Thursday", "Friday", "Saturday"],
        exercises: [
          {
            day: "Monday",
            routines: [
              { name: "Barbell Bench Press", sets: 5, reps: 5 },
              { name: "Incline Barbell Press", sets: 4, reps: 8 },
              { name: "Weighted Dips", sets: 4, reps: 10 },
              { name: "Cable Crossovers", sets: 4, reps: 12 },
              { name: "Skull Crushers", sets: 4, reps: 12 },
            ]
          },
          {
            day: "Tuesday",
            routines: [
              { name: "Deadlifts", sets: 5, reps: 5 },
              { name: "Barbell Rows", sets: 5, reps: 8 },
              { name: "Weighted Pull-ups", sets: 4, reps: 8 },
              { name: "T-Bar Rows", sets: 4, reps: 10 },
              { name: "Preacher Curls", sets: 4, reps: 12 },
            ]
          },
          {
            day: "Thursday",
            routines: [
              { name: "Back Squats", sets: 5, reps: 5 },
              { name: "Front Squats", sets: 4, reps: 8 },
              { name: "Bulgarian Split Squats", sets: 4, reps: 10 },
              { name: "Leg Extensions", sets: 4, reps: 15 },
              { name: "Standing Calf Raises", sets: 5, reps: 20 },
            ]
          },
          {
            day: "Friday",
            routines: [
              { name: "Military Press", sets: 5, reps: 5 },
              { name: "Arnold Press", sets: 4, reps: 10 },
              { name: "Lateral Raises", sets: 4, reps: 15 },
              { name: "Face Pulls", sets: 4, reps: 15 },
              { name: "Shrugs", sets: 4, reps: 12 },
            ]
          },
          {
            day: "Saturday",
            routines: [
              { name: "Power Cleans", sets: 5, reps: 5 },
              { name: "Romanian Deadlifts", sets: 4, reps: 8 },
              { name: "Weighted Planks", sets: 4, reps: 60 },
              { name: "Cable Crunches", sets: 4, reps: 20 },
              { name: "Landmine Twists", sets: 4, reps: 15 },
            ]
          }
        ]
      },
      'improve fitness': {
        schedule: ["Monday", "Tuesday", "Thursday", "Friday", "Saturday"],
        exercises: [
          {
            day: "Monday",
            routines: [
              { name: "CrossFit WOD", sets: 1, reps: 30 },
              { name: "Olympic Lifts", sets: 5, reps: 5 },
              { name: "Gymnastics Skills", sets: 4, reps: 10 },
              { name: "Core Circuit", sets: 4, reps: 15 },
            ]
          },
          {
            day: "Tuesday",
            routines: [
              { name: "Distance Running", sets: 1, reps: 50 },
              { name: "Tempo Work", sets: 4, reps: 8 },
              { name: "Plyometrics", sets: 5, reps: 12 },
              { name: "Agility Drills", sets: 4, reps: 10 },
            ]
          },
          {
            day: "Thursday",
            routines: [
              { name: "Swimming", sets: 1, reps: 60 },
              { name: "Full Body Circuit", sets: 5, reps: 15 },
              { name: "Functional Movements", sets: 4, reps: 12 },
            ]
          },
          {
            day: "Friday",
            routines: [
              { name: "HIIT Training", sets: 10, reps: 2 },
              { name: "Compound Lifts", sets: 5, reps: 8 },
              { name: "Conditioning Work", sets: 4, reps: 20 },
            ]
          },
          {
            day: "Saturday",
            routines: [
              { name: "Sport-Specific Training", sets: 1, reps: 90 },
              { name: "Active Recovery", sets: 1, reps: 30 },
            ]
          }
        ]
      }
    }
  };

  // Normalize inputs
  const level = (fitnessLevel || 'beginner').toLowerCase();
  let goal = (fitnessGoals || 'improve fitness').toLowerCase();
  
  // Match goal variations
  if (goal.includes('loss') || goal.includes('lose') || goal.includes('weight')) goal = 'weight loss';
  else if (goal.includes('muscle') || goal.includes('gain') || goal.includes('bulk')) goal = 'build muscle';
  else goal = 'improve fitness';

  // Get base workout
  let workout = workoutDatabase[level]?.[goal] || workoutDatabase.beginner['improve fitness'];
  
  // Adjust based on age (older = lower intensity)
  if (ageNum > 50) {
    workout = JSON.parse(JSON.stringify(workout)); // Deep clone
    workout.exercises.forEach(day => {
      day.routines.forEach(routine => {
        routine.sets = Math.max(2, routine.sets - 1);
        routine.reps = Math.max(8, Math.floor(routine.reps * 0.8));
      });
    });
  }
  
  // Adjust for injuries
  if (injuries && injuries.toLowerCase() !== 'none' && !injuries.toLowerCase().includes('no')) {
    workout = JSON.parse(JSON.stringify(workout));
    if (injuries.toLowerCase().includes('knee')) {
      workout.exercises.forEach(day => {
        day.routines = day.routines.filter(r => 
          !r.name.toLowerCase().includes('squat') && 
          !r.name.toLowerCase().includes('lunge') &&
          !r.name.toLowerCase().includes('jump')
        );
      });
    }
    if (injuries.toLowerCase().includes('shoulder') || injuries.toLowerCase().includes('arm')) {
      workout.exercises.forEach(day => {
        day.routines = day.routines.filter(r => 
          !r.name.toLowerCase().includes('press') && 
          !r.name.toLowerCase().includes('push')
        );
      });
    }
  }

  return workout;
}

// Comprehensive fallback function to generate diet plan based on user data
function generateDietPlanFallback(formData: any) {
  const { fitnessGoals, age, weight, height, allergies, fitnessLevel } = formData;
  const ageNum = parseInt(age) || 25;
  const weightNum = parseInt(weight) || 70;
  const heightNum = parseInt(height) || 170;
  
  // Calculate BMR (Basal Metabolic Rate) using Mifflin-St Jeor Equation
  const bmr = 10 * weightNum + 6.25 * heightNum - 5 * ageNum + 5;
  
  // Activity multipliers
  const activityMultipliers = {
    beginner: 1.3,
    intermediate: 1.55,
    advanced: 1.725
  };
  
  const level = (fitnessLevel || 'beginner').toLowerCase();
  const tdee = bmr * (activityMultipliers[level as keyof typeof activityMultipliers] || 1.3);
  
  // Adjust calories based on goal
  let goal = (fitnessGoals || 'improve fitness').toLowerCase();
  let targetCalories = Math.round(tdee);
  
  if (goal.includes('loss') || goal.includes('lose')) {
    targetCalories = Math.round(tdee - 500); // 500 calorie deficit
    goal = 'weight loss';
  } else if (goal.includes('muscle') || goal.includes('gain') || goal.includes('bulk')) {
    targetCalories = Math.round(tdee + 300); // 300 calorie surplus
    goal = 'build muscle';
  } else {
    goal = 'maintain';
  }
  
  // Ensure minimum calories
  targetCalories = Math.max(1200, targetCalories);
  
  // Diet plan database
  const dietDatabase: any = {
    'weight loss': {
      breakfast: [
        ["Oatmeal with berries", "Greek yogurt", "Green tea"],
        ["Scrambled egg whites", "Whole grain toast", "Orange juice"],
        ["Protein smoothie", "Banana", "Chia seeds"],
        ["Avocado toast on whole grain", "Poached egg", "Black coffee"],
        ["Greek yogurt parfait", "Granola", "Mixed berries"],
      ],
      morningSnack: [
        ["Apple", "Almonds (10-12)"],
        ["Carrot sticks", "Hummus"],
        ["Low-fat cottage cheese", "Cucumber slices"],
        ["Protein bar", "Green tea"],
        ["Mixed nuts (small handful)", "Pear"],
      ],
      lunch: [
        ["Grilled chicken salad", "Quinoa", "Lemon water"],
        ["Turkey wrap", "Mixed greens", "Cucumber water"],
        ["Tuna salad", "Brown rice", "Herbal tea"],
        ["Vegetable stir-fry", "Tofu", "Green tea"],
        ["Grilled fish", "Sweet potato", "Steamed broccoli"],
      ],
      afternoonSnack: [
        ["Protein shake", "Berries"],
        ["Rice cakes", "Almond butter"],
        ["Edamame", "Cherry tomatoes"],
        ["Greek yogurt", "Walnuts"],
        ["Celery sticks", "Peanut butter"],
      ],
      dinner: [
        ["Baked salmon", "Asparagus", "Cauliflower rice"],
        ["Grilled chicken breast", "Green beans", "Mixed salad"],
        ["Lean beef", "Roasted vegetables", "Small portion brown rice"],
        ["Shrimp stir-fry", "Zucchini noodles", "Bell peppers"],
        ["Turkey meatballs", "Marinara sauce", "Spaghetti squash"],
      ]
    },
    'build muscle': {
      breakfast: [
        ["Scrambled eggs (3 whole)", "Oatmeal", "Whole milk", "Banana"],
        ["Protein pancakes", "Greek yogurt", "Honey", "Berries"],
        ["Breakfast burrito", "Eggs", "Cheese", "Avocado"],
        ["French toast", "Protein powder", "Peanut butter", "Maple syrup"],
        ["Egg white omelet", "Turkey sausage", "Hash browns", "Orange juice"],
      ],
      morningSnack: [
        ["Protein shake", "Banana", "Peanut butter"],
        ["Trail mix", "Protein bar"],
        ["Greek yogurt", "Granola", "Honey"],
        ["Tuna sandwich", "Whole grain bread"],
        ["Smoothie bowl", "Protein powder", "Mixed nuts"],
      ],
      lunch: [
        ["Grilled chicken breast", "Brown rice", "Broccoli", "Sweet potato"],
        ["Beef stir-fry", "Jasmine rice", "Mixed vegetables"],
        ["Salmon fillet", "Quinoa", "Asparagus", "Avocado"],
        ["Turkey burger", "Whole wheat bun", "Sweet potato fries"],
        ["Pasta with chicken", "Marinara sauce", "Side salad", "Garlic bread"],
      ],
      afternoonSnack: [
        ["Protein shake", "Banana", "Oats"],
        ["Cottage cheese", "Pineapple", "Almonds"],
        ["Rice cakes", "Peanut butter", "Honey"],
        ["Hard-boiled eggs (2)", "Whole grain crackers"],
        ["Protein bar", "Apple", "Walnuts"],
      ],
      dinner: [
        ["Steak", "Baked potato", "Grilled vegetables", "Dinner roll"],
        ["Grilled salmon", "Wild rice", "Brussels sprouts"],
        ["Chicken thighs", "Pasta", "Alfredo sauce", "Steamed broccoli"],
        ["Pork chops", "Mashed potatoes", "Green beans"],
        ["Shrimp", "Fried rice", "Egg", "Mixed vegetables"],
      ],
      eveningSnack: [
        ["Casein protein shake", "Berries"],
        ["Cottage cheese", "Almonds"],
        ["Greek yogurt", "Honey", "Granola"],
      ]
    },
    'maintain': {
      breakfast: [
        ["Whole grain cereal", "Milk", "Banana", "Coffee"],
        ["Eggs (2)", "Whole wheat toast", "Avocado", "Orange juice"],
        ["Smoothie bowl", "Granola", "Mixed fruits"],
        ["Oatmeal", "Protein powder", "Berries", "Green tea"],
        ["Greek yogurt", "Honey", "Nuts", "Apple"],
      ],
      morningSnack: [
        ["Fruit salad", "Handful of nuts"],
        ["Protein bar", "Coffee"],
        ["Yogurt", "Granola"],
        ["Apple", "Cheese stick"],
        ["Smoothie", "Chia seeds"],
      ],
      lunch: [
        ["Chicken sandwich", "Side salad", "Fruit"],
        ["Grain bowl", "Quinoa", "Chicken", "Vegetables"],
        ["Soup", "Whole grain bread", "Small salad"],
        ["Sushi rolls", "Edamame", "Miso soup"],
        ["Burrito bowl", "Brown rice", "Beans", "Vegetables"],
      ],
      afternoonSnack: [
        ["Hummus", "Veggie sticks"],
        ["Trail mix"],
        ["Protein shake"],
        ["Rice cakes", "Almond butter"],
        ["Fruit", "String cheese"],
      ],
      dinner: [
        ["Grilled chicken", "Roasted vegetables", "Quinoa"],
        ["Fish tacos", "Cabbage slaw", "Black beans"],
        ["Stir-fry", "Tofu or chicken", "Brown rice"],
        ["Pasta primavera", "Grilled chicken", "Side salad"],
        ["Grilled salmon", "Sweet potato", "Steamed broccoli"],
      ]
    }
  };

  // Select random items from each category
  const selectRandom = (arr: any[]) => arr[Math.floor(Math.random() * arr.length)];
  
  const selectedDiet = dietDatabase[goal] || dietDatabase.maintain;
  
  // Handle allergies
  const hasAllergy = (food: string, allergyList: string) => {
    if (!allergyList || allergyList.toLowerCase().includes('none')) return false;
    const lower = allergyList.toLowerCase();
    const foodLower = food.toLowerCase();
    
    if (lower.includes('dairy') && (foodLower.includes('milk') || foodLower.includes('cheese') || 
        foodLower.includes('yogurt') || foodLower.includes('butter'))) return true;
    if (lower.includes('nut') && (foodLower.includes('nut') || foodLower.includes('peanut') || 
        foodLower.includes('almond'))) return true;
    if (lower.includes('gluten') && (foodLower.includes('bread') || foodLower.includes('pasta') || 
        foodLower.includes('wheat'))) return true;
    if (lower.includes('egg') && foodLower.includes('egg')) return true;
    if (lower.includes('fish') && (foodLower.includes('fish') || foodLower.includes('salmon') || 
        foodLower.includes('tuna'))) return true;
    if (lower.includes('shellfish') && (foodLower.includes('shrimp') || foodLower.includes('crab'))) return true;
    
    return false;
  };
  
  const filterAllergies = (foods: string[]) => {
    return foods.filter(food => !hasAllergy(food, allergies || ''));
  };

  const meals = [
    {
      name: "Breakfast",
      foods: filterAllergies(selectRandom(selectedDiet.breakfast))
    },
    {
      name: "Morning Snack",
      foods: filterAllergies(selectRandom(selectedDiet.morningSnack))
    },
    {
      name: "Lunch",
      foods: filterAllergies(selectRandom(selectedDiet.lunch))
    },
    {
      name: "Afternoon Snack",
      foods: filterAllergies(selectRandom(selectedDiet.afternoonSnack))
    },
    {
      name: "Dinner",
      foods: filterAllergies(selectRandom(selectedDiet.dinner))
    }
  ];
  
  // Add evening snack for muscle building
  if (goal === 'build muscle' && selectedDiet.eveningSnack) {
    meals.push({
      name: "Evening Snack",
      foods: filterAllergies(selectRandom(selectedDiet.eveningSnack))
    });
  }

  return {
    dailyCalories: targetCalories,
    meals: meals.filter(meal => meal.foods.length > 0) // Remove meals with all foods filtered out
  };
}

export async function POST(request: NextRequest) {
  try {
    console.log("API Route: Received request");

    const formData = await request.json();
    console.log("Form data received:", formData);

    const {
      fitnessGoals,
      fitnessLevel,
      injuries,
      allergies,
      age,
      weight,
      height,
      additionalInfo,
    } = formData;

    // 🤖 TRY AI MODEL FIRST (Python RNN Model)
    console.log("🤖 Attempting to use AI RNN Model...");
    try {
      const aiResponse = await fetch(AI_MODEL_API, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(formData),
        signal: AbortSignal.timeout(10000), // 10 second timeout
      });

      if (aiResponse.ok) {
        const aiData = await aiResponse.json();
        
        if (aiData.success && aiData.workoutPlan && aiData.dietPlan) {
          console.log("✅ AI Model generated plan successfully!");
          
          // Add tips and recommendations
          const userLevel = fitnessLevel || 'beginner';
          const ageNum = parseInt(age) || 25;
          const goal = (fitnessGoals || '').toLowerCase();
          
          const tips = [];
          const warnings = [];
          
          // General tips based on level
          if (userLevel === 'beginner') {
            tips.push("Start slow and focus on proper form before increasing intensity");
            tips.push("Take rest days seriously - they're crucial for muscle recovery");
            tips.push("Stay hydrated throughout your workouts");
          } else if (userLevel === 'intermediate') {
            tips.push("Consider tracking your progress with measurements and photos");
            tips.push("Mix up your routine every 4-6 weeks to avoid plateaus");
            tips.push("Focus on progressive overload - gradually increase weight or reps");
          } else if (userLevel === 'advanced') {
            tips.push("Implement periodization in your training for optimal results");
            tips.push("Consider working with a coach for specialized programming");
            tips.push("Pay attention to mobility and recovery work");
          }
          
          // Goal-specific tips
          if (goal.includes('loss') || goal.includes('lose')) {
            tips.push("Maintain a consistent calorie deficit of 300-500 calories");
            tips.push("Prioritize protein to preserve muscle mass while losing fat");
            tips.push("Combine cardio with strength training for best results");
          } else if (goal.includes('muscle') || goal.includes('gain')) {
            tips.push("Eat in a slight calorie surplus (200-300 calories above maintenance)");
            tips.push("Consume 1.6-2.2g of protein per kg of body weight");
            tips.push("Get 7-9 hours of quality sleep for muscle recovery");
          }
          
          // Age-based warnings
          if (ageNum > 50) {
            warnings.push("Consult with a healthcare provider before starting any new exercise program");
            warnings.push("Focus on low-impact exercises if you have joint concerns");
            warnings.push("Warm up thoroughly before each workout");
          }
          
          if (ageNum > 65) {
            warnings.push("Consider balance and stability exercises to prevent falls");
            warnings.push("Monitor your heart rate during cardiovascular exercise");
          }

          return NextResponse.json({
            success: true,
            workoutPlan: aiData.workoutPlan,
            dietPlan: aiData.dietPlan,
            generatedAt: new Date().toISOString(),
            generatedBy: "AI RNN Model (90% Accuracy)",
            modelInfo: aiData.modelInfo,
            tips: tips,
            warnings: warnings.length > 0 ? warnings : undefined,
            hydration: `Drink ${userLevel === 'beginner' ? '8-10' : userLevel === 'intermediate' ? '10-12' : '12-15'} glasses of water daily`,
            supplements: goal.includes('muscle') 
              ? ["Whey Protein", "Creatine Monohydrate", "Multivitamin"] 
              : ["Multivitamin", "Fish Oil", "Vitamin D3"],
          });
        }
      }
    } catch (aiError) {
      console.log("⚠️ AI Model not available, falling back to traditional method...");
      console.error("AI Model error:", aiError);
    }

    // FALLBACK: Original OpenAI/Gemini/Local logic
    console.log("Using traditional plan generation...");

    // Determine workout days based on fitness level
    let workoutDays = "3-4 days per week";
    if (fitnessLevel === "beginner") {
      workoutDays = "3 days per week (e.g., Monday, Wednesday, Friday)";
    } else if (fitnessLevel === "intermediate") {
      workoutDays = "4-5 days per week";
    } else if (fitnessLevel === "advanced") {
      workoutDays = "5-6 days per week";
    }

    // Generate Workout Plan
    const workoutPrompt = `You are an experienced fitness coach creating a personalized workout plan based on:
    Age: ${age} years
    Height: ${height} cm
    Weight: ${weight} kg
    Injuries or limitations: ${injuries || "None"}
    Available days for workout: ${workoutDays}
    Fitness goal: ${fitnessGoals}
    Fitness level: ${fitnessLevel}
    Additional information: ${additionalInfo || "None"}
    
    As a professional coach:
    - Consider muscle group splits to avoid overtraining the same muscles on consecutive days
    - Design exercises that match the fitness level and account for any injuries
    - Structure the workouts to specifically target the user's fitness goal
    - For beginners, focus on foundational movements and proper form
    - For intermediate/advanced, include more complex exercises and variations
    
    CRITICAL SCHEMA INSTRUCTIONS:
    - Your output MUST contain ONLY the fields specified below, NO ADDITIONAL FIELDS
    - "sets" and "reps" MUST ALWAYS be NUMBERS, never strings
    - For example: "sets": 3, "reps": 10
    - Do NOT use text like "reps": "As many as possible" or "reps": "To failure"
    - Instead use specific numbers like "reps": 12 or "reps": 15
    - For cardio, use "sets": 1, "reps": 20 (representing 20 minutes) or another appropriate number
    - NEVER include strings for numerical fields
    - NEVER add extra fields not shown in the example below
    
    Return a JSON object with this EXACT structure:
    {
      "schedule": ["Monday", "Wednesday", "Friday"],
      "exercises": [
        {
          "day": "Monday",
          "routines": [
            {
              "name": "Exercise Name",
              "sets": 3,
              "reps": 10
            }
          ]
        }
      ]
    }
    
    DO NOT add any fields that are not in this example. Your response must be a valid JSON object with no additional text.`;

    console.log("Generating workout plan using fallback...");
    let workoutPlan;
    
    // Use local fallback to generate workout plan
    workoutPlan = generateWorkoutPlanFallback(formData);
    
    workoutPlan = validateWorkoutPlan(workoutPlan);
    console.log("Workout plan validated successfully");

    // Generate Diet Plan
    const dietPrompt = `You are an experienced nutrition coach creating a personalized diet plan based on:
      Age: ${age} years
      Height: ${height} cm
      Weight: ${weight} kg
      Fitness goal: ${fitnessGoals}
      Fitness level: ${fitnessLevel}
      Dietary restrictions/allergies: ${allergies || "None"}
      Additional information: ${additionalInfo || "None"}
      
      As a professional nutrition coach:
      - Calculate appropriate daily calorie intake based on the person's stats and goals
      - Create a balanced meal plan with proper macronutrient distribution
      - Include a variety of nutrient-dense foods while respecting dietary restrictions
      - Consider meal timing around workouts for optimal performance and recovery
      - Adjust portions and macros based on whether goal is weight loss, muscle gain, or maintenance
      
      CRITICAL SCHEMA INSTRUCTIONS:
      - Your output MUST contain ONLY the fields specified below, NO ADDITIONAL FIELDS
      - "dailyCalories" MUST be a NUMBER, not a string
      - DO NOT add fields like "supplements", "macros", "notes", or ANYTHING else
      - ONLY include the EXACT fields shown in the example below
      - Each meal should include ONLY a "name" and "foods" array
      - Provide at least 4-5 meals per day (breakfast, snack, lunch, snack, dinner)

      Return a JSON object with this EXACT structure and no other fields:
      {
        "dailyCalories": 2000,
        "meals": [
          {
            "name": "Breakfast",
            "foods": ["Oatmeal with berries", "Greek yogurt", "Black coffee"]
          },
          {
            "name": "Morning Snack",
            "foods": ["Apple", "Almonds"]
          },
          {
            "name": "Lunch",
            "foods": ["Grilled chicken salad", "Whole grain bread", "Water"]
          },
          {
            "name": "Afternoon Snack",
            "foods": ["Protein shake", "Banana"]
          },
          {
            "name": "Dinner",
            "foods": ["Baked salmon", "Quinoa", "Steamed broccoli"]
          }
        ]
      }
      
      DO NOT add any fields that are not in this example. Your response must be a valid JSON object with no additional text.`;

    console.log("Generating diet plan using fallback...");
    let dietPlan;
    
    // Use local fallback to generate diet plan
    dietPlan = generateDietPlanFallback(formData);
    
    dietPlan = validateDietPlan(dietPlan);
    console.log("Diet plan validated successfully");

    console.log("Successfully generated both plans");

    // Add fitness tips and recommendations
    const userLevel = formData.fitnessLevel || 'beginner';
    const ageNum = parseInt(formData.age) || 25;
    const goal = (formData.fitnessGoals || '').toLowerCase();
    
    const tips = [];
    const warnings = [];
    
    // General tips based on level
    if (userLevel === 'beginner') {
      tips.push("Start slow and focus on proper form before increasing intensity");
      tips.push("Take rest days seriously - they're crucial for muscle recovery");
      tips.push("Stay hydrated throughout your workouts");
    } else if (userLevel === 'intermediate') {
      tips.push("Consider tracking your progress with measurements and photos");
      tips.push("Mix up your routine every 4-6 weeks to avoid plateaus");
      tips.push("Focus on progressive overload - gradually increase weight or reps");
    } else if (userLevel === 'advanced') {
      tips.push("Implement periodization in your training for optimal results");
      tips.push("Consider working with a coach for specialized programming");
      tips.push("Pay attention to mobility and recovery work");
    }
    
    // Goal-specific tips
    if (goal.includes('loss') || goal.includes('lose')) {
      tips.push("Maintain a consistent calorie deficit of 300-500 calories");
      tips.push("Prioritize protein to preserve muscle mass while losing fat");
      tips.push("Combine cardio with strength training for best results");
    } else if (goal.includes('muscle') || goal.includes('gain')) {
      tips.push("Eat in a slight calorie surplus (200-300 calories above maintenance)");
      tips.push("Consume 1.6-2.2g of protein per kg of body weight");
      tips.push("Get 7-9 hours of quality sleep for muscle recovery");
    }
    
    // Age-based warnings
    if (ageNum > 50) {
      warnings.push("Consult with a healthcare provider before starting any new exercise program");
      warnings.push("Focus on low-impact exercises if you have joint concerns");
      warnings.push("Warm up thoroughly before each workout");
    }
    
    if (ageNum > 65) {
      warnings.push("Consider balance and stability exercises to prevent falls");
      warnings.push("Monitor your heart rate during cardiovascular exercise");
    }

    return NextResponse.json({
      success: true,
      workoutPlan,
      dietPlan,
      generatedAt: new Date().toISOString(),
      tips: tips,
      warnings: warnings.length > 0 ? warnings : undefined,
      hydration: `Drink ${userLevel === 'beginner' ? '8-10' : userLevel === 'intermediate' ? '10-12' : '12-15'} glasses of water daily`,
      supplements: goal.includes('muscle') 
        ? ["Whey Protein", "Creatine Monohydrate", "Multivitamin"] 
        : ["Multivitamin", "Fish Oil", "Vitamin D3"],
    });
  } catch (error: any) {
    console.error("Detailed error in API route:", error);
    console.error("Error message:", error?.message);
    console.error("Error stack:", error?.stack);
    
    return NextResponse.json(
      {
        success: false,
        error: error instanceof Error ? error.message : "Failed to generate fitness plan",
        details: error?.toString(),
      },
      { status: 500 }
    );
  }
}
