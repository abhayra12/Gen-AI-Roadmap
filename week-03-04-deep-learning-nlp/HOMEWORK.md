# 📝 Homework Assignment - Week 3-4

**Module:** Deep Learning & NLP Foundations  
**Due:** End of Week 4  
**Points:** 100

---

## 🎯 Assignment: Multi-lingual Text Classifier

Build a production-ready text classification system using transformers and HuggingFace.

---

## 📊 Project Requirements

### Task Options (Choose One)

**Option 1: Sentiment Analysis**
- Multi-lingual product reviews
- Classify: Positive/Negative/Neutral
- Support: English, Hindi, Tamil

**Option 2: Topic Classification**
- News article categorization
- Categories: Business, Tech, Sports, Entertainment
- Multi-label classification

**Option 3: Language Detection**
- Identify language of text
- Support 10+ Indian languages
- Handle code-mixed text

---

## 📋 Deliverables

### Part 1: Data Preparation (20 points)
- Collect or use existing dataset (min 5000 samples)
- Clean and preprocess text
- Split train/val/test (70/15/15)
- Handle class imbalance
- Create data loaders

### Part 2: Model Selection (15 points)
- Research suitable HuggingFace models
- Compare 3+ models on validation set
- Document selection criteria
- Justify final choice

### Part 3: Fine-tuning (30 points)
- Fine-tune selected model
- Track training metrics
- Implement early stopping
- Save best model
- Document hyperparameters

### Part 4: Evaluation (20 points)
- Comprehensive metrics (accuracy, F1, precision, recall)
- Confusion matrix
- Error analysis
- Performance by class
- Comparison with baseline

### Part 5: Deployment (15 points)
- Create inference script
- Build simple API (FastAPI)
- Test with new examples
- Document usage
- Provide demo

---

## 🎯 Grading Rubric

| Component | Excellent (90-100%) | Good (80-89%) | Satisfactory (70-79%) | Needs Work (<70%) |
|-----------|-------------------|---------------|---------------------|------------------|
| **Data Preparation** | Clean, well-documented, balanced | Minor issues, good docs | Basic preparation | Significant issues |
| **Model Selection** | Thorough comparison, justified | Good comparison | Basic justification | Poor selection process |
| **Fine-tuning** | Optimal hyperparameters, tracked | Good training, some tracking | Basic training | Poor training |
| **Evaluation** | Comprehensive analysis | Good metrics | Basic evaluation | Incomplete |
| **Deployment** | Production-ready API | Working API | Basic script | Non-functional |

---

## 📦 Submission Structure

```
homework/week-03-04/
├── README.md
├── text_classifier.ipynb
├── requirements.txt
├── data/
│   ├── train.csv
│   ├── val.csv
│   └── test.csv
├── models/
│   └── best_model/
├── src/
│   ├── data_prep.py
│   ├── train.py
│   └── inference.py
├── api/
│   └── app.py
└── reports/
    ├── model_comparison.md
    └── evaluation_report.md
```

---

## 💡 Implementation Tips

### Data Collection
```python
# Use HuggingFace datasets
from datasets import load_dataset

dataset = load_dataset("imdb")  # Example
# Or create custom dataset
```

### Model Fine-tuning
```python
from transformers import AutoModelForSequenceClassification, Trainer

model = AutoModelForSequenceClassification.from_pretrained(
    "bert-base-multilingual-cased",
    num_labels=3
)

trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=train_dataset,
    eval_dataset=val_dataset
)
```

### API Example
```python
from fastapi import FastAPI
from transformers import pipeline

app = FastAPI()
classifier = pipeline("text-classification", model="./models/best_model")

@app.post("/classify")
def classify_text(text: str):
    result = classifier(text)
    return {"prediction": result}
```

---

## 🚀 Bonus Challenges (+10 points each)

1. **Multi-lingual Support**: Handle 5+ languages
2. **Ensemble Model**: Combine multiple models
3. **Attention Visualization**: Show what model focuses on
4. **Real-time API**: Deploy to cloud with <100ms latency
5. **Mobile Optimization**: Quantize model for mobile deployment

---

## ✅ Submission Checklist

- [ ] All code runs without errors
- [ ] README is comprehensive
- [ ] Model achieves >80% accuracy
- [ ] API is functional
- [ ] Evaluation report is detailed
- [ ] Code is well-commented
- [ ] Committed to GitHub
- [ ] Updated progress tracker

---

**Due Date:** End of Week 4  
**Submit via:** GitHub repository

<div align="center">
Week 3-4 Homework | Text Classification with Transformers 🤖
</div>
