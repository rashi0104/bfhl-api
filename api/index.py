from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
import re

app = FastAPI(title="BFHL API", description="Bajaj Finserv Health Challenge API")

class InputData(BaseModel):
    data: List[str]

class ResponseData(BaseModel):
    is_success: bool
    user_id: str
    email: str
    roll_number: str
    odd_numbers: List[str]
    even_numbers: List[str]
    alphabets: List[str]
    special_characters: List[str]
    sum: str
    concat_string: str

def process_data(data: List[str]) -> dict:
    """Process the input data and return categorized results"""
    odd_numbers = []
    even_numbers = []
    alphabets = []
    special_characters = []
    numbers_sum = 0
    all_alphabets = []
    
    for item in data:
        # Check if item is a number
        if item.isdigit():
            num = int(item)
            if num % 2 == 0:
                even_numbers.append(item)
            else:
                odd_numbers.append(item)
            numbers_sum += num
        # Check if item contains only alphabetic characters
        elif item.isalpha():
            alphabets.append(item.upper())
            # Collect all individual alphabetic characters for concatenation
            all_alphabets.extend(list(item.lower()))
        else:
            # Check if it's a special character or contains special characters
            if not item.isalnum():
                special_characters.append(item)
            else:
                # Mixed alphanumeric - extract alphabets and numbers separately
                for char in item:
                    if char.isdigit():
                        num = int(char)
                        if num % 2 == 0:
                            even_numbers.append(char)
                        else:
                            odd_numbers.append(char)
                        numbers_sum += num
                    elif char.isalpha():
                        alphabets.append(char.upper())
                        all_alphabets.append(char.lower())
                    else:
                        special_characters.append(char)
    
    # Create concatenation string in reverse order with alternating caps
    concat_string = ""
    if all_alphabets:
        reversed_alphabets = all_alphabets[::-1]
        for i, char in enumerate(reversed_alphabets):
            if i % 2 == 0:
                concat_string += char.upper()
            else:
                concat_string += char.lower()
    
    return {
        "odd_numbers": odd_numbers,
        "even_numbers": even_numbers,
        "alphabets": alphabets,
        "special_characters": special_characters,
        "sum": str(numbers_sum),
        "concat_string": concat_string
    }

@app.post("/bfhl", response_model=ResponseData)
async def process_bfhl_data(input_data: InputData):
    """
    Process input data and return categorized results
    """
    try:
        # Process the data
        processed = process_data(input_data.data)
        
        # User information based on Rashi Goyal, DOB: 23 Sept 2003
        response = ResponseData(
            is_success=True,
            user_id="rashi_goyal_23092003",
            email="connectrashigoyal@gmail.com",
            roll_number="22BCE1832",
            odd_numbers=processed["odd_numbers"],
            even_numbers=processed["even_numbers"],
            alphabets=processed["alphabets"],
            special_characters=processed["special_characters"],
            sum=processed["sum"],
            concat_string=processed["concat_string"]
        )
        
        return response
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal server error: {str(e)}")

@app.get("/")
async def root():
    """Root endpoint for health check"""
    return {"message": "BFHL API is running", "endpoint": "/bfhl"}

# This is needed for Vercel
handler = app