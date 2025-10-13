# ⚡ Quick Start Guide - Gen AI Masters Program

**Ready to start learning? Follow this guide to get up and running in 10 minutes!**

---

## 🚀 Super Quick Start (5 minutes)

### Option A: GitHub Codespaces (Recommended)

1. **Open in Codespaces**
   - Click the green "Code" button → "Codespaces" tab
   - Click "Create codespace on main"
   - Wait 2-3 minutes for setup ☕

2. **Start Learning**
   ```bash
   # Open first notebook
   code week-01-02-python-ml-foundations/01_environment_setup.ipynb
   ```

3. **That's it!** Everything is pre-configured 🎉

### Option B: Local Setup (10 minutes)

```bash
# 1. Clone repository
git clone <your-repo-url>
cd T_Tech

# 2. Create virtual environment
python -m venv venv

# 3. Activate environment
# Windows:
.\venv\Scripts\Activate.ps1
# Linux/Mac:
source venv/bin/activate

# 4. Install packages
pip install -r requirements.txt

# 5. Start Jupyter
jupyter lab
```

---

## 🎯 Your First 30 Minutes

### Step 1: Set Up HuggingFace (5 mins)

1. Go to https://huggingface.co/join
2. Create free account
3. Go to https://huggingface.co/settings/tokens
4. Create new token (Read access)
5. Copy token
6. Add to environment:

**In Codespaces:**
- Repository Settings → Secrets → Codespaces
- Add secret: `HUGGINGFACE_TOKEN`

**Locally:**
```bash
# Create .env file
echo "HUGGINGFACE_TOKEN=your_token_here" > .env
```

### Step 2: Run Your First Model (10 mins)

Open `00_environment_setup.ipynb` and run this:

```python
from transformers import pipeline

# Load sentiment analysis model
classifier = pipeline("sentiment-analysis")

# Test it!
result = classifier("I'm excited to learn Gen AI!")
print(result)
# Output: [{'label': 'POSITIVE', 'score': 0.9998}]
```

**🎉 Congratulations! You just ran your first AI model!**

### Step 3: Review Course Structure (15 mins)

Read these in order:
1. `README.md` - Complete course overview
2. `GETTING_STARTED.md` - Detailed setup guide
3. `week-01-02-python-ml-foundations/README.md` - First module overview

---

## 📅 Week-by-Week Roadmap

### Week 1-2: Foundations ⏳ 15-20 hours
```
Day 1-2: Environment + Python Essentials
Day 3-4: NumPy + Pandas
Day 5-6: Data Preprocessing + ML
Day 7: Homework Assignment
```
**Start with:** `week-01-02-python-ml-foundations/01_environment_setup.ipynb`

### Week 3-4: Deep Learning & Transformers ⏳ 15-20 hours
```
Day 1-2: Neural Networks
Day 3-4: CNNs + RNNs
Day 5-6: Transformers + HuggingFace
Day 7: Homework Assignment
```
**Focus:** Understanding transformer architecture

### Week 5-6: LLMs & RAG ⏳ 15-20 hours
```
Day 1-2: LLMs + HuggingFace Tasks
Day 3-4: Prompt Engineering
Day 5-6: RAG Systems
Day 7: Homework Assignment
```
**Focus:** Building RAG applications

### Week 7-8: Agents & Advanced RAG ⏳ 20-25 hours
```
Day 1-3: LangChain Framework
Day 4-5: Advanced RAG
Day 6-7: LangGraph + Agents
```
**Focus:** Multi-agent systems

### Week 9-10: Training & Fine-tuning ⏳ 15-20 hours
```
Day 1-3: Model Training Concepts
Day 4-6: Fine-tuning (LoRA/QLoRA)
Day 7: Homework Assignment
```
**Focus:** Fine-tuning LLMs

### Week 11-12: Production & Capstone ⏳ 25-30 hours
```
Day 1-2: MLOps + FastAPI
Day 3-4: Docker + Cloud
Day 5-9: Capstone Project
```
**Focus:** Deploying production systems

---

## 🎯 Daily Study Routine

### Recommended Schedule (2-3 hours/day)

**Weekdays:**
```
🌅 Morning (Optional): 30 mins review previous day
🌆 Evening: 2 hours new material
  - 1 hour: Read/watch notebook
  - 45 mins: Code along
  - 15 mins: Notes/review
```

**Weekends:**
```
📚 Saturday: 3-4 hours
  - Complete remaining notebooks
  - Start homework
  
🚀 Sunday: 3-4 hours
  - Finish homework
  - Review week's learning
  - Prepare for next week
```

---

## ✅ Daily Checklist

Copy this to your notes app:

