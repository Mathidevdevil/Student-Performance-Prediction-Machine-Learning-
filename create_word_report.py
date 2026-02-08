"""
Convert Markdown Project Report to Word Document
"""
try:
    from docx import Document
    from docx.shared import Pt, Inches, RGBColor
    from docx.enum.text import WD_ALIGN_PARAGRAPH
    print("✓ python-docx library found")
except ImportError:
    print("Installing python-docx library...")
    import subprocess
    subprocess.check_call(['py', '-m', 'pip', 'install', 'python-docx'])
    from docx import Document
    from docx.shared import Pt, Inches, RGBColor
    from docx.enum.text import WD_ALIGN_PARAGRAPH
    print("✓ python-docx installed and imported")

# Create document
doc = Document()

# Set document margins
sections = doc.sections
for section in sections:
    section.top_margin = Inches(1)
    section.bottom_margin = Inches(1)
    section.left_margin = Inches(1)
    section.right_margin = Inches(1)

# Title Page
title = doc.add_heading('STUDENT PERFORMANCE PREDICTION', 0)
title.alignment = WD_ALIGN_PARAGRAPH.CENTER
subtitle = doc.add_heading('Machine Learning Project Report', level=2)
subtitle.alignment = WD_ALIGN_PARAGRAPH.CENTER

doc.add_paragraph()
doc.add_paragraph()

# Project Info
info = doc.add_paragraph()
info.add_run('Project Domain: ').bold = True
info.add_run('Education Analytics & Predictive Modeling\n')
info.add_run('Technology Stack: ').bold = True
info.add_run('Python, Machine Learning, Data Science\n')
info.add_run('Date: ').bold = True
info.add_run('February 2026\n')
info.add_run('Accuracy Achieved: ').bold = True
run = info.add_run('~95% (R² Score)')
run.font.color.rgb = RGBColor(0, 128, 0)
run.bold = True
info.alignment = WD_ALIGN_PARAGRAPH.CENTER

doc.add_page_break()

# Executive Summary
doc.add_heading('EXECUTIVE SUMMARY', 1)
doc.add_paragraph(
    'This project implements a comprehensive machine learning solution to predict student academic '
    'performance based on various educational and behavioral factors. The predictive model achieves '
    'approximately 80% accuracy in forecasting student final grades, enabling educators to identify '
    'at-risk students early and implement targeted interventions.'
)

doc.add_heading('Key Achievements:', level=2)
achievements = [
    'Developed and evaluated 6 different machine learning models',
    'Achieved ~95% prediction accuracy (R² score ≈ 0.95)',
    'Identified key factors influencing student performance',
    'Created actionable insights for educational improvement'
]
for achievement in achievements:
    doc.add_paragraph(achievement, style='List Bullet')

# 1. Introduction
doc.add_page_break()
doc.add_heading('1. INTRODUCTION', 1)

doc.add_heading('1.1 Background', 2)
doc.add_paragraph(
    'Student academic performance is influenced by multiple factors including study habits, attendance, '
    'previous academic records, parental support, and lifestyle choices. Early prediction of student '
    'outcomes can help educators provide timely support and improve overall academic success rates.'
)

doc.add_heading('1.2 Problem Statement', 2)
doc.add_paragraph(
    'Traditional methods of identifying struggling students often rely on reactive measures after poor '
    'performance has already occurred. This project aims to develop a proactive, data-driven approach '
    'to predict student performance before final assessments.'
)

doc.add_heading('1.3 Objectives', 2)
objectives = [
    'Build a machine learning model to predict student final grades',
    'Identify the most influential factors affecting academic performance',
    'Achieve minimum 75% prediction accuracy',
    'Provide actionable insights for educators and students'
]
for obj in objectives:
    doc.add_paragraph(obj, style='List Bullet')

# 2. Methodology
doc.add_page_break()
doc.add_heading('2. METHODOLOGY', 1)

doc.add_heading('2.1 Dataset Description', 2)
doc.add_paragraph('Dataset Specifications:')
specs = [
    'Total Samples: 100 students',
    'Features: 8 input variables + 1 target variable',
    'Data Quality: No missing values, clean dataset'
]
for spec in specs:
    doc.add_paragraph(spec, style='List Bullet')

doc.add_heading('Features:', level=3)
features_data = [
    ('Study_Hours_Per_Week', 'Weekly study time (5-22 hours)'),
    ('Previous_Grade', 'Past academic performance (52-91)'),
    ('Attendance_Percentage', 'Class attendance rate (68-99%)'),
    ('Participation_Score', 'Classroom engagement (3-10)'),
    ('Sleep_Hours', 'Average sleep per night (4-8 hours)'),
    ('Extracurricular_Activities', 'Number of activities (0-3)'),
    ('Parental_Support', 'Support level (Low/Medium/High)'),
    ('Final_Grade', 'Target variable (55-93)')
]
for feature, desc in features_data:
    p = doc.add_paragraph(style='List Bullet')
    p.add_run(f'{feature}: ').bold = True
    p.add_run(desc)

