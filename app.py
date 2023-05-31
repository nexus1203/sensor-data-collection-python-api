import falcon


class SensorResource:

    def __init__(self, data_collector):
        self.data_collector = data_collector

    def on_get(self, req, resp, sensor_id=None):
        if sensor_id is None:
            resp.media = self.data_collector.sensors_data
        else:
            if sensor_id in self.data_collector.sensors_data:
                resp.media = self.data_collector.sensors_data[sensor_id]
            else:
                raise falcon.HTTPNotFound()

    def on_post(self, req, resp):
        pass  # not implemented

    def on_put(self, req, resp):
        pass  # not implemented

    def on_delete(self, req, resp):
        pass  # not implemented


if __name__ == "__main__":
    # import the SensorDataCollector we created before
    from sensor import SensorDataCollector
    # Create sensor data collector and start it
    collector = SensorDataCollector(
        ['COM5', 'COM6'])  # replace with your actual serial ports
    collector.start()
    # Create Falcon API and add sensor resource
    api = falcon.API()
    api.add_route('/sensors', SensorResource(collector))
    api.add_route('/sensors/{sensor_id}', SensorResource(collector))
