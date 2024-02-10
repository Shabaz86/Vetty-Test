# Your Flask Application

## Overview
This Flask application provides a simple endpoint to read and render content from text files. It supports optional parameters to specify start and end line numbers.

## Usage
1. Ensure you have Python installed.
2. Create a virtual environment (optional but recommended).
3. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```
4. Run the Flask application:
    ```bash
    python app.py
    ```
   The application will be available at http://127.0.0.1:5000/readfile/.

## Endpoint
### `/readfile/`
- **Default:** `/readfile/file1.txt`
- **Optional Parameters:**
  - `start_line` (default: 1, type: int)
  - `end_line` (default: None, type: int)

### Examples:
- `/readfile/file2.txt`
- `/readfile/file3.txt?start_line=5&end_line=10`

## Error Handling
- 404: File not found.
- 500: Internal server error.

## File Encoding Detection
The application uses the `chardet` library to automatically detect the encoding of the text file.


