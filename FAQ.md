# ❓ Frequently Asked Questions (FAQ)

This document answers common questions about the Gen AI Masters Program.

---

## 📚 General Course Questions

<details>
<summary><b>Do I need prior AI/ML experience?</b></summary>
Basic Python knowledge is helpful, but not strictly required. The first module (Weeks 1-2) is designed to build a strong foundation in Python and classical machine learning, ensuring everyone starts on the same page.
</details>

<details>
<summary><b>How much time should I dedicate each week?</b></summary>
Plan for approximately **15-20 hours per week**. This includes time for reading, coding along with the notebooks, and completing assignments.
</details>

<details>
<summary><b>Can I complete the course faster or slower than 12 weeks?</b></summary>
Yes, the program is self-paced. You can move faster if you have more time or take longer if needed. The key is to ensure you understand the concepts, not just to finish quickly.
</details>

---

## 🛠️ Technical & Setup Questions

<details>
<summary><b>Should I use GitHub Codespaces or a local setup?</b></summary>
**GitHub Codespaces is strongly recommended.** It provides a pre-configured, consistent, and cloud-based environment, eliminating any local setup issues. Use a local setup only if you have a specific reason, such as needing to work offline or use a local GPU.
</details>

<details>
<summary><b>Do I need an expensive GPU?</b></summary>
**No.** The course is designed to use the Hugging Face Inference API for running large models, which means the heavy computation is done in the cloud. A standard laptop is all you need.
</details>

<details>
<summary><b>What if I encounter installation or package errors?</b></summary>
This is the primary reason we recommend Codespaces. If you are working locally, first ensure you are in an active virtual environment. Then, try upgrading `pip` and reinstalling the requirements:
```bash
pip install --upgrade pip
pip install -r requirements.txt
```
If issues persist, try installing problematic packages one by one to isolate the error.
</details>

---

## 🏗️ Project & Homework Questions

<details>
<summary><b>Can I use AI tools like GitHub Copilot or ChatGPT for assignments?</b></summary>
**Yes, you are encouraged to use them as productivity tools.** Use them to debug code, understand concepts, or get suggestions. However, do not simply copy and paste solutions. The goal is to learn, and using these tools effectively is part of the modern development workflow.
</details>

<details>
<summary><b>Can I choose a different topic for the capstone project?</b></summary>
**Absolutely.** The provided capstone is a template. You are encouraged to adapt the architecture and principles to a domain that interests you, such as finance, healthcare, or retail. The key is to demonstrate the same end-to-end skills.
</details>

<details>
<summary><b>How do I handle cloud costs for the capstone project?</b></summary>
The project is designed to be affordable. Most of the required services fall within the free tiers of cloud providers like GCP. The total cost should be minimal ($5-$15). We also discuss using free alternatives and local deployment strategies.
</details>

---

## 🆘 Getting Help

<details>
<summary><b>I'm stuck. What should I do?</b></summary>
1. **Re-read the material:** Often, the answer is in the notebook or linked resources.
2. **Experiment:** Try to isolate the problem by changing the code.
3. **Use AI:** Ask ChatGPT or Copilot to explain the error or concept.
4. **Search:** Look for your error message on Google or Stack Overflow.
5. **Ask the community:** If you're still stuck, open a **GitHub Discussion** in the repository. Provide context, code snippets, and the full error message.
</details>

---
*Have a question not listed here? Please check the GitHub Discussions or open a new one!*
