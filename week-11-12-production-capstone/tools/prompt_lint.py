# tools/prompt_lint.py
import sys
from pathlib import Path
import yaml

def lint_prompts(directory: Path) -> int:
    """
    Lints all YAML prompt files in a directory for specific quality rules.
    Returns the number of errors found.
    """
    error_count = 0
    try:
        prompt_files = list(directory.rglob("*.yaml"))
    except FileNotFoundError:
        print(f"Directory not found: {directory}")
        return 1
    
    if not prompt_files:
        print(f"No prompt files found in {directory} to lint.")
        return 0

    print(f"Linting {len(prompt_files)} prompt files...")

    for path in prompt_files:
        try:
            with open(path, 'r') as f:
                prompt_data = yaml.safe_load(f)

            # Rule 1: Check for a 'version' key
            if 'version' not in prompt_data:
                print(f"ERROR: {path} - Missing 'version' key.")
                error_count += 1

            # Rule 2: Check for a 'description' key
            if 'description' not in prompt_data:
                print(f"ERROR: {path} - Missing 'description' key.")
                error_count += 1
            
            # Rule 3: Check that description is not empty
            elif not prompt_data['description'].strip():
                print(f"ERROR: {path} - 'description' cannot be empty.")
                error_count += 1

            # Rule 4: Check for a 'template' key
            if 'template' not in prompt_data:
                print(f"ERROR: {path} - Missing 'template' key.")
                error_count += 1

            # Rule 5: Check for placeholders like 'TODO' or 'FIXME' in the template
            template = prompt_data.get('template', '')
            if 'TODO' in template or 'FIXME' in template:
                print(f"ERROR: {path} - Found placeholder 'TODO' or 'FIXME' in template.")
                error_count += 1

        except yaml.YAMLError as e:
            print(f"ERROR: Could not parse {path} - {e}")
            error_count += 1
        except Exception as e:
            print(f"ERROR: An unexpected error occurred with {path} - {e}")
            error_count += 1
            
    if error_count == 0:
        print("✅ All prompts passed linting.")
    else:
        print(f"\n❌ Found {error_count} errors in prompts.")
        
    return error_count

if __name__ == "__main__":
    if len(sys.argv) > 1:
        prompt_dir = Path(sys.argv[1])
        errors = lint_prompts(prompt_dir)
        sys.exit(1 if errors > 0 else 0)
    else:
        print("Usage: python tools/prompt_lint.py <directory_to_lint>")
        sys.exit(1)
