double kp=1,
       kl=0, 
       kd=0;
unsigned long currentTime, previousTime;
double elapsedTime;
double erroe;
double input, output, setPoint;
double cumError, rstePoint;

void setup() {
  

}

void loop() {
  setPoint = analogRead(A6);
    input = analogRead(A7);
    output = computePID(input);
    delay(100);
    analogWrite(3, output);
    
}

double computePID(double inp){
  currentTime = millis();
  elapsedTime = (double)(currentTime - previousTime);

  error = Setpoint - inp;
  cumError += error * elapsedTime;
  rateError = (error - lastError)/elapsedTime;

  double out = kp * error + kl * cumError + kd * rateError;

  lastError = error;
  previousTime = currentTime;

  return out;
}
