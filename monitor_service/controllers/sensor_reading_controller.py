from flask import jsonify, current_app

def calculate_average(data, appliance_key):
    """Helper function to calculate average, returning 0 if count is 0."""
    sum_value = data["sum"].get(appliance_key, 0)
    count_value = data["count"].get(appliance_key, 0)
    return sum_value / count_value if count_value > 0 else 0

def avg_get():
    sensor_data = current_app.config['SENSOR_DATA']
    data = {}
    
    # Use a loop to populate power_data
    for appliance in sensor_data["sum"]:
        data[appliance] = str(calculate_average(sensor_data, appliance))
    
    return jsonify(data)
