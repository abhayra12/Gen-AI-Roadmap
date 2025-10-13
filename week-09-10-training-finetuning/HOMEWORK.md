# 📝 Homework Assignment - Week 9-10

**Module:** Model Training & Fine-tuning  
**Due:** End of Week 10  
**Points:** 100

---

## 🎯 Assignment: Fine-tune LLM for Manufacturing Domain

Fine-tune a language model to understand manufacturing terminology and generate technical reports.

---

## 📊 Project Requirements

### Dataset Creation
Create or curate dataset with:
- 5000+ manufacturing text samples
- Technical documentation
- Maintenance logs
- Quality reports
- Equipment manuals

### Fine-tuning Tasks
1. **Task 1**: Domain-specific language understanding
2. **Task 2**: Technical report generation
3. **Task 3**: Manufacturing Q&A

---

## 📋 Task Breakdown

### Part 1: Dataset Preparation (20 points)
- Collect domain-specific data
- Clean and format text
- Create instruction-following format
- Split train/val/test
- Document data sources

### Part 2: Base Model Selection (10 points)
- Research suitable base models
- Consider size and capabilities
- Test baseline performance
- Justify selection

### Part 3: Fine-tuning Implementation (35 points)
- Implement LoRA fine-tuning
- Configure hyperparameters
- Track training metrics
- Use gradient accumulation
- Implement early stopping
- Save checkpoints

### Part 4: Evaluation (25 points)
- Quantitative metrics (perplexity, BLEU, ROUGE)
- Qualitative analysis
- Compare with base model
- Test on held-out data
- Domain expert evaluation (if possible)

### Part 5: Deployment (10 points)
- Create inference endpoint
- Optimize for latency
- Test with new samples
- Document API usage

---

## 💡 Implementation Guide

### Dataset Format
```json
{
  "instruction": "Generate a maintenance report for motor failure",
  "input": "Motor ID: M-123, Failure type: Bearing wear",
  "output": "Maintenance Report...[detailed report]"
}
```

### Fine-tuning Script
```python
from transformers import AutoModelForCausalLM, AutoTokenizer, Trainer
from peft import LoraConfig, get_peft_model

# Load base model
model = AutoModelForCausalLM.from_pretrained("mistralai/Mistral-7B-v0.1")
tokenizer = AutoTokenizer.from_pretrained("mistralai/Mistral-7B-v0.1")

# Configure LoRA
lora_config = LoraConfig(
    r=16,
    lora_alpha=32,
    target_modules=["q_proj", "v_proj"],
    lora_dropout=0.05,
    bias="none",
    task_type="CAUSAL_LM"
)

model = get_peft_model(model, lora_config)

# Train
trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=train_dataset,
    eval_dataset=eval_dataset,
)

trainer.train()
```

### Evaluation
```python
from evaluate import load

# Perplexity
perplexity = model.eval_perplexity(test_data)

# BLEU/ROUGE for generation
bleu = load("bleu")
rouge = load("rouge")

predictions = model.generate(test_inputs)
bleu_score = bleu.compute(predictions=predictions, references=references)
rouge_score = rouge.compute(predictions=predictions, references=references)
```

---

## 🎯 Grading Rubric

| Component | Points | Criteria |
|-----------|--------|----------|
| Dataset Preparation | 20 | Quality and relevance of data |
| Model Selection | 10 | Justified choice with baseline |
| Fine-tuning | 35 | Proper implementation and optimization |
| Evaluation | 25 | Comprehensive metrics and analysis |
| Deployment | 10 | Working inference endpoint |

---

## 🚀 Bonus Challenges (+10 points each)

1. **QLoRA**: Implement 4-bit quantization
2. **Multi-task**: Fine-tune for multiple tasks simultaneously
3. **Distributed Training**: Use multiple GPUs
4. **Instruction Tuning**: Create instruction-following model
5. **Benchmark**: Compare on standard benchmarks

---

## 📦 Submission Structure

```
homework/week-09-10/
├── README.md
├── finetuning_pipeline.ipynb
├── requirements.txt
├── data/
│   ├── train.jsonl
│   ├── val.jsonl
│   └── test.jsonl
├── scripts/
│   ├── prepare_data.py
│   ├── train.py
│   └── evaluate.py
├── models/
│   └── finetuned_model/
├── configs/
│   └── lora_config.yaml
└── reports/
    ├── training_log.txt
    ├── evaluation_results.md
    └── comparison_baseline.md
```

---

## ✅ Submission Checklist

- [ ] Dataset created and documented
- [ ] Fine-tuning completed successfully
- [ ] Evaluation comprehensive
- [ ] Improvement over baseline shown
- [ ] Inference endpoint working
- [ ] Code documented
- [ ] README comprehensive
- [ ] Committed to GitHub

---

<div align="center">
Week 9-10 Homework | LLM Fine-tuning | Adapt models to your domain! 🎯
</div>
