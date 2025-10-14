# 📝 Homework Assignment - Week 9-10: Specialize the Manufacturing Copilot

**Module:** Model Training & Fine-Tuning for the Factory Floor  
**Due:** End of Week 10  
**Points:** 100

---

## 🎯 Assignment: Fine-Tune a Core LLM for the Manufacturing Copilot

Your goal is to take a powerful, general-purpose Large Language Model (LLM) and specialize it to become the core intelligence of our **Manufacturing Copilot**. This involves fine-tuning it on domain-specific data so it can understand the unique language of your factory and assist with critical operational tasks.

---

## 📊 Project Requirements

### Dataset Curation
Assemble a high-quality dataset that reflects the day-to-day operations of a manufacturing plant. The dataset must contain at least 5,000 text samples, including:
- **Technical Documentation:** Schematics, standard operating procedures (SOPs).
- **Maintenance Logs:** Records of machine repairs, component replacements, and technician notes.
- **Quality Control Reports:** Defect descriptions, inspection results, and pass/fail records.
- **Equipment Manuals:** Operating instructions and safety warnings for machinery.

### Fine-Tuning Tasks
You will fine-tune the model to excel at three core competencies for the Manufacturing Copilot:
1.  **Domain-Specific Language Understanding:** Accurately interpret jargon, acronyms, and technical terms used on the factory floor.
2.  **Technical Report Generation:** Automatically draft maintenance reports, shift summaries, or incident analyses based on structured input.
3.  **Manufacturing Q&A:** Answer complex questions about machine operations, troubleshooting procedures, and quality standards.

---

## 📋 Task Breakdown

### Part 1: Dataset Preparation (20 points)
- **Collect & Curate:** Gather text data from various manufacturing sources.
- **Clean & Format:** Pre-process the text to remove noise and structure it for training.
- **Instruction Formatting:** Convert the data into an instruction-following format (e.g., JSONL with "instruction", "input", "output" keys).
- **Split & Document:** Divide the data into training, validation, and test sets. Document your data sources and any pre-processing steps.

### Part 2: Base Model Selection (10 points)
- **Research:** Investigate and select a suitable pre-trained base model (e.g., from the Mistral, Llama, or other open-source families).
- **Justify:** Write a brief justification for your choice, considering model size, performance, and suitability for the manufacturing domain.
- **Baseline:** Test the *un-tuned* base model on a few sample prompts to establish a performance baseline.

### Part 3: Fine-Tuning Implementation (35 points)
- **LoRA Implementation:** Implement the LoRA (Low-Rank Adaptation) technique for efficient fine-tuning.
- **Configuration:** Carefully configure hyperparameters (learning rate, rank, alpha).
- **Training & Monitoring:** Track training metrics (loss, accuracy) using tools like TensorBoard or W&B. Use techniques like gradient accumulation and early stopping to optimize the training process.
- **Save Artifacts:** Save the final trained LoRA adapter weights.

### Part 4: Evaluation (25 points)
- **Quantitative Metrics:** Measure performance using perplexity for language modeling and BLEU/ROUGE scores for report generation tasks.
- **Qualitative Analysis:** Manually review model outputs for clarity, accuracy, and relevance to the manufacturing context.
- **Comparison:** Compare the fine-tuned model’s performance against the baseline to demonstrate improvement.
- **Hold-out Test:** Evaluate the final model on the held-out test set.

### Part 5: Mock Deployment & Inference (10 points)
- **Inference Script:** Create a Python script that loads the base model and the trained LoRA adapter to run inference on new, unseen prompts.
- **API Documentation:** Document how to use your inference script with clear examples relevant to the Manufacturing Copilot.

---

## 💡 Implementation Guide

### Recommended Dataset Format
```json
{
  "instruction": "Generate a maintenance report for a CNC machine motor failure.",
  "input": "Machine ID: CNC-4B, Motor ID: M-123, Failure Type: Bearing wear, Technician Notes: Excessive vibration reported during morning shift.",
  "output": "Maintenance Report\nDate: [Current Date]\nMachine ID: CNC-4B\nMotor ID: M-123\nIssue: Motor failure due to excessive bearing wear.\nDescription: The primary drive motor failed inspection following reports of excessive vibration. A full diagnostic confirmed that the main bearings have seized. \nAction Taken: The motor has been decommissioned and replaced. The replacement motor (ID: M-124) was installed and calibrated. \nRecommendation: Schedule a vibration analysis for all similar CNC machines within the next 30 days."
}
```

