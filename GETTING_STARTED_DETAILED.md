# 🚀 Getting Started: Your Development Environment

Welcome! This guide provides a clear, step-by-step path to setting up your development environment. To ensure a smooth and consistent experience, we **strongly recommend using GitHub Codespaces**. It's the fastest way to get started and avoids common local setup issues.

---

## 🛠️ Environment Setup: The Recommended Path (GitHub Codespaces)

GitHub Codespaces creates a pre-configured, containerized development environment in the cloud. This means you can start coding in minutes with all the necessary tools and dependencies already installed, directly from your browser.

### Steps to Launch Your Codespace:
1.  **Navigate to the Repository:** Go to the main page of this repository on GitHub.
2.  **Open in Codespaces:**
    *   Click the green **`< > Code`** button located at the top of the file list.
    *   Select the **`Codespaces`** tab.
    *   Click **`Create codespace on main`**. GitHub will prepare your environment, which may take a few minutes.
3.  **Set Your Hugging Face Token:**
    *   To download models from Hugging Face, you need to provide an access token.
    *   Once your Codespace is running, go to your repository's **`Settings`** tab.
    *   Navigate to **`Secrets and variables`** > **`Codespaces`** on the left-hand menu.
    *   Create a new repository secret named `HUGGINGFACE_TOKEN`.
    *   Paste your [Hugging Face access token](https://huggingface.co/settings/tokens) into the value field. It's recommended to use a token with 'read' permissions.
    *   The environment is designed to automatically detect and use this secret, so you only need to do this once.
4.  **Start Learning:**
    *   Once the Codespace is ready, it will open a VS Code interface in your browser.
    *   Open the `00_environment_setup.ipynb` notebook from the file explorer on the left.
    *   Run the cells in the notebook to verify that all dependencies are correctly installed and that you can successfully connect to Hugging Face.

That's it! You are now fully set up and ready to begin the course.

---

## 💻 Local Development Setup (Alternative Path)

If you are an advanced user and prefer to work on your local machine, follow these steps. Please note that this path may require more troubleshooting.

### 1. Prerequisites:
- **Python:** Ensure you have Python 3.11 or higher installed.
- **Git:** You must have Git installed for cloning the repository.
- **IDE:** A modern code editor like VS Code is highly recommended.

### 2. Setup Instructions:
1.  **Clone the Repository:**
    ```bash
    git clone https://github.com/your-username/your-repo-name.git
    cd your-repo-name
    ```
2.  **Create and Activate a Virtual Environment:**
    *   This is a critical step to isolate project dependencies.
    *   **Windows (PowerShell):**
        ```powershell
        python -m venv venv
        .\venv\Scripts\Activate.ps1
        ```
    *   **macOS / Linux (Bash):**
        ```bash
        python3 -m venv venv
        source venv/bin/activate
        ```
3.  **Install Dependencies:**
    *   First, upgrade `pip` to the latest version.
    *   Then, install all required packages from the `requirements.txt` file.
    ```bash
    pip install --upgrade pip
    pip install -r requirements.txt
    ```
4.  **Set Environment Variables:**
    *   Create a file named `.env` in the root directory of the project.
    *   Add your Hugging Face token to this file. This keeps your secret keys out of your code.
        ```
        HUGGINGFACE_TOKEN="hf_your_hugging_face_token_here"
        ```
    *   The notebooks are configured to automatically load variables from this `.env` file. **Crucially, ensure your `.gitignore` file includes `.env` to prevent accidentally committing your secrets.**

---

## ✅ Verification: The Final Check

Whether you are on Codespaces or your local machine, the final step is to **verify your setup**.
- Open and run all the cells in the `00_environment_setup.ipynb` notebook.
- If every cell executes without any errors, your environment is correctly configured and ready for the course.

## 🗂️ Next Steps

With your environment fully operational, you are ready to dive in:
1.  Start by reading the `README.md` in the `week-01-02-python-ml-foundations` directory to get an overview of the first module.
2.  Begin your hands-on learning with the first notebook of the course.

Happy coding, and welcome to the Gen AI Masters Program!