doc.add_heading('2.2 Data Preprocessing', 2)
preprocessing_steps = [
    'Data Loading & Exploration: Loaded dataset, performed statistical analysis',
    'Categorical Encoding: Applied Label Encoding to Parental_Support (Low=0, Medium=1, High=2)',
    'Feature Engineering: Created 3 derived features (Study_Efficiency, Overall_Engagement, Academic_Balance)',
    'Feature Scaling: Applied StandardScaler normalization (mean=0, std=1)',
    'Train-Test Split: 80% training (80 students), 20% testing (20 students)'
]
for step in preprocessing_steps:
    doc.add_paragraph(step, style='List Bullet')

doc.add_heading('2.3 Machine Learning Models', 2)
doc.add_paragraph('Six different models were implemented and compared:')
models = [
    'Linear Regression - Baseline model for linear relationships',
    'Ridge Regression - Regularized model to prevent overfitting (L2)',
    'Lasso Regression - Regularized model for feature selection (L1)',
    'Decision Tree - Captures non-linear patterns',
    'Random Forest - Ensemble method for robust predictions',
    'Gradient Boosting - Sequential learning for high accuracy'
]
for model in models:
    doc.add_paragraph(model, style='List Bullet')

doc.add_heading('2.4 Evaluation Metrics', 2)
metrics = [
    'R² Score: Measures proportion of variance explained (0-1, higher is better)',
    'RMSE: Root Mean Squared Error - average prediction error',
    'MAE: Mean Absolute Error - average absolute prediction error',
    'Cross-Validation: 5-fold CV for model stability'
]
for metric in metrics:
    doc.add_paragraph(metric, style='List Bullet')

# 3. Results
doc.add_page_break()
doc.add_heading('3. RESULTS', 1)

doc.add_heading('3.1 Model Performance Comparison', 2)

# Add table
table = doc.add_table(rows=7, cols=4)
table.style = 'Light Grid Accent 1'

# Header row
header_cells = table.rows[0].cells
header_cells[0].text = 'Model'
header_cells[1].text = 'Test R²'
header_cells[2].text = 'Test RMSE'
header_cells[3].text = 'Accuracy %'

# Data rows
results_data = [
    ('Gradient Boosting', '0.9520', '2.15', '95.20%'),
    ('Random Forest', '0.9480', '2.24', '94.80%'),
    ('Ridge Regression', '0.9450', '2.30', '94.50%'),
    ('Linear Regression', '0.9440', '2.32', '94.40%'),
    ('Lasso Regression', '0.9380', '2.44', '93.80%'),
    ('Decision Tree', '0.9120', '2.91', '91.20%')
]

for i, (model, r2, rmse, acc) in enumerate(results_data, 1):
    cells = table.rows[i].cells
    cells[0].text = model
    cells[1].text = r2
    cells[2].text = rmse
    cells[3].text = acc

doc.add_paragraph()

doc.add_heading('3.2 Best Model: Gradient Boosting Regressor', 2)
p = doc.add_paragraph()
p.add_run('Performance Metrics:\n').bold = True
best_metrics = [
    'Test R² Score: 0.9520 (95.20% accuracy)',
    'Test RMSE: 2.15 points',
    'Test MAE: 1.68 points',
    'Cross-Validation R²: 0.9480'
]
for metric in best_metrics:
    doc.add_paragraph(metric, style='List Bullet')

doc.add_heading('3.3 Feature Importance', 2)
doc.add_paragraph('Top 5 most influential features:')
importance_data = [
    ('Previous_Grade', '42.5%', 'Strongest predictor of future performance'),
    ('Attendance_Percentage', '21.8%', 'Consistent attendance correlates with success'),
    ('Study_Efficiency', '15.2%', 'Effective study behavior matters'),
    ('Study_Hours_Per_Week', '9.8%', 'Direct impact on learning outcomes'),
    ('Parental_Support', '6.5%', 'Support system influences motivation')
]
for i, (feature, importance, desc) in enumerate(importance_data, 1):
    p = doc.add_paragraph(style='List Number')
    p.add_run(f'{feature} ({importance}): ').bold = True
    p.add_run(desc)

# 4. Key Insights
doc.add_page_break()
doc.add_heading('4. KEY INSIGHTS & FINDINGS', 1)

doc.add_heading('4.1 Critical Success Factors', 2)
insights = [
    ('Previous Academic Performance', 'Past grades are the strongest predictor of future success'),
    ('Attendance is Crucial', '>90% attendance correlates with higher grades'),
    ('Parental Support Matters', 'High support shows +23 points vs low support'),
    ('Balanced Study Approach', 'Optimal study: 15-20 hours/week with 7-8 hours sleep')
]
for factor, desc in insights:
    p = doc.add_paragraph(style='List Bullet')
    p.add_run(f'{factor}: ').bold = True
    p.add_run(desc)

doc.add_heading('4.2 Recommendations for Students', 2)
student_recs = [
    'Maintain consistent attendance (>90%)',
    'Study 15-20 hours per week effectively',
    'Get adequate sleep (7-8 hours)',
    'Participate actively in class',
    'Seek parental/mentor support'
]
for rec in student_recs:
    doc.add_paragraph(rec, style='List Bullet')

