🌡️ IoT Monitoring Microservices Project:

This project simulates an IoT-based system that collects and monitors temperature, humidity, and power consumption data from two sensors 
— ac_sensor and washing_sensor. 
Each sensor sends data via HTTP to three dedicated monitoring services: Temperature Monitor, Humidity Monitor, and Power Monitor. 
Each service computes the average value of its metric and exposes it through a REST API, all accessible from a unified Swagger UI interface. 
The entire system runs under Docker Compose, using Kafka for communication and Zookeeper for coordination.

Technologies Used:

• Kafka.

• Zookeeper.

• REST API.

• Swagger / OpenAPI.

• Docker & Docker-Compose. 

• Python. 

• Connexion.

Dependencies:
• connexion[uvicorn, flask, swagger-ui] >= 2.6.0. 

• flask >= 2.2.0, <2.3.0. 

• kafka-python. 

• flasgger. 

• openapi-spec-validator. 

• python_dateutil == 2.6.0. 

• setuptools >= 21.0.0. 

• swagger-ui-bundle >= 0.0.2.

• uvicorn.

🔧 Common Issues & Solutions:

1) Dependency Conflicts – Fixed by pinning compatible versions in requirements.txt (especially Flask <2.3.0 for Connexion).

2) Swagger Errors – Resolved by ensuring valid OpenAPI specs and proper installation of swagger-ui-bundle and connexion[swagger-ui], and by ensuring that what we write in controllers fit the swagger.yaml,
and that swagger has an appropriate syntax, that fits to all project and his versions of libraries and dependencies. 

3) Encoding / JSON Serialization Error – Fixed by replacing Connexion’s encoder with a custom one using Flask’s JSONEncoder.
   Fixed code (encoder.py):

   from flask.json import JSONEncoder
   import six
   from models.base_model_ import Model

   class CustomJSONEncoder(JSONEncoder):
       include_nulls = False

       def default(self, o):
           if isinstance(o, Model):
               dikt = {}
               for attr, _ in six.iteritems(o.swagger_types):
                   value = getattr(o, attr)
                   if value is None and not self.include_nulls:
                       continue
                   attr = o.attribute_map[attr]
                   dikt[attr] = value
               return dikt
           return super().default(o)

4) Port Conflicts – Solved by assigning unique ports to each monitor service in docker-compose.yml (e.g., 5001/5002/5003).

5) Service Connectivity Issues – Solved by creating a shared network in docker-compose.yml, allowing services to communicate by container name (e.g., http://humidity:5001).

Summary:

A fully containerized microservice-based IoT system built with Python, Kafka, and Connexion, providing live data aggregation and monitoring through a clean Swagger UI. 
It demonstrates distributed communication, REST API orchestration, and modular architecture — all in one deployable Docker environment.
