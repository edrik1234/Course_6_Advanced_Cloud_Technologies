import json

def handle_bad_path_request(event, path):
    return {
        'statusCode': 400,
        'body': json.dumps('Empty path is not supported')
    }

def lambda_handler(event, context):
    try:
        method = event["httpMethod"]
        path = event["path"]

        if path == "/":
            return handle_bad_path_request(event, "/")

        elif path == "/calc":
            if method == "GET":
                dict_calc = {
                    "num1": "int",
                    "num2": "int",
                    "operator": "str within {'*','/', '//', '+', '-'}"
                }
                return {
                    'statusCode': 200,
                    'body': json.dumps(dict_calc)
                }

            elif method == "POST":
                try:
                    body = json.loads(event["body"])
                except json.JSONDecodeError:
                    return {
                        'statusCode': 400,
                        'body': json.dumps("Invalid JSON format ")
                    }

                if "num1" not in body or "num2" not in body or "operator" not in body:
                    raise KeyError("Missing required keys in the request body")
        
                num1 = body["num1"]
                num2 = body["num2"]
                operator = body["operator"]

                if not isinstance(num1, int) or not isinstance(num2, int):
                    raise ValueError("num1 and num2 must be integers ")
                if not isinstance(operator, str):
                    raise ValueError("operator must be a string ")

                if operator == "+":
                    result = num1 + num2
                elif operator == "-":
                    result = num1 - num2
                elif operator == "*":
                    result = num1 * num2
                elif operator == "/":
                    if num2 == 0:
                        raise ZeroDivisionError("Cannot divide by zero ")
                    result = num1 / num2
                elif operator == "//":
                    if num2 == 0:
                        raise ZeroDivisionError("Cannot divide by zero ")
                    result = num1 // num2
                else:
                    return {
                        'statusCode': 400,
                        'body': json.dumps(f'Unsupported operator: {operator}')
                    }

                return {
                    'statusCode': 200,
                    'body': json.dumps(f'Result: {num1} {operator} {num2} = {result}')
                }

            else:
                return {
                    'statusCode': 405,
                    'body': json.dumps(f'Unsupported method: {method}')
                }

        else:
            return {
                'statusCode': 404,
                'body': json.dumps(f'Unsupported path: {path}')
            }

    except ValueError as e:
        return {
            'statusCode': 400,
            'body': json.dumps(f'Invalid value: {str(e)}')
        }
    except ZeroDivisionError as e:
        return {
            'statusCode': 400,
            'body': json.dumps(str(e))
        }
    except KeyError as e:
        return {
            'statusCode': 400,
            'body': json.dumps(f'Missing key: {e}')
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps(f'Internal server error: {str(e)}')
        }
    
