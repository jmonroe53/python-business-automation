# Python Business Automation — Lead Tracker

Sprint 01 learning project for the [AI Mastery & PocketCrew curriculum](https://github.com/jmonroe53/AI-Mastery-PocketCrew-Development/issues/1).

Build a command-line lead tracker while practicing Python functions, dictionaries, loops, files, and testing. **This repository is a starter scaffold, not a completed assignment.**

## Setup

Requires Python 3.11+.

```bash
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\\Scripts\\activate
python -m pip install -e '.[dev]'
python -m lead_tracker
pytest
```

## Planned features

- [ ] Add a lead (name, email, source, interest level)
- [ ] List and search leads
- [ ] Edit and delete a lead
- [ ] Save and load leads from JSON or CSV
- [ ] Score leads by interest and source
- [ ] Generate a summary report
- [ ] Add tests for storage, validation, and scoring

## Repository layout

```text
src/lead_tracker/  # Python application package
tests/             # Automated tests
data/              # Local sample data (no real customer information)
.github/workflows/ # Continuous integration
```

## Learning milestones

1. Implement the menu and data model.
2. Add validation and file persistence.
3. Add scoring and reporting.
4. Test, document, and demo the app.

Use synthetic lead data only. Never commit secrets or actual customer information.
