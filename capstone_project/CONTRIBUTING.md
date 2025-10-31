# Contributing to Manufacturing Copilot

Thank you for your interest in contributing! This project welcomes contributions from the community.

## Getting Started

1. Fork the repository
2. Clone your fork: `git clone https://github.com/YOUR_USERNAME/Gen-AI-Roadmap.git`
3. Create a branch: `git checkout -b feature/your-feature-name`
4. Make your changes
5. Test your changes: `pytest tests/ -v`
6. Commit: `git commit -m 'Add some feature'`
7. Push: `git push origin feature/your-feature-name`
8. Open a Pull Request

## Development Setup

```bash
# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: .\venv\Scripts\Activate.ps1

# Install dependencies
pip install -r requirements-dev.txt

# Run tests
pytest tests/ -v --cov=app

# Format code
black app/ tests/

# Lint
flake8 app/ tests/

# Type check
mypy app/ --ignore-missing-imports
```

## Code Standards

- Follow PEP 8 style guide
- Add type hints to all functions
- Write docstrings for public functions (Google style)
- Maintain test coverage above 80%
- Update documentation for new features

### Example Code Style

```python
def example_function(param1: str, param2: int = 0) -> dict:
    """
    Brief description of what the function does.
    
    Args:
        param1: Description of param1
        param2: Description of param2 (default: 0)
        
    Returns:
        Dictionary with results
        
    Raises:
        ValueError: If param1 is empty
    """
    if not param1:
        raise ValueError("param1 cannot be empty")
    
    return {"result": param1, "count": param2}
```

## Pull Request Guidelines

- Keep PRs focused on a single feature/fix
- Write clear PR descriptions explaining:
  - What changed
  - Why it changed
  - How to test it
- Update tests for code changes
- Update documentation if needed
- Ensure all tests pass
- Follow the existing code style
- Reference related issues

### PR Title Format

- `feat: Add new feature`
- `fix: Fix bug in X`
- `docs: Update documentation`
- `test: Add tests for Y`
- `refactor: Refactor component Z`
- `chore: Update dependencies`

## Testing

### Run All Tests
```bash
pytest tests/ -v
```

### Run Specific Test File
```bash
pytest tests/test_api.py -v
```

### Run with Coverage
```bash
pytest tests/ --cov=app --cov-report=html
```

### Add New Tests
Place tests in the `tests/` directory:
- `test_api.py` - API endpoint tests
- `test_agents.py` - Agent logic tests
- `test_models.py` - Pydantic model tests
- `test_security.py` - Security tests

## Documentation

- Update relevant markdown files in `docs/` or root
- Add docstrings to new functions and classes
- Update `README.md` if adding major features
- Add examples to `guides/` if creating tutorials

## Code Review Process

1. Automated checks must pass:
   - Tests (pytest)
   - Linting (flake8)
   - Type checking (mypy)
   - Formatting (black)

2. Manual review by maintainers:
   - Code quality
   - Design decisions
   - Documentation
   - Test coverage

3. Approval and merge

## Issue Reporting

### Bug Reports

Include:
- Description of the bug
- Steps to reproduce
- Expected behavior
- Actual behavior
- Environment (OS, Python version, etc.)
- Error messages/logs

### Feature Requests

Include:
- Description of the feature
- Use case / motivation
- Proposed implementation (optional)
- Alternatives considered

### Questions

- Check existing issues first
- Search documentation
- Provide context about what you're trying to achieve

## Development Workflow

### Feature Development

```bash
# 1. Create feature branch
git checkout -b feature/my-feature

# 2. Make changes
# ... edit code ...

# 3. Add tests
# ... create/update tests ...

# 4. Run tests
pytest tests/ -v

# 5. Format and lint
black app/ tests/
flake8 app/ tests/

# 6. Commit
git add .
git commit -m "feat: Add my feature"

# 7. Push
git push origin feature/my-feature

# 8. Create Pull Request
```

### Bug Fix Workflow

```bash
# 1. Create fix branch
git checkout -b fix/bug-description

# 2. Write failing test
# ... add test that exposes bug ...

# 3. Fix the bug
# ... implement fix ...

# 4. Verify test passes
pytest tests/ -v

# 5. Commit and push
git add .
git commit -m "fix: Fix bug in X"
git push origin fix/bug-description

# 6. Create Pull Request
```

## Commit Guidelines

### Commit Message Format

```
<type>(<scope>): <subject>

<body>

<footer>
```

### Types
- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation only
- `style`: Code style (formatting, etc.)
- `refactor`: Code refactoring
- `test`: Adding tests
- `chore`: Maintenance tasks

### Examples

```bash
feat(agents): Add retry logic to RAG agent

- Implement exponential backoff
- Add max retry configuration
- Update tests

Closes #123
```

```bash
fix(api): Fix authentication header validation

The API was not properly validating bearer tokens
with special characters. This adds proper escaping.

Fixes #456
```

## Getting Help

- **Documentation**: Check `docs/` and `guides/` directories
- **Issues**: Open a GitHub issue
- **Discussions**: Use GitHub Discussions for questions
- **Email**: Contact maintainers (see README)

## Recognition

Contributors will be:
- Listed in CONTRIBUTORS.md
- Mentioned in release notes
- Acknowledged in documentation

Thank you for contributing! 🎉

## License

By contributing, you agree that your contributions will be licensed under the MIT License.
