double kp=1,
kl=0.01,
kd=0.1;
unsigned long currentTime, previousTime;
double elapsedTime;
double error;
double input, outputX, outputY, setPoint;
double cumError, rateError, lastError;
long coordinates[2];
String data ;

double x, y, targetX, targetY;

#include <Servo.h>

Servo servoX; // create servo object to control a servo
Servo servoY; // create servo object to control a

void setup() {
Serial.begin(115200); //инициализируем последовательную связь на COM порту со скоростью 9600 бод/с
Serial.print("Hi!, I am Arduino");

servoX.attach(9);
servoY.attach(8);
}

void readCoordinates() {
  long long v = 0;

  while (Serial.available() > 0) {
      data = Serial.readStringUntil(';');
  }
  long x = 0;
  for(int i=0; i<10; i++) {
    x*=2;
    if(data[i] == '1') x++;
  }
  coordinates[0] = x;

  x = 0;
  for(int i=10; i<20; i++) {
    x*=2;
    if(data[i] == '1') x++;
  }
  coordinates[1] = x;
}

double computePID(double inp, double target){
//  currentTime = millis();
//  elapsedTime = (double)(currentTime - previousTime);
//
    error = target - inp;
//  cumError += error * elapsedTime;
//  rateError = (error - lastError)/elapsedTime;

  double out = kp * error + kl * cumError + kd * rateError;

  lastError = error;
  previousTime = currentTime;
  return error;

}

void loop() {


targetX = 650;
targetY = 350;
readCoordinates();

x = coordinates[0];
y = coordinates[1];
outputX = computePID(x, targetX);
outputY = computePID(y, targetY);
int outX = map(outputX, -300, 300, 10, 170);
int outY = map(outputY, -300, 300, 10, 170);

Serial.print(outX);
Serial.print(" ");
Serial.println(outY);


//servoX.write(90);
//servoY.write(90);

delay(300);
}