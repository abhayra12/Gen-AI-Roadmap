# 📝 Homework Assignment: Predictive Maintenance Analysis

**Module:** Week 1-2: Python & ML Foundations  
**Program:** Gen AI Masters Program
**Due:** End of Week 2  
**Total Points:** 100

---

## 🎯 Assignment Objective

This assignment challenges you to apply your foundational Python and machine learning skills to a real-world industrial problem: **predictive maintenance**. You will build a complete data analysis and machine learning pipeline to predict equipment failure using sensor data from a manufacturing environment. This project will test your ability to handle data, train models, and derive actionable insights.

**Your mission:** To act as a data scientist for a manufacturing company and deliver a model that can anticipate machine failures, enabling proactive maintenance and reducing costly downtime.

---

## 📂 Dataset: Predictive Maintenance for Manufacturing

You will be working with a simulated predictive maintenance dataset that contains sensor readings and operational data from various machines on a factory floor. Each row represents a snapshot of a machine's state at a specific moment in time.

### Dataset Columns

-   `UDI`: Unique identifier for each data point (row).
-   `Product ID`: Identifier for the product being worked on by the machine.
-   `Type`: Quality variant of the product, denoted as L (Low), M (Medium), or H (High).
-   `Air temperature [K]`: Ambient air temperature in Kelvin.
-   `Process temperature [K]`: Temperature of the manufacturing process in Kelvin.
-   `Rotational speed [rpm]`: Rotational speed of the machine's tool in revolutions per minute.
-   `Torque [Nm]`: Torque exerted by the tool in Newton-meters. This is a measure of rotational force.
-   `Tool wear [min]`: The amount of time the tool has been in use, which correlates with its wear.
-   `Machine failure`: **This is your target variable.** A binary flag where `1` indicates that the machine failed at this time step, and `0` indicates it did not.
-   `Failure_Type`: A categorical variable describing the nature of the failure if one occurred (e.g., Tool Wear Failure, Heat Dissipation Failure). This can be used for a more detailed, multi-class analysis or for deeper EDA.

---

## 📋 Task Breakdown

This project is divided into five parts, mirroring a typical end-to-end machine learning workflow.

### Part 1: Data Loading & Exploratory Data Analysis (EDA) (20 points)

**Goal:** Understand the dataset's structure, quality, and underlying patterns.

**Tasks:**
1.  **Load the Dataset**: Load the predictive maintenance dataset into a Pandas DataFrame.
2.  **Initial Inspection**: Use `.info()`, `.describe()`, and `.head()` to get a first look at the data.
3.  **Data Quality Check**: Systematically check for missing values (`.isnull().sum()`) and duplicates.
4.  **Target Variable Analysis**: Visualize the distribution of the `Machine failure` target variable. Is the dataset balanced or imbalanced?
5.  **Comprehensive EDA**: Create at least four other insightful visualizations to explore relationships between features and the target. Examples include:
    -   A correlation heatmap to identify relationships between numerical features.
    -   Distribution plots (histograms or KDEs) of key numerical features, segmented by whether a failure occurred.
    -   Box plots to compare the distributions of sensor readings for failure vs. non-failure cases.
    -   A count plot to show the frequency of different `Failure_Type` categories.

**Deliverables:**
-   Code cells for loading and inspecting the data.
-   A markdown summary of your findings on data quality (missing values, duplicates, etc.).
-   At least five high-quality, clearly labeled visualizations, each accompanied by a written interpretation of the insights it provides.

---

### Part 2: Data Preprocessing & Feature Engineering (20 points)

**Goal:** Prepare the data for modeling by cleaning, transforming, and enhancing it.

**Tasks:**
1.  **Feature Engineering**: Create at least one new, meaningful feature from the existing ones. For example, you could calculate the power consumed by the machine (`power [W] = rotational_speed [rpm] * torque [Nm]`) or the temperature difference (`temp_diff [K] = process_temperature [K] - air_temperature [K]`). Justify your choice.
2.  **Encode Categorical Variables**: Convert the `Type` column into a numerical format. **One-hot encoding** is a suitable method here.
3.  **Scale Numerical Features**: Use `StandardScaler` from scikit-learn to scale all numerical features. This is crucial for distance-based and regularized models.
4.  **Train-Test Split**: Split the preprocessed data into training (80%) and testing (20%) sets. Crucially, use **stratification** on the `Machine failure` target variable to ensure that the proportion of failures is the same in both the train and test sets.

**Deliverables:**
-   A clean, well-documented preprocessing pipeline.
-   A comparison of the data (e.g., using `.head()` or `.describe()`) before and after preprocessing to demonstrate the transformations.
-   The final, cleaned, and split datasets ready for modeling.

---

### Part 3: Model Training & Evaluation (30 points)

**Goal:** Train several classification models and rigorously evaluate their performance to find the best one.

**Tasks:**
1.  **Train Multiple Models**: Train at least three different types of classification models. Good choices include:
    -   **Logistic Regression** (as a simple baseline).
    -   **Random Forest Classifier** (a powerful ensemble model).
    -   **Gradient Boosting Classifier** (e.g., `XGBoost`, `LightGBM`, or `scikit-learn's GradientBoostingClassifier`).
2.  **Evaluate Performance**: For each model, calculate and report the following metrics on the **test set**:
    -   Accuracy, Precision, Recall, and F1-Score.
    -   Display a **confusion matrix** to visualize how the model is performing on each class.
