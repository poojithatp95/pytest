# pytest

This repository includes a minimal setup for running pytest.

Quickstart
1. Create a virtual environment and activate it:

	macOS / Linux (zsh/bash):

	```bash
	python3 -m venv .venv
	source .venv/bin/activate
	```

2. Install dependencies:

	```bash
	pip install -r requirements.txt
	```

3. Run tests:

	```bash
	python -m pytest -q
	```

CI: A GitHub Actions workflow is included at `.github/workflows/pytest.yml` that installs dependencies and runs `pytest` on push and pull requests to `main`.

Files added:
- `src/myproj/__init__.py` — example function `add`
- `tests/test_add.py` — pytest tests for the example
- `requirements.txt` — pytest pinned

