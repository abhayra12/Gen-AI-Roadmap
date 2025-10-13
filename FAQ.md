# FAQ - Frequently Asked Questions

## 📚 General Questions

### Q: Do I need prior ML/AI experience?
**A:** Basic Python knowledge is recommended, but Week 1-2 covers all fundamentals. If you're completely new to Python, spend extra time on those weeks.

### Q: How much time should I dedicate per week?
**A:** Plan for **15-20 hours/week:**
- Watching/reading: 5-7 hours
- Coding along: 5-7 hours
- Homework: 3-4 hours
- Review: 2-3 hours

### Q: Can I complete this faster than 12 weeks?
**A:** Yes! The structure is flexible. You can accelerate if you have more time. However, don't rush the capstone project.

### Q: What if I fall behind?
**A:** That's okay! The material stays available. Focus on understanding over speed. Skip optional sections if needed.

---

## 🛠️ Technical Setup

### Q: Should I use Codespaces or local setup?
**A:** **Codespaces is recommended** for:
- Zero setup hassle
- Consistent environment
- Works on any device
- 60 free hours/month

Use local setup if:
- You have a powerful GPU
- You prefer working offline
- You want more control

### Q: Do I need a GPU?
**A:** **No!** We use HuggingFace Inference API, which runs models in the cloud. A basic laptop is sufficient.

