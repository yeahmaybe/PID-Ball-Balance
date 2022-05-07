double kp=1,
       kl=0,
       kd=0;
unsigned long currentTime, previousTime;
double elapsedTime;
double error;
double input, output, setPoint;
double cumError, rstePoint;


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

  setPoint = analogRead(A6);
    input = analogRead(A7);
    output = computePID(input);
    delay(100);
    analogWrite(3, output);
  
  servoX.attach(9);
  servoY.attach(8);
}

int[] readCoordinates() {
    int[2] coordinates;
    int v = 0;
    while (Serial.available() > 0) {
        char data = Serial.read();
      if(data == '1') {
        v = v*2 + 1;
      }
      if(data == '0') {
        v = v*2;
      }
    }
    coordinates[0] = v/1024;
    coordinates[1] = v%1024;
}

double computePID(double inp, int target){
  currentTime = millis();
  elapsedTime = (double)(currentTime - previousTime);

  error = target - inp;
  cumError += error * elapsedTime;
  rateError = (error - lastError)/elapsedTime;

  double out = kp * error + kl * cumError + kd * rateError;

  lastError = error;
  previousTime = currentTime;

  return out;
}
 
void loop() {

    int targetX = 0;
    int targetY = 0;

    outputX = computePID(x, targetX);
    outputY = computePID(y, targetY);

    int[2] coordinates = readCoordinates()
    int x = coordinates[0];
    int y = coordinates[1];

    servoX.write(outputX);
    servoY.write(outputY);

    delay(100);
}