```markdown
### Today's Learning Session

**Date:** ___________  
**Week:** ___________  
**Notebook:** ___________

- [ ] Read notebook introduction
- [ ] Run all cells
- [ ] Understand key concepts
- [ ] Modify examples
- [ ] Add notes
- [ ] Commit to GitHub
- [ ] Update progress tracker

**Time spent:** _____ hours  
**Key learnings:**
- 
- 
- 

**Questions:**
- 
- 
```

---

## 🛠️ Essential Tools

### Must-Have
- ✅ GitHub account
- ✅ HuggingFace account
- ✅ Text editor (VS Code in Codespaces)
- ✅ Jupyter Lab

### Nice-to-Have
- 📝 Notion/Obsidian for notes
- 💬 ChatGPT for questions
- 🐙 GitHub Desktop (local)
- 📊 Excalidraw for diagrams

---

## 🎓 Learning Resources

### Keep These Tabs Open
- [HuggingFace Docs](https://huggingface.co/docs)
- [LangChain Docs](https://python.langchain.com/)
- [Course README](./README.md)
- [Progress Tracker](./PROGRESS_TRACKER.md)

### For When You're Stuck
- [FAQ](./FAQ.md)
- [GitHub Discussions](#)
- [Stack Overflow](https://stackoverflow.com/)
- Course community

---

## 💡 Success Tips

### DO:
- ✅ Code along, don't just read
- ✅ Make mistakes and learn
- ✅ Ask questions early
- ✅ Track your progress
- ✅ Celebrate small wins
- ✅ Share your learnings

### DON'T:
- ❌ Skip the basics
- ❌ Copy-paste without understanding
- ❌ Compare your pace with others
- ❌ Aim for perfection
- ❌ Give up when stuck
- ❌ Study for hours without breaks

---

## 🆘 Quick Troubleshooting

### Import errors?
```bash
pip install --upgrade pip
pip install -r requirements.txt
```

### HuggingFace token issues?
```python
from huggingface_hub import login
login()  # Paste your token
```

### Jupyter not starting?
```bash
pip install --upgrade jupyter jupyterlab
jupyter lab
```

### Out of memory?
Use HuggingFace Inference API (we teach this in Week 3!)

---

## 📊 Tracking Progress

### Use These Files
1. **PROGRESS_TRACKER.md** - Check off completed notebooks
2. **Personal notes** - Add to each notebook
3. **GitHub commits** - Commit after each notebook
4. **Homework folder** - Organize submissions

### Git Workflow
```bash
# After completing a notebook
git add .
git commit -m "Complete week-01-02/01_environment_setup.ipynb"
git push

# Create branch for homework
git checkout -b homework-week-01
# ... work on homework ...
git add .
git commit -m "Complete Week 1-2 homework"
git push
```

---

## 🎯 Milestones

### Week 2: First Milestone 🎉
- [ ] Completed 5 notebooks
- [ ] Submitted homework
- [ ] Passed Checkpoint 1
- [ ] Updated portfolio

### Week 4: Deep Learning 🧠
- [ ] Built a transformer
- [ ] Used HuggingFace models
- [ ] Completed text classification

### Week 6: RAG Master 📚
- [ ] Built RAG application
- [ ] Deployed locally
- [ ] Passed Checkpoint 3

### Week 8: Agent Creator 🤖
- [ ] Built multi-agent system
- [ ] Implemented tools
- [ ] Advanced RAG patterns

### Week 10: Fine-tuning Expert 🎯
- [ ] Fine-tuned a model
- [ ] Evaluated performance
- [ ] Passed Checkpoint 5

### Week 12: Gen AI Master 🚀
- [ ] Deployed capstone
- [ ] Production-ready
- [ ] Portfolio complete

---

## 🎊 Ready to Start?

**Your next steps:**

1. ⭐ **Star this repository**
2. 📖 **Read** the main [README.md](./README.md)
3. ⚙️ **Complete** `00_environment_setup.ipynb`
4. 🚀 **Begin** with Week 1-2 notebooks
5. 📊 **Track** progress in [PROGRESS_TRACKER.md](./PROGRESS_TRACKER.md)

---

## 📞 Need Help?

- 🐛 **Technical issues:** Open GitHub Issue
- 💬 **Questions:** GitHub Discussions
- 📚 **Concepts:** Check [FAQ.md](./FAQ.md)
- 🤝 **Community:** Join Discord/Slack

---

## 🌟 Remember

> "The journey of a thousand miles begins with a single step."  
> — Lao Tzu

You're about to learn cutting-edge AI technology. Take it one notebook at a time, stay curious, and enjoy the journey!

**Let's build something amazing together! 🚀**

---

<div align="center">

**Quick Start Guide** | Gen AI Masters Program | October 2025

[🏠 Home](./README.md) | [📚 Getting Started](./GETTING_STARTED.md) | [❓ FAQ](./FAQ.md) | [📊 Progress](./PROGRESS_TRACKER.md)

</div>
