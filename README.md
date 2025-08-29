# BFHL API - Bajaj Finserv Health Challenge

A FastAPI-based REST API that processes input arrays and categorizes the data according to specific requirements.

## Author Information
- **Name**: Rashi Goyal
- **Date of Birth**: 23 September 2003
- **User ID**: rashi_goyal_23092003
- **Email**: connectrashigoyal@gmail.com
- **Roll Number**: 22BCE1832

## API Endpoint

### POST /bfhl

Processes an input array and returns categorized data.

**Request Format:**
```json
{
  "data": ["a","1","334","4","R", "$"]
}
```

**Response Format:**
```json
{
  "is_success": true,
  "user_id": "rashi_goyal_23092003",
  "email": "connectrashigoyal@gmail.com",
  "roll_number": "22BCE1832",
  "odd_numbers": ["1"],
  "even_numbers": ["334","4"],
  "alphabets": ["A","R"],
  "special_characters": ["$"],
  "sum": "339",
  "concat_string": "Ra"
}
```

## Features

1. **Status**: Returns success/failure status
2. **User Information**: Includes user_id, email, and roll_number
3. **Number Processing**: Separates odd and even numbers
4. **Alphabet Processing**: Converts to uppercase
5. **Special Characters**: Identifies non-alphanumeric characters
6. **Sum Calculation**: Returns sum of all numbers as string
7. **String Concatenation**: Reverses alphabets with alternating case

## Installation & Setup

1. Clone the repository
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the server:
   ```bash
   python3 main.py
   ```

The API will be available at `http://localhost:8000`

## Testing

Run the test suite:
```bash
python3 test_api.py
```

## Deployment Options

### Vercel
1. Connect your GitHub repository to Vercel
2. Deploy using the included `vercel.json` configuration

### Railway
1. Connect your GitHub repository to Railway
2. Deploy using the included `Procfile`

### Render
1. Connect your GitHub repository to Render
2. Deploy using the included `render.yaml`

## API Documentation

Once deployed, visit `/docs` for interactive API documentation powered by FastAPI's automatic OpenAPI integration.

## Examples

### Example A
**Input**: `["a","1","334","4","R", "$"]`
**Output**: Odd: ["1"], Even: ["334","4"], Alphabets: ["A","R"], Special: ["$"], Sum: "339"

### Example B  
**Input**: `["2","a", "y", "4", "&", "-", "*", "5","92","b"]`
**Output**: Odd: ["5"], Even: ["2","4","92"], Alphabets: ["A","Y","B"], Special: ["&","-","*"], Sum: "103"

### Example C
**Input**: `["A","ABcD","DOE"]`
**Output**: Odd: [], Even: [], Alphabets: ["A","ABCD","DOE"], Special: [], Sum: "0"