3.  **Compare Models**: Create a summary table or a bar chart that clearly compares the key performance metrics (especially F1-Score and Recall) of all trained models.
4.  **Feature Importance**: For your best-performing tree-based model (e.g., Random Forest), plot the **feature importances** to understand which factors are most predictive of machine failure.

**Deliverables:**
-   Training code for all models.
-   A performance comparison table or chart.
-   A confusion matrix and feature importance plot for the best-performing model.
-   A brief markdown cell justifying your choice of the "best" model based on the problem context (hint: is it more important to avoid missing a failure or to avoid false alarms?).

---

### Part 4: Hyperparameter Tuning (15 points)

**Goal:** Optimize your best model to squeeze out additional performance.

**Tasks:**
1.  **Select a Model**: Choose your best-performing model from Part 3 for tuning.
2.  **Define Parameter Grid**: Create a parameter grid for the hyperparameters you want to tune. For a Random Forest, this might include `n_estimators`, `max_depth`, `min_samples_split`, and `min_samples_leaf`.
3.  **Perform Grid Search**: Use `GridSearchCV` with 5-fold cross-validation to systematically search for the optimal combination of parameters.
4.  **Evaluate Tuned Model**: Report the performance of the tuned model on the test set. Compare its performance to the default model to demonstrate the impact of tuning.

**Deliverables:**
-   Code for the `GridSearchCV` setup and execution.
-   A statement of the best parameters found by the grid search.
-   A clear comparison of the tuned model's performance against the original, untuned model.

---

### Part 5: Project Summary & Conclusion (15 points)

**Goal:** Communicate your results and provide actionable recommendations.

**Tasks:**
1.  **Summarize Your Findings**: Write a concise summary of the project. What was the business goal? What were the key steps in your workflow? What were the most important results?
2.  **Conclusion & Recommendations**: Based on your analysis, what is your final recommendation? Which model should the company deploy? What are the business implications of using this model (e.g., potential cost savings, operational improvements)?
3.  **Reflection**: Briefly reflect on any challenges you faced during the project (e.g., imbalanced data, feature selection) and what you learned in the process.

**Deliverables:**
-   A well-written summary and conclusion section in your notebook, aimed at both technical and non-technical stakeholders.

---

## 📦 Submission Requirements

A professional project is well-organized. Please follow this structure.

### Recommended File Structure
```
homework/week-01-02/
├── README.md                          # A brief overview of your project
├── manufacturing_analysis.ipynb       # Your main Jupyter Notebook with all analysis and outputs
├── requirements.txt                   # A list of all Python libraries used (e.g., pandas, scikit-learn)
├── models/                            # (Optional but good practice)
│   └── best_predictive_model.pkl      # Your saved, trained model
└── figures/                           # (Optional but good practice)
    ├── correlation_heatmap.png
    ├── feature_importance.png
    └── ...
```

### Notebook Requirements
1.  **Clear Structure**: Use markdown cells to structure your notebook into the five parts of the assignment.
2.  **Well-Commented Code**: Explain your code, especially complex parts.
3.  **Visible Outputs**: Ensure all cell outputs (tables, plots, metrics) are visible in the submitted notebook.
4.  **Reproducibility**: Set a random seed (e.g., `np.random.seed(42)`) at the beginning of your notebook to ensure your results are reproducible.

### Submission Steps
```bash
# 1. Ensure your project is in the correct directory structure
#    homework/week-01-02/

# 2. Generate your requirements.txt file
pip freeze > requirements.txt

# 3. Commit your work to Git
git add .
git commit -m "Complete Week 1-2 homework: Predictive Maintenance Analysis"
git push

# 4. Update your progress tracker
# Mark the homework as complete in the main PROGRESS_TRACKER.md
```

---

## 💡 Helpful Tips & Best Practices

### EDA
-   Always start by understanding your target variable.
-   Don't just create plots; interpret them in markdown cells. What does the plot tell you?

### Modeling
-   Start with a simple baseline model (like Logistic Regression) to set a performance benchmark.
-   Given the nature of the problem (predicting failures), **Recall** and **F1-Score** are likely more important than Accuracy. Think about why.
-   Use `joblib` or `pickle` to save your final, trained model.

### Code
```python
# Set a random seed for reproducibility
import numpy as np
import random
SEED = 42
np.random.seed(SEED)
random.seed(SEED)

# Save your best model
import joblib
joblib.dump(best_model, 'models/best_predictive_model.pkl')

# Save figures for reports
import matplotlib.pyplot as plt
plt.savefig('figures/my_plot.png', dpi=300, bbox_inches='tight')
```

---

## 📚 Resources

-   **Pandas**: [10 Minutes to Pandas](https://pandas.pydata.org/docs/user_guide/10min.html)
-   **Visualization**: [Seaborn Tutorial](https://seaborn.pydata.org/tutorial.html), [Matplotlib Usage Guide](https://matplotlib.org/stable/users/getting_started/)
-   **Scikit-learn**: [Preprocessing Guide](https://scikit-learn.org/stable/modules/preprocessing.html), [Model Evaluation Guide](https://scikit-learn.org/stable/modules/model_evaluation.html)

---

## ✅ Self-Assessment Checklist

Before submitting, ask yourself:
-   [ ] Have I completed all five parts of the assignment?
-   [ ] Does my notebook run from top to bottom without errors?
-   [ ] Is my notebook well-organized with clear headings and explanations?
-   [ ] Are all my visualizations clearly labeled and interpreted?
-   [ ] Have I included a `requirements.txt` file?
-   [ ] Have I written a clear and compelling conclusion with actionable recommendations?

---

<div align="center">
    <h3>Good luck, and we look forward to seeing your analysis!</h3>
</div>