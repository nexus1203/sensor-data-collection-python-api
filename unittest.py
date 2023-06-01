import unittest
from sensor import SensorDataCollector

class TestSensorDataCollector(unittest.TestCase):

    def setUp(self):
        self.collector = SensorDataCollector(['COM5', 'COM6'])

    def tearDown(self):
        self.collector.stop()

    def test_start(self):
        self.collector.start()
        self.assertTrue(self.collector.threads)

    def test_stop(self):
        self.collector.start()
        self.collector.stop()
        self.assertFalse(self.collector.threads)

    def test_collect_data(self):
        self.collector.start()
        # Assuming data collection takes 2 seconds
        self.collector.stop_event.wait(timeout=2)
        self.assertTrue(self.collector.sensors_data)

    def test_parse_data(self):
        line = "Sensor: 0, Humidity: 50.0, Temperature: 25.5"
        sensor_id, temperature, humidity = SensorDataCollector._parse_data(line)
        self.assertEqual(sensor_id, "0")
        self.assertEqual(temperature, 25.5)
        self.assertEqual(humidity, 50.0)

if __name__ == '__main__':
    unittest.main()
