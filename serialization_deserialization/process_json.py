"""
1. Takes a dictionary (data) and a filename (filename) as input.
2. Uses json.dump to serialize the dictionary to the specified JSON file.
3. Uses json.load to deserialize the JSON file back into a dictionary.
4. Returns the deserialized dictionary.
"""

import json

def process_json(data: dict, filename: str) -> dict:
    """Serialize a dictionary to a JSON file and deserialize it back."""
    # Serialize the dictionary to a JSON file
    with open(filename, 'w') as file:
        json.dump(data, file)
    
    # Deserialize the JSON file back into a dictionary
    with open(filename, 'r') as file:
        deserialized_data = json.load(file)
    
    return deserialized_data

# Test the process_json function
if __name__ == "__main__":
    test_data = {'name': 'Alice', 'age': 30, 'city': 'Kampala'}
    filename = 'data.json'
    result = process_json(test_data, filename)
    print(f"Original dictionary: {test_data}")
    print(f"Deserialized dictionary: {result}")
