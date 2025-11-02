AWS API LAMBDA CALCULATOR:

🧮 AWS Lambda Calculator API
A serverless calculator REST API built with AWS Lambda, API Gateway, S3, and EC2.
This project demonstrates how to design, deploy, and manage a fully serverless backend on AWS — performing real-time arithmetic operations and storing results in the cloud.

🚀 Overview
The API allows users to perform basic arithmetic operations (+, -, *, /, //) through HTTP requests.
Each result is saved as a JSON file inside an AWS S3 bucket, providing persistent and easily retrievable calculation logs.

🏗️ Architecture
AWS Lambda → Executes all backend logic and calculations.

Amazon API Gateway → Exposes RESTful endpoints to trigger Lambda functions.

Amazon S3 → Stores JSON results and serves as a lightweight database.

Amazon EC2 → Used for testing, deployment scripts, and server monitoring.

IAM Roles → Control access between Lambda, S3, and API Gateway securely.

🧰 Technologies Used
Category	Tools & Services
Cloud Platform	AWS
Compute	AWS Lambda
API Management Amazon API Gateway
Storage	Amazon S3
Deployment AWS EC2
Python
Libraries	boto3, json, datetime, urllib
Infrastructure IAM Roles, CloudWatch Logs

🧩 API Endpoints

Method	Endpoint	Description

⚙️ Error Handling

Invalid Operator → Returns 400 with message "Invalid operator".

Division by Zero → Returns 400 with message "Cannot divide by zero".

Empty Bucket → Returns 404 with message "No files found in S3 bucket".

🧠 How It Works

User sends a calculation request via API Gateway.

Lambda function performs the operation and creates a timestamped JSON file.

Result is uploaded to an S3 bucket using boto3.

Users can list all previous calculations using the root / endpoint.

Example_Request:

POST /calc
{
  "number_1": 10,
  "number_2": 5,
  "operator": "+"
}

Output:

{
  "Sat Nov 02 11:00:00 2025": "10 + 5 = 15"
}
GET	/	Lists all JSON result files from the S3 bucket
GET	/calc	Returns an example of the required input format
POST	/calc	Performs a calculation and saves the result to S3