### Q: What if HuggingFace rate limits me?
**A:** Free tier is generous. If you hit limits:
1. Wait a few minutes (limits reset)
2. Use caching (we'll show you how)
3. Consider HF Pro ($9/month) for heavy usage

### Q: I'm getting installation errors. Help!
**A:** Common fixes:
```bash
# Update pip first
pip install --upgrade pip setuptools wheel

# Install one package at a time to identify issues
pip install transformers
pip install langchain
# etc.

# Use conda if pip fails (optional)
conda install -c conda-forge transformers
```

---

## 📖 Course Content

### Q: Why start with Python/ML basics?
**A:** Strong foundations are crucial. Even if you know Python, the ML review ensures everyone starts on the same page. You can skim if you're experienced.

### Q: Can I skip notebooks?
**A:** **Not recommended.** Each builds on previous ones. If you must skip:
- Complete all checkpoints
- Review code in skipped notebooks
- Test your understanding

### Q: Are there video lectures?
**A:** This is a **hands-on, code-first** course. Each notebook contains:
- Theory explanations
- Code examples
- Practice exercises
- External resource links

### Q: Where can I find additional resources?
**A:** Each notebook links to:
- Official documentation
- Research papers
- Video tutorials
- Blog posts

---

## 🤔 Learning & Practice

### Q: I don't understand a concept. What should I do?
**A:** 
1. **Re-read** the notebook section
2. **Google** the concept
3. **Ask** in GitHub Discussions
4. **Review** linked resources
5. **Experiment** with the code

### Q: How do I know if I truly understand?
**A:** You should be able to:
- Explain it to someone else
- Modify the code successfully
- Complete homework without looking at solutions
- Pass checkpoint assessments

### Q: Should I take notes?
**A:** **Yes!** The PROGRESS_TRACKER.md has a notes section. Also:
- Add markdown cells in notebooks
- Create a personal wiki
- Write blog posts (great for portfolio!)

---

## 📝 Homework & Assessments

### Q: How are homework assignments graded?
**A:** This is **self-paced**. Evaluate yourself using provided rubrics. Focus on learning, not grades.

### Q: Can I use ChatGPT/Copilot for homework?
**A:** **Use wisely:**
- ✅ Use for understanding concepts
- ✅ Use for debugging
- ✅ Use for code suggestions
- ❌ Don't copy-paste entire solutions
- ❌ Don't skip understanding

The goal is **learning**, not completion.

### Q: Where do I submit homework?
**A:** Create a `homework/` directory in your repo. Organize by week. This becomes part of your portfolio!

### Q: I'm stuck on homework. Can I see solutions?
**A:** **Try these first:**
1. Review relevant notebook
2. Check documentation
3. Search GitHub for similar projects
4. Ask in Discussions (without sharing full solution)
5. Move on and return later

---

## 🏗️ Capstone Project

### Q: Can I choose a different domain?
**A:** **Yes!** The manufacturing example is a template. Adapt to:
- Healthcare (medical image analysis)
- Finance (document processing)
- Agriculture (crop disease detection)
- Retail (customer service bot)

Keep the same **technical stack** and **production setup**.

### Q: Can I work in a team?
**A:** Capstone is designed for **individual work** to showcase your skills. However, you can:
- Pair program for learning
- Review each other's code
- Share infrastructure costs

### Q: How detailed should the capstone be?
**A:** Aim for **MVP (Minimum Viable Product)**:
- Core features working
- Deployed and accessible
- Basic monitoring
- Clean code

Don't over-engineer! Focus on demonstrating key skills.

### Q: What if I can't afford GCP costs?
**A:** 
- GCP free tier covers most needs
- Total cost: $5-15 for the project
- Alternatives: Fly.io, Railway, Render (free tiers)
- Local Docker deployment is also acceptable

---

## 🐛 Troubleshooting

### Q: My Jupyter kernel keeps dying
**A:** Common causes:
1. **Out of memory:** Use HF endpoints instead of loading models locally
2. **Infinite loop:** Check your code
3. **Package conflicts:** Create fresh environment

```bash
# Reset kernel
# In Jupyter: Kernel → Restart

# Or recreate environment
pip install --upgrade --force-reinstall jupyter
```

### Q: Import errors for packages
**A:**
```bash
# Verify installation
pip list | grep package_name

# Reinstall specific package
pip install --upgrade --force-reinstall package_name

# Check Python version
python --version  # Should be 3.10+
```

### Q: HuggingFace authentication fails
**A:**
```python
# Re-login
from huggingface_hub import login
login()  # Enter your token when prompted

# Or set environment variable
import os
os.environ["HUGGINGFACE_TOKEN"] = "your_token"

# Verify
from huggingface_hub import whoami
print(whoami())
```

### Q: Docker container won't start
**A:**
```bash
# Check logs
docker logs container_name

# Common fixes:
# 1. Port already in use
docker ps  # Check running containers
# Change port in docker-compose.yml

# 2. Permission issues
# Run with sudo (Linux) or check Docker Desktop (Windows/Mac)

# 3. Build from scratch
docker-compose down -v
docker-compose build --no-cache
docker-compose up
```

---

## 💼 Career & Portfolio

### Q: Is this enough to get a Gen AI job?
**A:** This course provides **strong foundations**. To maximize chances:
- ✅ Complete capstone with clean code
- ✅ Write blog posts about your learnings
- ✅ Contribute to open-source projects
- ✅ Network on LinkedIn/Twitter
- ✅ Keep learning (AI evolves fast!)

### Q: How do I showcase this on my resume?
**A:** 
**Resume:**
- Add "Gen AI Masters Program" to Education/Courses
- List key skills (LLMs, RAG, LangChain, etc.)
- Highlight capstone in Projects section

**LinkedIn:**
- Update headline: "AI Engineer | Gen AI Specialist"
- Add skills with endorsements
- Share project posts
- List certifications/courses

**GitHub:**
- Pin capstone repository
- Write detailed README with demo
- Add GIFs/screenshots
- Include live demo link

### Q: Should I get certified?
**A:** This course doesn't provide formal certification, but:
- Your **GitHub portfolio** is more valuable
- Consider: AWS ML Specialty, GCP ML Engineer
- HuggingFace has free courses with certificates

---

## 🌍 Community & Support

### Q: Where can I ask questions?
**A:** 
1. **GitHub Discussions:** General questions
2. **GitHub Issues:** Bug reports, technical problems
3. **Discord/Slack:** Real-time chat (if available)
4. **LinkedIn/Twitter:** Share progress, network

### Q: Can I contribute to the course?
**A:** **Absolutely!** Ways to contribute:
- Fix typos/errors (PRs welcome)
- Add examples
- Improve explanations
- Share your capstone as inspiration
- Help others in Discussions

### Q: How do I stay updated?
**A:** 
- ⭐ Star the repo for updates
- Watch repo for notifications
- Follow on Twitter/LinkedIn
- Check CHANGELOG for updates

---

## 🔮 What's Next After This Course?

### Advanced Topics to Explore
1. **Advanced Fine-tuning:** RLHF, DPO
2. **Multi-modal Models:** CLIP, Flamingo
3. **Agent Frameworks:** AutoGPT, BabyAGI
4. **Model Optimization:** Quantization, Pruning
5. **Edge Deployment:** ONNX, TensorFlow Lite

### Recommended Next Courses
- **LangChain Academy:** Advanced agent patterns
- **Fast.ai:** Practical Deep Learning
- **HuggingFace:** Advanced NLP
- **AWS/GCP ML Courses:** Cloud ML engineering

### Staying Current
- Follow: Andrej Karpathy, Sebastian Raschka, Chip Huyen
- Read: Arxiv papers, HuggingFace blog, OpenAI blog
- Podcasts: Practical AI, TWIML, Gradient Dissent
- Communities: Reddit r/MachineLearning, Discord servers

---

## 🎯 Tips for Success

### Time Management
- **Block time:** Schedule consistent study hours
- **Pomodoro:** 25 min focus, 5 min break
- **Weekend projects:** Dedicate Saturdays to homework
- **Daily review:** 15 mins reviewing previous day

### Learning Strategies
- **Active recall:** Close notebook, explain concept
- **Spaced repetition:** Review Week 1 in Week 3, Week 5
- **Teaching:** Explain to friend/blog/video
- **Project-based:** Apply immediately to mini-projects

### Avoiding Burnout
- Take breaks between notebooks
- Don't compare pace with others
- Celebrate small wins
- It's okay to not understand everything immediately
- Sleep > Cramming

---

## 🆘 Still Have Questions?

**Can't find your answer?**
1. Search existing GitHub Issues/Discussions
2. Check course documentation
3. Google the error message
4. Ask in GitHub Discussions (we're here to help!)

**For urgent technical issues:**
Open a GitHub Issue with:
- Clear description
- Error message
- What you've already tried
- Your environment (OS, Python version, etc.)

---

## 📧 Contact

- **GitHub Discussions:** [Link to discussions]
- **Email:** [Support email if applicable]
- **Discord:** [Community link if available]

---

**Remember:** There are no stupid questions. We're all learning together! 🚀

---

<div align="center">
Last Updated: October 2025 | Have a question not listed? Open an Issue!
</div>
