int trigger=6;
int echo=7;
long dauer=0; 
long entfernung=0; 
int sound = 8;

void setup()
{
Serial.begin (9600); 
pinMode(trigger, OUTPUT); 
pinMode(echo, INPUT);
pinMode(sound, OUTPUT);
}

void loop()
{
digitalWrite(trigger, LOW); 
delay(5);
digitalWrite(trigger, HIGH); 
delay(10);
digitalWrite(trigger, LOW);
dauer = pulseIn(echo, HIGH); 
entfernung = (dauer/2) * 0.03432; 
if (entfernung >= 500 || entfernung <= 0) 
{
//Serial.println("Kein Messwert");
noTone(sound);
}
else{
    Serial.print(entfernung); 
    }
    delay(1000);
    }