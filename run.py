from waitress import serve
import falcon
from sensor import SensorDataCollector
from app import SensorResource
# Create sensor data collector and start it
collector = SensorDataCollector(['/dev/ttyACM0', '/dev/ttyACM1'
                                 ])  # replace with your actual serial ports
collector.start()
# Create Falcon API and add sensor resource
api = falcon.API()
api.add_route('/sensors', SensorResource(collector))
api.add_route('/sensors/{sensor_id}', SensorResource(collector))
# Serve the Falcon API with Waitress
serve(api, host='0.0.0.0', port=8080)