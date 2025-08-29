import requests
import json

# Base URL for the API
BASE_URL = "http://localhost:8000"

def test_api():
    """Test the API with the provided examples"""
    
    # Test cases from the assignment
    test_cases = [
        {
            "name": "Example A",
            "input": {"data": ["a","1","334","4","R", "$"]},
            "expected_patterns": {
                "odd_numbers": ["1"],
                "even_numbers": ["334","4"], 
                "alphabets": ["A","R"],
                "special_characters": ["$"],
                "sum": "339"
            }
        },
        {
            "name": "Example B", 
            "input": {"data": ["2","a", "y", "4", "&", "-", "*", "5","92","b"]},
            "expected_patterns": {
                "odd_numbers": ["5"],
                "even_numbers": ["2","4","92"],
                "alphabets": ["A", "Y", "B"],
                "special_characters": ["&", "-", "*"],
                "sum": "103"
            }
        },
        {
            "name": "Example C",
            "input": {"data": ["A","ABcD","DOE"]},
            "expected_patterns": {
                "odd_numbers": [],
                "even_numbers": [],
                "alphabets": ["A","ABCD","DOE"],
                "special_characters": [],
                "sum": "0"
            }
        }
    ]
    
    print("Testing BFHL API...")
    print("=" * 50)
    
    for test_case in test_cases:
        print(f"\n{test_case['name']}")
        print("-" * 30)
        
        try:
            response = requests.post(f"{BASE_URL}/bfhl", json=test_case["input"])
            
            if response.status_code == 200:
                data = response.json()
                print("✅ Status: SUCCESS")
                print(f"Request: {test_case['input']}")
                print("Response:")
                print(json.dumps(data, indent=2))
                
                # Validate expected patterns
                for key, expected in test_case["expected_patterns"].items():
                    if data.get(key) == expected:
                        print(f"✅ {key}: MATCH")
                    else:
                        print(f"❌ {key}: MISMATCH - Expected {expected}, Got {data.get(key)}")
            else:
                print(f"❌ Status: FAILED - {response.status_code}")
                print(response.text)
                
        except Exception as e:
            print(f"❌ Error: {e}")
    
    print("\n" + "=" * 50)
    print("Testing complete!")

if __name__ == "__main__":
    test_api()