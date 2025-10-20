"""
Script to update course notebooks from ChatOpenAI to HuggingFaceEndpoint
"""

import json
import os
from pathlib import Path

# Cell to add at the beginning of notebooks that use LLMs
SETUP_CELL = {
    "cell_type": "code",
    "execution_count": None,
    "metadata": {},
    "outputs": [],
    "source": [
        "# ⚙️ Setup: Load HuggingFace Token\n",
        "import os\n",
        "from dotenv import load_dotenv\n",
        "\n",
        "load_dotenv()  # Load .env file from project root\n",
        "\n",
        "HF_TOKEN = os.getenv(\"HUGGINGFACE_TOKEN\")\n",
        "if not HF_TOKEN:\n",
        "    raise ValueError(\n",
        "        \"❌ HUGGINGFACE_TOKEN not found!\\n\"\n",
        "        \"Please ensure .env file exists in project root with:\\n\"\n",
        "        \"HUGGINGFACE_TOKEN=hf_your_token_here\\n\"\n",
        "        \"See 00_huggingface_setup.ipynb for setup instructions.\"\n",
        "    )\n",
        "\n",
        "print(\"✅ HuggingFace token loaded!\")"
    ]
}

IMPORT_REPLACEMENT_NOTE = {
    "cell_type": "markdown",
    "metadata": {},
    "source": [
        "**📝 Note**: This notebook has been updated to use **HuggingFace Inference Endpoints** instead of OpenAI.\n",
        "\n",
        "- ✅ **No local GPU required**\n",
        "- ✅ **Free tier available**\n",
        "- ✅ **Setup guide**: See `00_huggingface_setup.ipynb`\n",
        "\n",
        "**Quick Setup**:\n",
        "1. Get token from https://huggingface.co/settings/tokens\n",
        "2. Add to `.env` file: `HUGGINGFACE_TOKEN=hf_your_token_here`\n",
        "3. Run this notebook!"
    ]
}


def update_notebook_cells(notebook_path):
    """Update a single notebook to use HuggingFace endpoints."""
    
    print(f"Processing: {notebook_path}")
    
    try:
        with open(notebook_path, 'r', encoding='utf-8', errors='ignore') as f:
            notebook = json.load(f)
    except Exception as e:
        print(f"  ❌ Error reading: {e}")
        return False
    
    cells = notebook.get('cells', [])
    updated_cells = []
    added_setup = False
    added_note = False
    found_openai_import = False
    
    for i, cell in enumerate(cells):
        cell_source = cell.get('source', [])
        
        # Convert source to string for easier processing
        if isinstance(cell_source, list):
            source_str = ''.join(cell_source)
        else:
            source_str = cell_source
        
        # Check if this cell imports ChatOpenAI
        if 'from langchain_openai import ChatOpenAI' in source_str:
            found_openai_import = True
            
            # Add note before first import (only once)
            if not added_note:
                updated_cells.append(IMPORT_REPLACEMENT_NOTE)
                added_note = True
            
            # Add setup cell before first import (only once)
            if not added_setup:
                updated_cells.append(SETUP_CELL)
                added_setup = True
            
            # Replace the import
            new_source = source_str.replace(
                'from langchain_openai import ChatOpenAI',
                'from langchain_huggingface import HuggingFaceEndpoint'
            )
            
            # Update cell source
            cell['source'] = new_source.split('\n') if '\n' in new_source else [new_source]
        
        # Check if this cell creates ChatOpenAI instance
        elif 'ChatOpenAI(' in source_str:
            # Replace ChatOpenAI with HuggingFaceEndpoint
            new_source = source_str
            
            # Replace class name
            new_source = new_source.replace('ChatOpenAI(', 'HuggingFaceEndpoint(')
            
            # Replace model parameter
            new_source = new_source.replace('model=', 'repo_id=')
            new_source = new_source.replace('model =', 'repo_id=')
            
            # Replace API key parameter
            new_source = new_source.replace(
                'openai_api_key=os.getenv("OPENAI_API_KEY")',
                'huggingfacehub_api_token=HF_TOKEN'
            )
            new_source = new_source.replace(
                "openai_api_key=os.getenv('OPENAI_API_KEY')",
                'huggingfacehub_api_token=HF_TOKEN'
            )
            
            # Replace model names with HuggingFace models
            new_source = new_source.replace(
                'repo_id="gpt-3.5-turbo"',
                'repo_id=os.getenv("HF_LLM_MODEL", "meta-llama/Llama-2-7b-chat-hf")'
            )
            new_source = new_source.replace(
                "repo_id='gpt-3.5-turbo'",
                'repo_id=os.getenv("HF_LLM_MODEL", "meta-llama/Llama-2-7b-chat-hf")'
            )
            new_source = new_source.replace(
                'repo_id="gpt-4"',
                'repo_id=os.getenv("HF_LLM_MODEL", "meta-llama/Llama-2-7b-chat-hf")'
            )
            
            # Add max_new_tokens if not present
            if 'max_new_tokens' not in new_source and 'HuggingFaceEndpoint(' in new_source:
                # Find the closing parenthesis
                if new_source.strip().endswith(')'):
                    new_source = new_source.rstrip(')\n ') + ',\n    max_new_tokens=512\n)'
            
            # Update cell source
            cell['source'] = new_source.split('\n') if '\n' in new_source else [new_source]
        
        updated_cells.append(cell)
    
    if found_openai_import:
        # Update notebook cells
        notebook['cells'] = updated_cells
        
        # Write back
        try:
            with open(notebook_path, 'w', encoding='utf-8', errors='ignore') as f:
                json.dump(notebook, f, indent=1, ensure_ascii=False)
            
            print(f"  ✅ Updated: {notebook_path.name}")
            return True
        except Exception as e:
            print(f"  ❌ Error writing: {e}")
            return False
    else:
        print(f"  ⏭️  Skipped (no OpenAI usage): {notebook_path.name}")
        return False


def main():
    """Main function to update all notebooks."""
    
    # Get project root
    project_root = Path(__file__).parent.parent
    
    print("=" * 60)
    print("UPDATING NOTEBOOKS TO USE HUGGINGFACE ENDPOINTS")
    print("=" * 60)
    print()
    
    # Find all notebooks
    notebook_paths = list(project_root.glob("week-*/**/*.ipynb"))
    
    print(f"Found {len(notebook_paths)} notebooks\n")
    
    updated_count = 0
    for nb_path in sorted(notebook_paths):
        if update_notebook_cells(nb_path):
            updated_count += 1
    
    print()
    print("=" * 60)
    print(f"COMPLETED: Updated {updated_count} notebooks")
    print("=" * 60)
    print()
    print("Next steps:")
    print("1. Review changes with: git diff")
    print("2. Test a sample notebook")
    print("3. Commit changes: git add -A && git commit -m 'Update to HuggingFace endpoints'")
    print()


if __name__ == "__main__":
    main()
