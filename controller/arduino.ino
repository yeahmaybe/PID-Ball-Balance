// double kp=1;
// double kl=0;
// double kd=0;
// unsigned long currentTime, previousTime;
// double elapsedTime;
// double error;
// double input, outputX, outputY, setPoint;
// double cumError, rateError, lastError;
int coordinates[2];
//
// int minAngle = 60,
//     maxAngle = 120,
//     dispersion = 300;
// String data;

double x, y;

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

  while (Serial.available() >= 2) {
      coordinates[0] = Serial.read();
      coordinates[1] = Serial.read();

  }
//   long x = 0;
//   for(int i=0; i<10; i++) {
//     x*=2;
//     if(data[i] == '1') x++;
//   }
//   coordinates[0] = x;
//
//   x = 0;
//   for(int i=10; i<20; i++) {
//     x*=2;
//     if(data[i] == '1') x++;
//   }
//   coordinates[1] = x;
}

// double computePID(double inp) { //double target){
//   currentTime = millis();
//   elapsedTime = (double)(currentTime - previousTime);
//
//   error = inp; //target - inp;
//   cumError += error * elapsedTime;
//   rateError = (error - lastError)/elapsedTime;
//
//   double out = kp * error + kl * cumError + kd * rateError;
//
//   lastError = error;
//   previousTime = currentTime;
//   return out;
// }

void loop() {
    readCoordinates();
    x = coordinates[0];
    y = coordinates[1];
//     outputX = computePID(x);
//     outputY = computePID(y);
//     int outX = constrain(map(outputX, -dispersion, dispersion, minAngle, maxAngle), minAngle, maxAngle);
//     int outY = constrain(map(outputY, -dispersion, dispersion, minAngle, maxAngle), minAngle, maxAngle);

    //Serial.println(x);
    //Serial.print(" ");
    //Serial.println(outputY);
    //
    //Serial.println(outX);
    //Serial.print(" ");
    //Serial.println(outY);

    servoX.write(x);
    servoY.write(y);

    delay(200);
}