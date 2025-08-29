#!/usr/bin/env python3
"""
Simple script to test your deployed BFHL API
Replace YOUR_LIVE_URL with your actual Vercel URL
"""

import requests
import json

# Replace this with your actual Vercel URL
API_URL = "https://YOUR_VERCEL_URL.vercel.app/bfhl"

def test_deployed_api():
    print("🚀 Testing your deployed BFHL API...")
    print(f"URL: {API_URL}")
    print("=" * 50)
    
    # Test data from the assignment
    test_data = {"data": ["a","1","334","4","R", "$"]}
    
    try:
        print("Sending test request...")
        response = requests.post(API_URL, json=test_data)
        
        if response.status_code == 200:
            print("✅ SUCCESS! Your API is working!")
            result = response.json()
            print("\n📝 Response:")
            print(json.dumps(result, indent=2))
            
            # Check if all required fields are present
            required_fields = ["is_success", "user_id", "email", "roll_number", 
                             "odd_numbers", "even_numbers", "alphabets", 
                             "special_characters", "sum", "concat_string"]
            
            missing_fields = [field for field in required_fields if field not in result]
            
            if not missing_fields:
                print("\n✅ All required fields are present!")
                print(f"✅ Email: {result['email']}")
                print(f"✅ Roll Number: {result['roll_number']}")
                print("\n🎉 Your API is ready for submission!")
            else:
                print(f"\n❌ Missing fields: {missing_fields}")
                
        else:
            print(f"❌ Error: Status code {response.status_code}")
            print(f"Response: {response.text}")
            
    except requests.exceptions.RequestException as e:
        print(f"❌ Network error: {e}")
        print("\n💡 Make sure to replace YOUR_VERCEL_URL with your actual URL!")
    
    print("\n" + "=" * 50)
    print("Remember to submit this URL to the assignment form:")
    print(f"📎 {API_URL}")

if __name__ == "__main__":
    print("⚠️  IMPORTANT: Update the API_URL variable with your actual Vercel URL first!")
    print()
    test_deployed_api()