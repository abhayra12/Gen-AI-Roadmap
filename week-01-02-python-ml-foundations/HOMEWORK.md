# 📝 Homework Assignment - Week 1-2

**Module:** Python & ML Foundations  
**Due:** End of Week 2  
**Points:** 100

---

## 🎯 Assignment Overview

**Objective:** Build a complete data analysis and machine learning pipeline for manufacturing quality control.

**Skills Demonstrated:**
- Data loading and cleaning
- Exploratory Data Analysis
- Feature engineering
- Model training and evaluation
- Code organization and documentation

---

## 📊 Dataset

**Dataset:** Manufacturing Quality Control Data  
**File:** `datasets/manufacturing/quality_data.csv`

### Dataset Description
Simulated manufacturing data with:
- **Product Features:** Dimensions, weight, temperature, pressure
- **Process Parameters:** Machine settings, operator, shift
- **Quality Metrics:** Defect type, severity, pass/fail

### Columns
- `product_id`: Unique identifier
- `production_date`: Manufacturing date
- `machine_id`: Machine used
- `operator_id`: Operator ID
- `shift`: Day/Night shift
- `dimension_x`, `dimension_y`, `dimension_z`: Product dimensions (mm)
- `weight`: Product weight (g)
- `temperature`: Processing temperature (°C)
- `pressure`: Processing pressure (bar)
- `defect_type`: Type of defect (if any)
- `severity`: Low/Medium/High
- `quality_status`: Pass/Fail

---

## 📋 Task Breakdown

### Part 1: Data Loading & Exploration (20 points)

**Tasks:**
1. Load the dataset using pandas
2. Display basic information (shape, dtypes, memory usage)
3. Check for missing values
4. Generate summary statistics
5. Identify data quality issues

**Deliverables:**
- Code cells showing data loading
- Summary table of data characteristics
- List of identified issues

**Rubric:**
- Correct data loading (5 pts)
- Comprehensive data inspection (10 pts)
- Clear documentation (5 pts)

---

### Part 2: Exploratory Data Analysis (25 points)

**Tasks:**
1. **Univariate Analysis**
   - Distribution of numerical features
   - Frequency of categorical features
   - Identify outliers

2. **Bivariate Analysis**
   - Correlation between features
   - Quality status vs features
   - Defect patterns by machine/operator/shift

3. **Visualizations** (minimum 6)
   - Histograms for numerical features
   - Bar plots for categorical features
   - Correlation heatmap
   - Boxplots for outlier detection
   - Scatter plots for relationships
   - Time series trends

**Deliverables:**
- Minimum 6 high-quality visualizations
- Written insights for each visualization
- Summary of key findings

**Rubric:**
- Quality of visualizations (10 pts)
- Depth of analysis (10 pts)
- Insights quality (5 pts)

---

### Part 3: Data Preprocessing (20 points)

**Tasks:**
1. **Handle Missing Values**
   - Identify missing data patterns
   - Choose appropriate strategy (imputation/removal)
   - Implement solution

2. **Feature Engineering**
   - Create derived features
   - Encode categorical variables
   - Scale numerical features

3. **Handle Outliers**
   - Identify outliers
   - Decide treatment strategy
   - Apply corrections

4. **Train-Test Split**
   - Split data (80/20 or 70/30)
   - Ensure stratification
   - Verify split quality

**Deliverables:**
- Preprocessing pipeline code
- Before/after comparison
- Cleaned dataset ready for modeling

**Rubric:**
- Missing data handling (5 pts)
- Feature engineering (7 pts)
- Proper train-test split (5 pts)
- Pipeline organization (3 pts)

---

### Part 4: Model Training (25 points)

**Tasks:**
1. **Baseline Model**
   - Train simple model (Logistic Regression or Decision Tree)
   - Evaluate performance

2. **Multiple Models**
   - Train at least 3 different models:
     - Logistic Regression
     - Random Forest
     - Gradient Boosting (XGBoost or similar)
   
3. **Hyperparameter Tuning**
   - Use GridSearchCV or RandomizedSearchCV
   - Optimize at least one model

4. **Model Comparison**
   - Compare all models on consistent metrics
   - Select best model

**Deliverables:**
- Training code for all models
- Hyperparameter tuning results
- Performance comparison table

**Rubric:**
- Model variety (8 pts)
- Hyperparameter tuning (8 pts)
- Proper evaluation (6 pts)
- Model selection justification (3 pts)

---

### Part 5: Model Evaluation & Insights (10 points)

**Tasks:**
1. **Evaluation Metrics**
   - Accuracy, Precision, Recall, F1-Score
   - Confusion Matrix
   - ROC-AUC curve
   - Feature importance

2. **Business Insights**
   - Which features most impact quality?
   - Which machines/operators need attention?
   - Recommendations for quality improvement

**Deliverables:**
- Comprehensive evaluation report
- Visualized confusion matrix and ROC curve
- Feature importance plot
- Business recommendations (2-3 paragraphs)

**Rubric:**
- Evaluation completeness (5 pts)
- Business insights quality (5 pts)

---

## 📦 Submission Requirements

### File Structure
```
homework/week-01-02/
├── README.md                          # Project overview
├── manufacturing_analysis.ipynb       # Main notebook
├── requirements.txt                   # Dependencies used
├── src/                              # (Optional) Modular code
│   ├── preprocessing.py
│   └── modeling.py
├── models/                           # Saved models
│   └── best_model.pkl
├── reports/                          # Generated reports
│   ├── EDA_report.md
│   └── model_evaluation.md
└── figures/                          # Saved visualizations
    ├── correlation_heatmap.png
    ├── feature_importance.png
    └── ...
```

