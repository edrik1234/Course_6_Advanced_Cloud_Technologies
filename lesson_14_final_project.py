import json
import boto3
import time
from botocore.exceptions import ClientError

s3 = boto3.client("s3")
bucket_name = "lumbda-files-bucket-edrian-netyosov"


def handle_empty_path():
    try:
        output = {}
        response = s3.list_objects(Bucket=bucket_name)
        if "Contents" in response:
            for content in response["Contents"]:
                file_name = content["Key"]
                file_obj = s3.get_object(Bucket=bucket_name, Key=file_name)
                output[file_name] = file_obj["Body"].read().decode("utf-8")
            return {
                "statusCode": 200,
                "body": json.dumps(output)
            }
        else:
            return {
                "statusCode": 404,
                "body": json.dumps({"message": "Bucket is empty"})
            }
    except ClientError as e:
        return {
            "statusCode": 500,
            "body": json.dumps({"error": str(e)})
        }
    except Exception as e:
        return {
            "statusCode": 500,
            "body": json.dumps({"error": str(e)})
        }


def handle_create(calculations_dict):
    try:
        file_name = f"calc_{int(time.time())}.json"
        file_body = json.dumps(calculations_dict)
        s3.put_object(Bucket=bucket_name, Key=file_name, Body=file_body)
        return {
            "statusCode": 200,
            "body": json.dumps({"status": "Success", "file": file_name})
        }
    except ClientError as e:
        return {
            "statusCode": 500,
            "body": json.dumps({"error": str(e)})
        }


def calculations(data):
    try:
        number_1 = data["number_1"]
        number_2 = data["number_2"]
        operator = data["operator"]

        if not isinstance(number_1, int) or not isinstance(number_2, int):
            raise ValueError("number_1 and number_2 must be integers")

        if operator in ["/", "//"] and number_2 == 0:
            raise ZeroDivisionError("Division by zero")

        if operator == "+":
            result = number_1 + number_2
        elif operator == "-":
            result = number_1 - number_2
        elif operator == "*":
            result = number_1 * number_2
        elif operator == "/":
            result = number_1 / number_2
        elif operator == "//":
            result = number_1 // number_2
        else:
            raise ValueError("Invalid operator. Use one of +, -, *, /, //")

        calculations_dict = {
            str(time.ctime()): f"{number_1} {operator} {number_2} = {result}"
        }

        handle_create(calculations_dict)

        return {
            "statusCode": 200,
            "body": json.dumps(calculations_dict)
        }

    except (ValueError, ZeroDivisionError) as e:
        return {
            "statusCode": 400,
            "body": json.dumps({"error": str(e)})
        }
    except Exception as e:
        return {
            "statusCode": 500,
            "body": json.dumps({"error": str(e)})
        }


def lambda_handler(event, context):
    try:
        path = event["path"]
        http_method = event["httpMethod"]

        if path == "/":
            if http_method == "GET":
                return handle_empty_path()

        elif path == "/calc":
            if http_method == "POST":
                try:
                    body = json.loads(event["body"])
                except json.JSONDecodeError:
                    return {
                        "statusCode": 400,
                        "body": json.dumps({"error": "Invalid JSON format"})
                    }
                return calculations(body)

            elif http_method == "GET":
                calculator_pattern = {
                    "number_1": "int",
                    "number_2": "int",
                    "operator": "str within {'+','-','*','/','//'}"
                }
                return {
                    "statusCode": 200,
                    "body": json.dumps(calculator_pattern)
                }

        return {
            "statusCode": 404,
            "body": json.dumps({"error": "Unsupported Operation"})
        }

    except KeyError as e:
        return {
            "statusCode": 400,
            "body": json.dumps({"error": f"Missing field: {e}"})
        }
    except Exception as e:
        return {
            "statusCode": 500,
            "body": json.dumps({"error": str(e)})
        }
