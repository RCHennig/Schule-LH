const int buttonPin = 13;  // the number of the pushbutton pin
const int ledPin = 10;    // the number of the LED pin


int buttonState = 0;  // variable for reading the pushbutton status
int state = 0;

void setup() {
  // initialize the LED pin as an output:
  pinMode(ledPin, OUTPUT);
  // initialize the pushbutton pin as an input:
  pinMode(buttonPin, INPUT);
}

void loop() {
  // read the state of the pushbutton value:
  
  buttonState = digitalRead(buttonPin);

  // check if the pushbutton is pressed. If it is, the buttonState is HIGH:

  if (buttonState == HIGH && state == 0) {
    //delay(70);
    digitalWrite(ledPin, HIGH);
    //delay(10);
    state = 1;
    //delay(100);
  }else if (buttonState == HIGH && state == 1){
    //delay(70);
    digitalWrite(ledPin, LOW);
    //delay(10);
    state = 0;
    //delay(100);
  }else{
    //delay(100);
  }
 delay(200); //while schleife

  }