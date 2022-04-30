

#include <Servo.h>

Servo servoX;  // create servo object to control a servo
Servo servoY;  // create servo object to control a 

int potpin = A0;  // analog pin used to connect the potentiometer
int val;    // variable to read the value from the analog pin
int up, down, mid;


void setup() { 
  Serial.begin(9600); //инициализируем последовательную связь на COM порту со скоростью 9600 бод/с
  pinMode(LED_BUILTIN, OUTPUT); //задаем режим работы на вывод данных для контакта 13, к которому подключен светодиод
  digitalWrite (LED_BUILTIN, LOW);
  Serial.println("Hi!, I am Arduino");
  
  servoX.attach(9);
  servoY.attach(8);
}

int[] readCoordinates() {
    int[2] coordinates;
    int v = 0;
    while (Serial.available() > 0) {
        char data = Serial.read();
//       if(data == '1') {
//         v = v*2 + 1;
//       }
//       if(data == '0') {
//         v = v*2;
//       }
        v = 2*v + atoi(data);
    }
    coordinates[0] = v/1024;
    coordinates[1] = v%1024;
}
 
void loop() {
  int[2] coordinates = readCoordinates()
  int x = coordinates[0];
  int y = coordinates[1];

  servoX.write();
  servoY.write();

  delay(1000);
}