### Fine-Tuning with PEFT
```python
from transformers import AutoModelForCausalLM, AutoTokenizer, Trainer, TrainingArguments, DataCollatorForLanguageModeling
from peft import LoraConfig, get_peft_model
from datasets import load_dataset

# 1. Load Base Model & Tokenizer
base_model_id = "mistralai/Mistral-7B-v0.1"
model = AutoModelForCausalLM.from_pretrained(base_model_id)
tokenizer = AutoTokenizer.from_pretrained(base_model_id)

# --- Add a padding token ---
# Models like Mistral don't have a default padding token.
# We'll use the end-of-sentence token for padding to avoid errors in batching.
if tokenizer.pad_token is None:
    tokenizer.pad_token = tokenizer.eos_token

# 2. Configure LoRA
lora_config = LoraConfig(
    r=16,
    lora_alpha=32,
    target_modules=["q_proj", "v_proj"], # Target attention blocks
    lora_dropout=0.05,
    bias="none",
    task_type="CAUSAL_LM"
)

# 3. Add LoRA adapter to the model
model = get_peft_model(model, lora_config)
# It's good practice to disable caching for training
model.config.use_cache = False 

# 4. Load your manufacturing dataset
# Ensure your JSONL files are in the correct path
train_dataset = load_dataset("json", data_files="data/train.jsonl", split="train")
eval_dataset = load_dataset("json", data_files="data/val.jsonl", split="train")

# 5. Set up Trainer
training_args = TrainingArguments(
    output_dir="./results",
    per_device_train_batch_size=4,
    gradient_accumulation_steps=4,
    learning_rate=2e-4,
    num_train_epochs=3,
    logging_steps=10,
    save_steps=50,
    evaluation_strategy="steps",
    eval_steps=50,
    load_best_model_at_end=True,
    report_to="none", # Can be "wandb" or "tensorboard"
)

# The data collator handles batching and padding
data_collator = DataCollatorForLanguageModeling(tokenizer, mlm=False)

trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=train_dataset,
    eval_dataset=eval_dataset,
    data_collator=data_collator,
)

# 6. Train!
trainer.train()

# 7. Save the final adapter
model.save_pretrained("./final_adapter")
```

---

## 🎯 Grading Rubric

| Component | Points | Criteria |
|---|---|---|
| **Dataset Preparation** | 20 | Quality, relevance, and documentation of the manufacturing data. |
| **Model Selection** | 10 | Well-justified choice with a clear baseline performance assessment. |
| **Fine-Tuning** | 35 | Correct implementation of LoRA, good hyperparameter choices, and clear training process. |
| **Evaluation** | 25 | Comprehensive quantitative and qualitative analysis showing clear improvement. |
| **Deployment** | 10 | A working, well-documented inference script. |

---

## 🚀 Bonus Challenges (+10 points each)

1.  **QLoRA Fine-Tuning:** Implement fine-tuning using 4-bit quantization (QLoRA) to reduce memory footprint.
2.  **Distributed Training:** If you have access to multiple GPUs, adapt your script for distributed training.
3.  **Advanced Evaluation:** Create a small, human-curated test set of challenging manufacturing scenarios and evaluate your model's performance on it.

---

## 📦 Submission Structure

Your submission should be a well-organized Git repository with the following structure:

```
manufacturing-copilot-finetune/
├── README.md                # High-level project overview and results
├── finetuning_notebook.ipynb  # Your main notebook for experimentation
├── requirements.txt         # Project dependencies
├── data/
│   ├── train.jsonl
│   ├── val.jsonl
│   └── test.jsonl
├── scripts/
│   ├── train.py             # (Optional) Standalone training script
│   └── evaluate.py          # (Optional) Standalone evaluation script
└── reports/
    └── evaluation_summary.md  # Detailed analysis of your results
```

---

## ✅ Submission Checklist

- [ ] The curated dataset is clean, well-documented, and relevant.
- [ ] The fine-tuning process completes successfully.
- [ ] The evaluation report is thorough and demonstrates clear improvement over the baseline.
- [ ] The inference script works correctly on new prompts.
- [ ] The code is well-commented and the `README.md` is comprehensive.
- [ ] The entire project is committed to your Git repository.

---

<div align="center">
Week 9-10 Homework | Fine-Tuning the Manufacturing Copilot | From Generalist to Specialist 🏭
</div>
