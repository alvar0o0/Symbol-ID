# Financial Symbol Matcher

A microSaaS solution for matching financial instrument symbols across different vendors and formats.

## Features
- Intelligent symbol matching with normalization
- Support for multiple vendors (Bloomberg, Reuters, etc.)
- Confidence scoring for matches
- RESTful API

## Tech Stack
- Python/Flask
- SQLAlchemy
- SQLite
- [Future: AI/ML components]

## Development
```bash
# Setup
python -m venv .venv
source .venv/bin/activate  # or `.venv\Scripts\activate` on Windows
pip install -r requirements.txt

# Run
python run.py
