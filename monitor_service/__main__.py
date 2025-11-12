import os
import connexion
from encoder import CustomJSONEncoder
from threading import Thread
from consumer import monitorSensor

def main():
    app = connexion.App(__name__, specification_dir='./swagger/')
    app.app.json_encoder = CustomJSONEncoder  # Use the custom JSON encoder
    app.app.config['SENSOR_DATA'] = {
        "current": {},
        "sum": {},
        "count": {}
    }

    # List of topics to consume (set via environment variable, e.g., "ac_power,washing_power" for PowerMonitor)
    kafka_topics = os.getenv("KAFKA_TOPICS", "").split(",")

    # Start a separate thread for each Kafka topic
    threads = []
    for topic in kafka_topics:
        thread = Thread(target=monitorSensor, args=(app.app.config['SENSOR_DATA'], topic))
        thread.start()
        threads.append(thread)

    # Start Flask API
    app.add_api('swagger.yaml', arguments={'title': 'IoT Monitoring API'}, pythonic_params=True)
    app.run(host="0.0.0.0", port=5000)

    # Wait for all consumer threads to finish
    for thread in threads:
        thread.join()

if __name__ == '__main__':
    main()
