
#include <WiFi.h>
#include <HTTPClient.h>
#include <Arduino_JSON.h>
const char* ssid = "F660A-YQWG-G";
const char* password = "XTdNgMeR";
char buffer[255];
const char input[] = "{\"result\":true,\"count\":42,\"foo\":\"bar\"}";
const char *host = "https://sv-souji-f2104.herokuapp.com/devices/new";

unsigned long counter = 0;
unsigned long tick = 0;

void setup() {
  Serial.begin(115200);

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
  
}

void loop() {
  if (WiFi.status() == WL_CONNECTED) {
    counter++;
  tick = millis();
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
  myObject["value"]["detect_times"] = 1;
  myObject["value"]["detect_ratio"] = 1;
  myObject["value"]["value"] = 1;
 
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


  } else {
    Serial.println("Error in WiFi connection");
  }

  delay(10000);
}
