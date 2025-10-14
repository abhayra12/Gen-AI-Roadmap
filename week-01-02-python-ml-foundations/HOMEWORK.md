# 📝 Homework Assignment - Week 1-2

**Module:** Python & ML Foundations  
**Due:** End of Week 2  
**Points:** 100

---

## 🎯 Assignment: Predictive Maintenance for Manufacturing Equipment

**Objective:** Apply your Python and ML skills to predict equipment failure based on sensor data from a manufacturing environment.

**Task:**
Build a complete data analysis and machine learning pipeline that:
1.  Loads and explores a predictive maintenance dataset.
2.  Performs comprehensive Exploratory Data Analysis (EDA) with visualizations to identify patterns that may lead to equipment failure.
3.  Preprocesses the data, which includes handling categorical features, scaling numerical data, and splitting the dataset for training and testing.
4.  Trains multiple classification models to predict the likelihood of machine failure.
5.  Evaluates and compares the performance of these models using metrics like F1-score, ROC-AUC, and confusion matrices.
6.  Generates actionable insights and recommendations for the maintenance team based on the best-performing model.

**Dataset:** A simulated predictive maintenance dataset will be used. This dataset contains sensor readings and operational data from various machines.

### Dataset Description
The dataset contains real-time data collected from sensors on manufacturing equipment. Each row represents a snapshot of a machine's state at a given time.

### Columns
-   `UDI`: Unique identifier for each data point.
-   `Product ID`: Identifier for the product being worked on.
-   `Type`: Quality variant of the product (L, M, H for Low, Medium, High).
-   `Air temperature [K]`: Ambient air temperature in Kelvin.
-   `Process temperature [K]`: Temperature of the manufacturing process in Kelvin.
-   `Rotational speed [rpm]`: Rotational speed of the machine's tool in revolutions per minute.
-   `Torque [Nm]`: Torque exerted by the tool in Newton-meters.
-   `Tool wear [min]`: Wear on the tool in minutes of usage.
-   `Machine failure`: Target variable. `1` if the machine failed, `0` otherwise.
-   `Failure_Type`: The type of failure (e.g., Tool Wear Failure, Heat Dissipation Failure, etc.). This can be used for more detailed analysis.

---

## 📋 Task Breakdown

### Part 1: Data Loading & EDA (20 points)

**Tasks:**
1.  Load the predictive maintenance dataset.
2.  Display basic information (`.info()`, `.describe()`).
3.  Check for missing values and assess data quality.
4.  Visualize the distribution of the target variable (`Machine failure`).
5.  Create at least four other visualizations (e.g., correlation heatmap, feature distributions by failure type) to understand the data.

**Deliverables:**
-   Code cells for loading and initial inspection.
-   A summary of your data quality findings.
-   At least five high-quality, labeled visualizations with written insights for each.

---

### Part 2: Data Preprocessing (20 points)

**Tasks:**
1.  **Feature Engineering**: Create at least one new feature from existing ones (e.g., `power = rotational_speed [rpm] * torque [Nm]`).
2.  **Encode Categorical Variables**: Convert the `Type` column into a numerical format using one-hot encoding.
3.  **Scale Numerical Features**: Use `StandardScaler` to scale the numerical features.
4.  **Train-Test Split**: Split the data into 80% training and 20% testing sets. Ensure you use stratification on the target variable to maintain the same class distribution in both sets.

**Deliverables:**
-   A clean, well-documented preprocessing pipeline.
-   A comparison of the data before and after preprocessing.
-   The final, cleaned dataset ready for modeling.

---

### Part 3: Model Training & Evaluation (30 points)

**Tasks:**
1.  **Train Multiple Models**: Train at least three different classification models (e.g., Logistic Regression, Random Forest, Gradient Boosting).
2.  **Evaluate Performance**: For each model, calculate and report:
    -   Accuracy, Precision, Recall, and F1-Score.
    -   A confusion matrix to visualize true vs. predicted labels.
3.  **Compare Models**: Create a summary table comparing the performance of all trained models.
4.  **Feature Importance**: For your best-performing model (e.g., Random Forest), plot the feature importances to understand which factors are most predictive of failure.

**Deliverables:**
-   Training code for all models.
-   A performance comparison table.
-   A confusion matrix and feature importance plot for the best model.
-   A brief justification for your choice of the best model.

---

### Part 4: Hyperparameter Tuning (15 points)

**Tasks:**
1.  **Select a Model**: Choose your best-performing model from Part 3.
2.  **Define Parameter Grid**: Create a parameter grid for hyperparameter tuning (e.g., `n_estimators`, `max_depth` for a Random Forest).
3.  **Perform Grid Search**: Use `GridSearchCV` with 5-fold cross-validation to find the optimal combination of parameters.
4.  **Evaluate Tuned Model**: Report the performance of the tuned model on the test set and compare it to the default model to show the impact of tuning.

**Deliverables:**
-   Code for the `GridSearchCV` setup and execution.
-   The best parameters found by the grid search.
-   A comparison of the tuned model's performance against the original.

---

### Part 5: Project Summary & Conclusion (15 points)

**Tasks:**
1.  **Summarize Your Findings**: Write a brief summary of the project. What was the goal? What steps did you take? What were the key results?
2.  **Conclusion**: What is your final recommendation? Which model should the manufacturing company use for predictive maintenance and why? What are the business implications?
3.  **Reflection**: Briefly reflect on any challenges you faced and what you learned during the project.

**Deliverables:**
-   A well-written summary and conclusion section in your notebook.

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
