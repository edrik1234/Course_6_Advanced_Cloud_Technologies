Calculator Project:


Description:
This project is a clean and modern implementation of a simple serverless calculator, built using AWS Lambda and API Gateway. It supports both GET and POST methods through a RESTful API 
and demonstrates structured exception handling, proper status codes, and clean logical flow.

When you access the root path “/”, the function returns a 400 status code since this path is not supported.
When you access “/calc”, the behavior depends on the method you choose:

If you use the GET method:
the function returns a JSON structure that explains the expected input format, showing the three required fields: num1, num2, and operator.
Example:
{
"num1": "int",
"num2": "int",
"operator": "str within {'*', '/', '//', '+', '-'}"
}

If you use the POST method:
you must provide num1, num2, and operator according to the format above.
The calculator then performs the corresponding arithmetic operation, which can be addition, subtraction, multiplication, float division ( / ), or integer division ( // ).


This project uses:
AWS Lambda as the compute layer, API Gateway to expose endpoints, REST API standards for communication, and Python’s built-in exception handling for validation and error control.


During development, I encountered and solved several issues that improved both my code quality and my understanding of logic flow:

Conditional Logic Error:
Initially, I wrote:
if "num1" or "num2" or "operator" not in body
This caused the condition to always evaluate as True, since non-empty strings are considered truthy.
I fixed it by writing:
if "num1" not in body or "num2" not in body or "operator" not in body

Invalid JSON Handling:
Some inputs were not valid JSON strings. I solved this by wrapping the parsing step in an exception block using “except json.JSONDecodeError”, ensuring that invalid formats return a clear 400 error message.

Incorrect HTTP Status Codes:
Originally, unsupported HTTP methods returned the wrong status code. I corrected this by returning a proper 405 “Method Not Allowed” response for unsupported methods.


Overall, this project demonstrates clean code practices, clear exception handling, and professional REST API design, showcasing both backend logic and cloud-based service integration using AWS.
