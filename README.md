# Regex Data Extraction Project

## Overview
This repository contains a Python project designed to extract various data types (Email, URL, Phone Number, Credit Card, etc.) from text using Regular Expressions.

## Author
- **Samuel Kwizera**  
 

## Project Structure


### 1. `patterns.py`
Holds all the compiled regex patterns for each data type.

### 2. `extractors.py`
Provides functions that apply those regex patterns to text and return the extracted matches.

### 3. `tests.py`
Contains automated tests (using Python’s `unittest`) to verify each extractor function works properly.

### 4. `main.py`
The main script to demonstrate the usage of these extractor functions on a sample string.

## Setup and Usage

1. **Clone the Repository**
   ```bash
   git clone https://github.com/Samkwizera/regex_data_extraction.git
   

---

## How to Use This Project

1. **Create the folder** `regex_data_extraction`.
2. **Place** the four Python files (`main.py`, `patterns.py`, `extractors.py`, `tests.py`) inside the folder.
3. **Place** the `README.md` in the same folder.
4. **Initialize a Git repo** (`git init`) and commit/push as needed.
5. **Run** `python main.py` to see the extraction in action. 
6. **Run** `python tests.py` for unit tests.