### Notebook Requirements
1. **Clear Structure**
   - Markdown sections for each part
   - Well-commented code
   - Cell outputs visible

2. **Reproducibility**
   - Set random seeds
   - Include requirements.txt
   - Clear execution order

3. **Documentation**
   - README explaining project
   - Inline comments
   - Analysis insights

### Submission Steps
```bash
# 1. Create homework directory
mkdir -p homework/week-01-02
cd homework/week-01-02

# 2. Complete your work
# ... work on assignment ...

# 3. Commit to Git
git add .
git commit -m "Complete Week 1-2 homework: Manufacturing Quality Analysis"
git push

# 4. Update progress tracker
# Mark homework as complete in PROGRESS_TRACKER.md
```

---

## 🎯 Grading Rubric

| Component | Points | Criteria |
|-----------|--------|----------|
| **Part 1: Data Exploration** | 20 | Thorough data inspection and documentation |
| **Part 2: EDA** | 25 | High-quality visualizations and insights |
| **Part 3: Preprocessing** | 20 | Proper data cleaning and feature engineering |
| **Part 4: Modeling** | 25 | Multiple models with proper evaluation |
| **Part 5: Insights** | 10 | Business recommendations |
| **Bonus: Code Quality** | +10 | Clean code, modular structure, documentation |
| **Total** | 100+10 | |

### Grade Scale
- **90-100:** Excellent - Production-ready quality
- **80-89:** Good - Solid understanding
- **70-79:** Satisfactory - Meets requirements
- **Below 70:** Needs improvement - Review topics

---

## 💡 Helpful Tips

### EDA Tips
- Start simple, then go deeper
- Always label axes and add titles
- Use color effectively
- Write insights as you discover them

### Modeling Tips
- Start with baseline (simple model)
- Use cross-validation
- Don't overfit on training data
- Document your decisions

### Code Tips
```python
# Set random seed for reproducibility
import numpy as np
import random
np.random.seed(42)
random.seed(42)

# Save your best model
import joblib
joblib.dump(best_model, 'models/best_model.pkl')

# Save figures
import matplotlib.pyplot as plt
plt.savefig('figures/my_plot.png', dpi=300, bbox_inches='tight')
```

---

## 📚 Resources

### Pandas
- [10 Minutes to Pandas](https://pandas.pydata.org/docs/user_guide/10min.html)
- [Data Cleaning Tutorial](https://realpython.com/python-data-cleaning-numpy-pandas/)

### Visualization
- [Matplotlib Tutorial](https://matplotlib.org/stable/tutorials/index.html)
- [Seaborn Gallery](https://seaborn.pydata.org/examples/index.html)

### Scikit-learn
- [Preprocessing Guide](https://scikit-learn.org/stable/modules/preprocessing.html)
- [Model Selection](https://scikit-learn.org/stable/model_selection.html)
- [Metrics Guide](https://scikit-learn.org/stable/modules/model_evaluation.html)

---

## ❓ FAQ

### Q: Can I use additional libraries?
**A:** Yes! But document them in requirements.txt.

### Q: How many visualizations are enough?
**A:** Minimum 6, but quality > quantity. Each should provide insights.

### Q: Should I create functions or write inline code?
**A:** Both! Start inline for exploration, then refactor important code into functions.

### Q: What if my model accuracy is low?
**A:** That's okay! Focus on proper methodology. Explain why accuracy might be low and what could improve it.

### Q: Can I use automated ML tools (AutoML)?
**A:** Not for this assignment. The goal is to learn the process manually.

---

## 🚀 Bonus Challenges (+10 points each)

### Challenge 1: Advanced Feature Engineering
- Create interaction features
- Polynomial features
- Time-based features
- Domain-specific features

### Challenge 2: Model Explainability
- Use SHAP or LIME
- Explain individual predictions
- Feature interaction analysis

### Challenge 3: Deployment Ready
- Create prediction function
- Save preprocessing pipeline
- Write inference script
- Create simple API (FastAPI)

---

## ✅ Self-Assessment Checklist

Before submitting, verify:

- [ ] All 5 parts completed
- [ ] Code runs without errors
- [ ] Notebook is well-organized
- [ ] Visualizations are clear and labeled
- [ ] README is comprehensive
- [ ] Models are saved
- [ ] Requirements.txt is included
- [ ] Committed to Git
- [ ] No sensitive data in repo
- [ ] Passed self-review

---

## 🎯 Learning Outcomes

By completing this assignment, you will:
- ✅ Handle real-world messy data
- ✅ Perform comprehensive EDA
- ✅ Build ML pipelines
- ✅ Compare multiple models
- ✅ Generate business insights
- ✅ Create reproducible analysis

---

## 📧 Getting Help

**Stuck?**
1. Review relevant notebooks
2. Check course FAQ
3. Search Stack Overflow
4. Ask in GitHub Discussions
5. Review documentation

**Remember:** Struggle is part of learning! Try to solve problems independently before asking for help.

---

## 🎉 Submission Confirmation

When you're done:

1. Run all cells from top to bottom
2. Save notebook with outputs
3. Commit and push to GitHub
4. Update PROGRESS_TRACKER.md
5. Give yourself a pat on the back! 🎉

**You've completed your first Gen AI Masters homework!**

---

<div align="center">

**Week 1-2 Homework** | Manufacturing Quality Analysis

[🏠 Course Home](../../README.md) | [📚 Week 1-2 README](../README.md) | [❓ FAQ](../../FAQ.md)

</div>
