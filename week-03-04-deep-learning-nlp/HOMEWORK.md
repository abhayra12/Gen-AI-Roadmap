# 📝 Homework Assignment - Week 3-4

**Module:** Deep Learning & NLP Foundations  
**Due:** End of Week 4  
**Points:** 100

---

## 🎯 Assignment: Manufacturing Document Classifier for Copilot

**Objective:** Build a robust text classification system using transformers to automatically categorize documents from a manufacturing environment. This classifier will be a core component of our Manufacturing Copilot, helping it understand and route information efficiently.

---

## 📊 Project Requirements

### Task: Maintenance Log Severity Classification

Your task is to build a multi-class text classifier that categorizes maintenance logs into one of three severity levels: **Normal**, **Warning**, or **Critical**.

- **Dataset:** You will create a synthetic dataset of at least 100 maintenance log entries. Each entry should be a realistic sentence or short paragraph describing a factory event.
- **Classes:**
    - `Normal (0)`: Routine operations, scheduled maintenance, successful checks.
    - `Warning (1)`: Minor deviations, potential issues, observations requiring monitoring.
    - `Critical (2)`: System failures, safety alerts, production stoppages.

---

## 📋 Deliverables

### Part 1: Data Preparation (20 points)
- Create a synthetic dataset of at least 100 samples in a CSV or JSON file.
- Ensure a reasonable balance between the three classes.
- Split the data into training, validation, and test sets (e.g., 70/15/15 split).
- Load the data using HuggingFace `datasets` or PyTorch `Dataset`.

### Part 2: Model Selection & Fine-tuning (35 points)
- Choose a suitable pre-trained model from the HuggingFace Hub (e.g., `distilbert-base-uncased`, `bert-base-uncased`). Justify your choice.
- Fine-tune the model on your training dataset using the `Trainer` API.
- Implement a `compute_metrics` function to track accuracy during evaluation.
- Save the best-performing model checkpoint.

### Part 3: Evaluation (25 points)
- Evaluate the fine-tuned model on the test set.
- Report key metrics: accuracy, precision, recall, and F1-score (macro-averaged).
- Generate and display a confusion matrix to visualize model performance.
- Conduct an error analysis: identify a few examples where the model failed and hypothesize why.

### Part 4: Inference & Deployment (20 points)
- Create a simple inference pipeline using the fine-tuned model.
- Write a script or function that takes a new, unseen maintenance log as input and outputs the predicted severity.
- (Optional but Recommended) Build a simple web interface using Gradio or Streamlit to demonstrate your classifier.

---

## 🎯 Grading Rubric

| Component | Excellent (90-100%) | Good (80-89%) | Satisfactory (70-79%) | Needs Work (<70%) |
|-----------|-------------------|---------------|---------------------|------------------|
| **Data Preparation** | High-quality, realistic, well-balanced data. | Good data, minor balance issues. | Basic dataset, some unrealistic samples. | Incomplete or poorly formatted data. |
| **Model Fine-tuning** | Optimal model choice and training process. | Good training, minor hyperparameter issues. | Basic training completed. | Model does not train or converge. |
| **Evaluation** | Comprehensive metrics and insightful error analysis. | Good metrics, basic error analysis. | Basic metrics reported. | Incomplete or missing evaluation. |
| **Inference** | Clean, functional inference script/demo. | Working inference script. | Basic script with minor bugs. | Non-functional inference. |

---

## 📦 Submission Structure

Organize your project in a clean, readable format.

```
homework/week-03-04/
├── README.md                 # Project overview, instructions to run
├── maintenance_classifier.ipynb # Your main notebook
├── requirements.txt          # Required packages
├── data/
│   └── maintenance_logs.csv    # Your synthetic dataset
└── saved_model/                # Your fine-tuned model files
```

---

## 💡 Implementation Tips

### Data Creation
```python
import pandas as pd

data = {
    'text': [
        'Routine lubrication of conveyor belt completed.',
        'Slight increase in motor temperature observed on Line 2.',
        'Emergency shutdown of hydraulic press due to pressure loss.'
        # ... more samples
    ],
    'label': [0, 1, 2] # 0:Normal, 1:Warning, 2:Critical
}
df = pd.DataFrame(data)
df.to_csv('data/maintenance_logs.csv', index=False)
```

### Model Fine-tuning
```python
from transformers import AutoModelForSequenceClassification, Trainer, TrainingArguments
from datasets import load_dataset

# Load your data
dataset = load_dataset('csv', data_files='data/maintenance_logs.csv')

# ... (tokenize and split data) ...

model = AutoModelForSequenceClassification.from_pretrained(
    "distilbert-base-uncased",
    num_labels=3
)

training_args = TrainingArguments(...)

trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=tokenized_train_dataset,
    eval_dataset=tokenized_val_dataset,
    compute_metrics=compute_metrics
)
trainer.train()
```

### Inference
```python
from transformers import pipeline

classifier = pipeline(
    "text-classification",
    model="./saved_model"
)

new_log = "Vibration levels on the main pump are exceeding the upper threshold."
result = classifier(new_log)
print(result)
```

---

## ✅ Submission Checklist

- [ ] All code runs without errors.
- [ ] The `README.md` file is clear and provides instructions.
- [ ] The model achieves a reasonable accuracy on the test set (>75% is a good target).
- [ ] The inference script correctly classifies new logs.
- [ ] The code is well-commented and easy to understand.
- [ ] The project is committed to your GitHub repository.

---

**Due Date:** End of Week 4  
**Submit via:** GitHub repository link.

<div align="center">
Good luck building your Manufacturing Copilot component! 🏭🤖
</div>
