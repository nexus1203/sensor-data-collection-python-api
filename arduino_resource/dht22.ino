#include <DHT.h>
#define DHTPIN 2          // Pin which is connected to the DHT sensor.
#define DHTTYPE DHT22     // Change to DHT11 if you're using that model
DHT dht(DHTPIN, DHTTYPE); // Initialize DHT sensor.
void setup()
{
    Serial.begin(9600);
    dht.begin();
}
void loop()
{
    // Reading temperature or humidity takes about 250 milliseconds!
    float humidity = dht.readHumidity();       // Read humidity (percent)
    float temperature = dht.readTemperature(); // Read temperature as Celsius
    // Check if any reads failed and exit early (to try again).
    if (isnan(humidity) || isnan(temperature))
    {
        Serial.println("Failed to read from DHT sensor!");
        delay(1000);
        return;
    }
    // Assign Sensor an id like  0, 1, 2 etc.
    Serial.print("Sensor: 0")
        Serial.print(","); // comma seperated
    // Print the sensor readings.
    Serial.print("Humidity: ");
    Serial.print(humidity); // unit is %
    Serial.print(",");
    Serial.print("Temperature: ");
    Serial.println(temperature); // unit is *C

    delay(1000); // Wait a second before next update
}