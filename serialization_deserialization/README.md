# Serialization and Deserialization in Python

## Project Overview
This project implements a Python function to demonstrate serialization and deserialization using the `json` module. The function `process_json` serializes a dictionary to a JSON file and deserializes it back, returning the resulting dictionary. The task showcases how to use JSON for data persistence and retrieval in a simple, interoperable format.

## Directory Structure
```
serialization_deserialization/
├── README.md
└── process_json.py
```

## Task Description
- **File**: `process_json.py`
- **Function**: `process_json(data: dict, filename: str) -> dict`
- **Description**: 
  - Takes a dictionary (`data`) and a filename (`filename`) as input.
  - Serializes the dictionary to a JSON file with the given filename.
  - Deserializes the JSON file back into a dictionary.
  - Returns the deserialized dictionary.
- **Expected Behavior**:
  - Input: A dictionary (e.g., `{'name': 'Alice', 'age': 30, 'city': 'Kampala'}`) and a filename (e.g., `'data.json'`).
  - Output: The deserialized dictionary, identical to the input dictionary.
  - Creates a JSON file with the specified filename containing the serialized data.

## Expected Output (for test case)
```
Original dictionary: {'name': 'Alice', 'age': 30, 'city': 'Kampala'}
Deserialized dictionary: {'name': 'Alice', 'age': 30, 'city': 'Kampala'}
```

## Notes
- The `process_json` function uses the `json` module for serialization (`json.dump`) and deserialization (`json.load`).
- The function assumes the input dictionary is JSON-serializable (contains basic types like strings, numbers, lists, etc.).
- Ensure the specified filename has a `.json` extension for clarity, though the function works with any valid filename.
- The test section in `process_json.py` creates a sample dictionary, processes it, and prints both the original and deserialized dictionaries for comparison.
