"""
Student Performance Prediction - Standalone Python Script
This script runs the complete ML workflow without requiring Jupyter
"""

# Import required libraries (will check if installed)
import sys

def check_and_install_packages():
    """Check if required packages are installed"""
    required_packages = {
        'pandas': 'pandas',
        'numpy': 'numpy', 
        'sklearn': 'scikit-learn',
        'matplotlib': 'matplotlib',
        'seaborn': 'seaborn'
    }
    
    missing = []
    for module, package in required_packages.items():
        try:
            __import__(module)
        except ImportError:
            missing.append(package)
    
    if missing:
        print(f"Missing packages: {', '.join(missing)}")
        print(f"\nPlease install them using:")
        print(f"py -m pip install {' '.join(missing)}")
        return False
    return True

if not check_and_install_packages():
    sys.exit(1)

# Now import everything
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.linear_model import LinearRegression, Ridge, Lasso
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error
import warnings
warnings.filterwarnings('ignore')

print("="*80)
print("STUDENT PERFORMANCE PREDICTION - ML PROJECT")
print("="*80)

# Load data
print("\n[1/8] Loading dataset...")
df = pd.read_csv('data/student_data.csv')
print(f"✓ Dataset loaded: {df.shape[0]} students, {df.shape[1]} features")

# Basic info
print("\n[2/8] Dataset Overview:")
print(f"  - Shape: {df.shape}")
print(f"  - Missing values: {df.isnull().sum().sum()}")
print(f"  - Target variable (Final_Grade) range: {df['Final_Grade'].min()}-{df['Final_Grade'].max()}")

# Preprocessing
print("\n[3/8] Preprocessing data...")
df_processed = df.copy()

# Encode categorical variable
label_encoder = LabelEncoder()
df_processed['Parental_Support_Encoded'] = label_encoder.fit_transform(df_processed['Parental_Support'])

# Feature engineering
df_processed['Study_Efficiency'] = df_processed['Study_Hours_Per_Week'] * df_processed['Attendance_Percentage'] / 100
df_processed['Overall_Engagement'] = (df_processed['Participation_Score'] + df_processed['Extracurricular_Activities']) / 2
df_processed['Academic_Balance'] = df_processed['Study_Hours_Per_Week'] / (df_processed['Sleep_Hours'] + 1)

print("✓ Created 3 engineered features")

# Prepare features
feature_columns = ['Study_Hours_Per_Week', 'Previous_Grade', 'Attendance_Percentage', 
                   'Participation_Score', 'Sleep_Hours', 'Extracurricular_Activities',
                   'Parental_Support_Encoded', 'Study_Efficiency', 'Overall_Engagement', 
                   'Academic_Balance']

X = df_processed[feature_columns]
y = df_processed['Final_Grade']

# Split data
print("\n[4/8] Splitting data...")
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
print(f"✓ Training: {X_train.shape[0]} samples | Testing: {X_test.shape[0]} samples")

# Scale features
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)
print("✓ Features scaled")

# Train models
print("\n[5/8] Training machine learning models...")
models = {
    'Linear Regression': LinearRegression(),
    'Ridge Regression': Ridge(alpha=1.0, random_state=42),
    'Lasso Regression': Lasso(alpha=0.1, random_state=42),
    'Decision Tree': DecisionTreeRegressor(max_depth=10, random_state=42),
    'Random Forest': RandomForestRegressor(n_estimators=100, max_depth=10, random_state=42),
    'Gradient Boosting': GradientBoostingRegressor(n_estimators=100, max_depth=5, random_state=42)
}

results = {}
for name, model in models.items():
    model.fit(X_train_scaled, y_train)
    y_test_pred = model.predict(X_test_scaled)
    
    test_r2 = r2_score(y_test, y_test_pred)
    test_rmse = np.sqrt(mean_squared_error(y_test, y_test_pred))
    test_mae = mean_absolute_error(y_test, y_test_pred)
    
    results[name] = {
        'test_r2': test_r2,
        'test_rmse': test_rmse,
        'test_mae': test_mae,
        'model': model
    }
    print(f"  ✓ {name:20s} - R²: {test_r2:.4f}, RMSE: {test_rmse:.4f}")

# Results
print("\n[6/8] Model Performance Comparison:")
print("-" * 80)
print(f"{'Model':<25} {'R² Score':<12} {'RMSE':<12} {'MAE':<12} {'Accuracy %':<12}")
print("-" * 80)

sorted_results = sorted(results.items(), key=lambda x: x[1]['test_r2'], reverse=True)
for name, metrics in sorted_results:
    print(f"{name:<25} {metrics['test_r2']:<12.4f} {metrics['test_rmse']:<12.4f} {metrics['test_mae']:<12.4f} {metrics['test_r2']*100:<12.2f}")

print("-" * 80)

# Best model
best_model_name = sorted_results[0][0]
best_metrics = sorted_results[0][1]

print(f"\n[7/8] Best Model Analysis:")
print(f"  🏆 Model: {best_model_name}")
print(f"  📊 Test R² Score: {best_metrics['test_r2']:.4f} ({best_metrics['test_r2']*100:.2f}% accuracy)")
print(f"  📉 RMSE: {best_metrics['test_rmse']:.4f}")
print(f"  📉 MAE: {best_metrics['test_mae']:.4f}")

# Feature importance (if applicable)
if best_model_name in ['Decision Tree', 'Random Forest', 'Gradient Boosting']:
    print(f"\n  Feature Importance ({best_model_name}):")
    feature_importance = pd.DataFrame({
        'Feature': feature_columns,
        'Importance': best_metrics['model'].feature_importances_
    }).sort_values('Importance', ascending=False)
    
    for idx, row in feature_importance.head(5).iterrows():
        print(f"    {row['Feature']:<30s}: {row['Importance']:.4f}")

# Key insights
print("\n[8/8] Key Insights:")
correlation_matrix = df[df.select_dtypes(include=[np.number]).columns].corr()
top_correlations = correlation_matrix['Final_Grade'].sort_values(ascending=False)[1:4]

print("  Most influential factors:")
for feature, corr in top_correlations.items():
    print(f"    • {feature}: {corr:.3f} correlation")

print("\n  Parental Support Impact:")
support_impact = df.groupby('Parental_Support')['Final_Grade'].mean().sort_values(ascending=False)
for level, avg_grade in support_impact.items():
    print(f"    • {level} Support: Average grade {avg_grade:.2f}")

print("\n" + "="*80)
print("✅ ANALYSIS COMPLETE!")
print("="*80)
print(f"\nProject achieved {best_metrics['test_r2']*100:.1f}% accuracy in predicting student performance.")
print("All models trained and evaluated successfully!")
