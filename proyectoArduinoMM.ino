void setup() {
  // Configuración de los pines de los LED como salida
  pinMode(2, OUTPUT);
  pinMode(3, OUTPUT);
  pinMode(4, OUTPUT);
  pinMode(5, OUTPUT);
  pinMode(6, OUTPUT);
  pinMode(7, OUTPUT);
  pinMode(8, OUTPUT);
  pinMode(9, OUTPUT);

  // Configuración de los pines de los botones como entrada con pull-up
  pinMode(10, INPUT_PULLUP);
  pinMode(11, INPUT_PULLUP);
  pinMode(12, INPUT_PULLUP);
  pinMode(13, INPUT_PULLUP);
  
  // Iniciar comunicación serial
  Serial.begin(9600);
}

void loop() {
  // Control de los LEDs a través de la comunicación serial
  if (Serial.available() > 0) {
    char estadoMonitor = Serial.read();
    if (estadoMonitor == 'A') {
      digitalWrite(2, HIGH);
      digitalWrite(3, HIGH);
      Serial.println("Grupo Led A Encendidos");
    } else if (estadoMonitor == 'B') {
      digitalWrite(4, HIGH);
      digitalWrite(5, HIGH);
      Serial.println("Grupo Led B Encendidos");
    } else if (estadoMonitor == 'C') {
      digitalWrite(6, HIGH);
      digitalWrite(7, HIGH);
      Serial.println("Grupo Led C Encendidos");
    } else if (estadoMonitor == 'D') {
      digitalWrite(8, HIGH);
      digitalWrite(9, HIGH);
      Serial.println("Grupo Led D Encendidos");
    } else if (estadoMonitor == 'E') {
      digitalWrite(2, LOW);
      digitalWrite(3, LOW);
      digitalWrite(4, LOW);
      digitalWrite(5, LOW);
      digitalWrite(6, LOW);
      digitalWrite(7, LOW);
      digitalWrite(8, LOW);
      digitalWrite(9, LOW);
      Serial.println("Todos los LEDs apagados");
    }
  }
  
  // Control de los LEDs y envío de mensajes a través de los botones físicos
  if (digitalRead(10) == LOW) {
    digitalWrite(2, HIGH);
    digitalWrite(3, HIGH);
    Serial.println("Botón A presionado");
    delay(100); // Debouncing
  } else if (digitalRead(11) == LOW) {
    digitalWrite(4, HIGH);
    digitalWrite(5, HIGH);
    Serial.println("Botón B presionado");
    delay(100);
  } else if (digitalRead(12) == LOW) {
    digitalWrite(6, HIGH);
    digitalWrite(7, HIGH);
    Serial.println("Botón C presionado");
    delay(100);
  } else if (digitalRead(13) == LOW) {
    digitalWrite(8, HIGH);
    digitalWrite(9, HIGH);
    Serial.println("Botón D presionado");
    delay(100);
  }
}




