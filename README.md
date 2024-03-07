# Scytale Exercise
Home assignment solution.

## Usage

1. Clone the repo:
```bash
git clone https://github.com/MadBull1995/scytale-exercise.git
```

2. Navigate to to repository root folder
```bash
cd ./scytale-exercise
```

3. And run the following command:
```bash
python -m src.main
```

The process would generate new `data` folder which will hold all phased persisted data.
The files will be structured as follows:
```bash 
.
├── ORGANIZTION_NAME
│   ├── REPO_NAME
│   │   └── part-00000-XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX-XXXX.json
│   └── output
│       ├── _SUCCESS
│       └── part-00000-XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX-XXXX.snappy.parquet
```

## Project structue

```bash
.
├── src
│   ├── __init__.py
│   ├── _schema.py # py-spark utils schema
│   ├── api.py # github api wrapper including rate limiter and paginator + optional use of auth
│   ├── data.py # main processing class
│   └── main.py # entry point
```

---
Created with `</>` by Amit Shmulevitch 2024