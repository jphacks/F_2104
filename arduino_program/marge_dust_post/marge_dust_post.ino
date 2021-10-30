
#include <WiFi.h>
#include <HTTPClient.h>
#include <Arduino_JSON.h>
#include <Wire.h>

#include "SparkFunCCS811.h" //Click here to get the library: http://librarymanager/All#SparkFun_CCS811

#define CCS811_ADDR 0x5B //Default I2C Address
//#define CCS811_ADDR 0x5A //Alternate I2C Address

CCS811 mySensor(CCS811_ADDR);

const char* ssid = "F660A-YQWG-G";
const char* password = "XTdNgMeR";
char buffer[255];
const char input[] = "{\"result\":true,\"count\":42,\"foo\":\"bar\"}";
const char *host = "https://sv-souji-f2104.herokuapp.com/devices/new";

unsigned long counter = 0;
unsigned long tick = 0;
int pin = 8;
unsigned long duration;
unsigned long starttime;
unsigned long sampletime_ms = 30000;
unsigned long lowpulseoccupancy = 0;
float ratio = 0;
float concentration = 0;

void setup() {
  Serial.begin(115200);
  
  Wire.begin(); //Inialize I2C Hardware

  if (mySensor.begin() == false)
  {
    Serial.print("CCS811 error. Please check wiring. Freezing...");
    while (1)
      ;
  }
  WiFi.begin(ssid, password);
  Serial.println("Connecting");
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
  Serial.println("");
  Serial.print("Connected to WiFi network with IP Address: ");
  Serial.println(WiFi.localIP());

  Serial.println("Timer set to 5 seconds (timerDelay variable), it will take 5 seconds before publishing the first reading.");
   Serial.begin(115200);
  pinMode(2,INPUT);
  starttime = millis();
}

void loop() {
duration = pulseIn(2, LOW);
  lowpulseoccupancy = lowpulseoccupancy+duration;

  if ((millis()-starttime) > sampletime_ms)
  {
    ratio = lowpulseoccupancy/(sampletime_ms*10.0);  // Integer percentage 0=>100
    concentration = 1.1*pow(ratio,3)-3.8*pow(ratio,2)+520*ratio+0.62; // using spec sheet curve
    Serial.print(lowpulseoccupancy);
    Serial.print(",");
    Serial.print(ratio);
    Serial.print(",");
    Serial.println(concentration);
    if (WiFi.status() == WL_CONNECTED) {
  
//  JSONVar myObject = JSON.parse(input);
    Serial.println("creation");
  Serial.println("========");

  JSONVar myObject;

  myObject["module_id"] = "a2:87:5e:60:53:13";
  myObject["type"] = "dust";
//  myObject["value"] = {
//    "detect_times": 1,
//    "": 0,
//    "value": 0
//  };
  myObject["value"]["detect_times"] = lowpulseoccupancy;
  myObject["value"]["detect_ratio"] = ratio;
  myObject["value"]["value"] = concentration;
 
//  myObject["sent_at"] = "2021-10-25 15:01:01.000000";
  Serial.print("myObject.keys() = ");
  Serial.println(myObject.keys());

  // JSON.stringify(myVar) can be used to convert the json var to a String
  String jsonString = JSON.stringify(myObject);

  Serial.print("JSON.stringify(myObject) = ");
  Serial.println(jsonString);

  Serial.println();

//  serializeJson(myObject, Serial);
  Serial.println("");
//  serializeJson(myObject, buffer, sizeof(buffer));

  HTTPClient http;
  http.begin(host);
  http.addHeader("Content-Type", "application/json");
//  int status_code = http.POST((uint8_t*)jsonString, strlen(jsonString));
  int status_code = http.POST(jsonString);
  Serial.printf("status_code=%d\r\n", status_code);
  if( status_code == 200 ){
    Stream* resp = http.getStreamPtr();

//    DynamicJsonDocument json_response(255);
//    deserializeJson(json_response, *resp);

//    serializeJson(json_response, Serial);
    Serial.println("");
  }
  http.end();
    if (mySensor.dataAvailable())
  {
    //If so, have the sensor read and calculate the results.
    //Get them later
    mySensor.readAlgorithmResults();

    Serial.print("CO2[");
    //Returns calculated CO2 reading
    Serial.print(mySensor.getCO2());
    Serial.print("] tVOC[");
    //Returns calculated TVOC reading
    Serial.print(mySensor.getTVOC());
    Serial.print("] millis[");
    //Display the time since program start
    Serial.print(millis());
    Serial.print("]");
    Serial.println();
      JSONVar myObject;

  myObject["module_id"] = "a2:87:5e:60:53:13";
  myObject["type"] = "air";
//  myObject["value"] = {
//    "detect_times": 1,
//    "": 0,
//    "value": 0
//  };
  myObject["value"]["CO2"] = mySensor.getCO2();
  myObject["value"]["tVOC"] = mySensor.getTVOC();
//  myObject["value"]["value"] = concentration;
 
//  myObject["sent_at"] = "2021-10-25 15:01:01.000000";
  Serial.print("myObject.keys() = ");
  Serial.println(myObject.keys());

  // JSON.stringify(myVar) can be used to convert the json var to a String
  String jsonString = JSON.stringify(myObject);

  Serial.print("JSON.stringify(myObject) = ");
  Serial.println(jsonString);

  Serial.println();

//  serializeJson(myObject, Serial);
  Serial.println("");
//  serializeJson(myObject, buffer, sizeof(buffer));

  HTTPClient http;
  http.begin(host);
  http.addHeader("Content-Type", "application/json");
//  int status_code = http.POST((uint8_t*)jsonString, strlen(jsonString));
  int status_code = http.POST(jsonString);
  Serial.printf("status_code=%d\r\n", status_code);
  if( status_code == 200 ){
    Stream* resp = http.getStreamPtr();

//    DynamicJsonDocument json_response(255);
//    deserializeJson(json_response, *resp);

//    serializeJson(json_response, Serial);
    Serial.println("");
  }
  http.end();
  }

  } else {
    Serial.println("Error in WiFi connection");
  }
     lowpulseoccupancy = 0;
    starttime = millis();
  }
  

  delay(10000);
}