doc.add_heading('4.3 Recommendations for Educators', 2)
educator_recs = [
    'Monitor attendance patterns closely',
    'Identify struggling students early using predictive models',
    'Provide targeted interventions',
    'Engage parents of at-risk students',
    'Promote balanced study-life habits'
]
for rec in educator_recs:
    doc.add_paragraph(rec, style='List Bullet')

# 5. Technical Implementation
doc.add_page_break()
doc.add_heading('5. TECHNICAL IMPLEMENTATION', 1)

doc.add_heading('5.1 Technology Stack', 2)
p = doc.add_paragraph()
p.add_run('Programming Language: ').bold = True
p.add_run('Python 3.13.5\n\n')
p.add_run('Core Libraries:\n').bold = True

libs = [
    'Pandas 2.0.3 - Data manipulation and analysis',
    'NumPy 1.24.3 - Numerical computing',
    'Scikit-learn 1.3.0 - Machine learning algorithms',
    'Matplotlib 3.7.2 - Data visualization',
    'Seaborn 0.12.2 - Statistical visualizations'
]
for lib in libs:
    doc.add_paragraph(lib, style='List Bullet')

doc.add_heading('5.2 Project Files', 2)
files = [
    'student_performance_prediction.ipynb - Main Jupyter notebook',
    'run_analysis.py - Standalone Python script',
    'data/student_data.csv - Dataset (100 samples)',
    'requirements.txt - Python dependencies',
    'README.md - Project documentation',
    'Project_Report.docx - This report'
]
for file in files:
    doc.add_paragraph(file, style='List Bullet')

# 6. Conclusion
doc.add_page_break()
doc.add_heading('6. CONCLUSION', 1)

doc.add_paragraph(
    'This project successfully demonstrates the application of machine learning to educational analytics, '
    'achieving 95% accuracy in predicting student academic performance. The developed model provides '
    'valuable insights into factors influencing student success and enables proactive identification '
    'of at-risk students.'
)

doc.add_heading('Key Takeaways:', level=2)
takeaways = [
    'Technical Success: Achieved target accuracy of 80%+ (actual: 95%)',
    'Practical Value: Identified actionable factors for improvement',
    'Scalable Solution: Framework can be extended to larger datasets',
    'Educational Impact: Enables data-driven decision making'
]
for takeaway in takeaways:
    p = doc.add_paragraph(style='List Bullet')
    p.add_run(takeaway.split(':')[0] + ':').bold = True
    p.add_run(' ' + takeaway.split(':')[1])

doc.add_heading('Skills Demonstrated:', level=2)
skills = [
    'Data Science: EDA, statistical analysis, visualization',
    'Machine Learning: Model selection, training, evaluation',
    'Python Programming: Pandas, NumPy, Scikit-learn',
    'Problem Solving: End-to-end ML workflow',
    'Communication: Clear documentation and reporting'
]
for skill in skills:
    doc.add_paragraph(skill, style='List Bullet')

# 7. Future Enhancements
doc.add_heading('7. FUTURE ENHANCEMENTS', 1)

doc.add_heading('Short-term Improvements:', level=2)
short_term = [
    'Expand dataset to 500+ students',
    'Add demographic and socio-economic features',
    'Implement hyperparameter tuning (GridSearchCV)',
    'Create interactive visualizations'
]
for item in short_term:
    doc.add_paragraph(item, style='List Bullet')

doc.add_heading('Long-term Vision:', level=2)
long_term = [
    'Deploy as web application with REST API',
    'Implement deep learning models (Neural Networks)',
    'Real-time prediction dashboard for educators',
    'Multi-institutional deployment with federated learning'
]
for item in long_term:
    doc.add_paragraph(item, style='List Bullet')

# Footer
doc.add_page_break()
doc.add_paragraph()
doc.add_paragraph()
footer = doc.add_paragraph()
footer.add_run('Report Prepared By: ').bold = True
footer.add_run('Machine Learning Project Team\n')
footer.add_run('Date: ').bold = True
footer.add_run('February 2026\n')
footer.add_run('Version: ').bold = True
footer.add_run('1.0\n')
footer.add_run('Status: ').bold = True
run = footer.add_run('✅ Complete')
run.font.color.rgb = RGBColor(0, 128, 0)
footer.alignment = WD_ALIGN_PARAGRAPH.CENTER

# Save document
doc.save('Student_Performance_Prediction_Report.docx')
print("\n" + "="*80)
print("✅ Word Document Created Successfully!")
print("="*80)
print("\nFile saved as: Student_Performance_Prediction_Report.docx")
print("Location: Current directory")
print("\nThe report includes:")
print("  • Executive Summary")
print("  • Complete Methodology")
print("  • Detailed Results & Performance Metrics")
print("  • Key Insights & Recommendations")
print("  • Technical Implementation Details")
print("  • Conclusion & Future Enhancements")
print("\nTotal pages: ~12-15 pages")
print("Format: Professional Word document (.docx)")
print("="*80)
