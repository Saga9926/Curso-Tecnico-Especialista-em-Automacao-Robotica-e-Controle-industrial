#include <Arduino.h>
#include <iostream>

// Definição dos pinos dos LEDs (Semáforos)
const int semaforo1Verde = 2;
const int semaforo1Vermelho = 3;
const int semaforo2Verde = 4;
const int semaforo2Amarelo = 5;
const int semaforo2Vermelho = 6;
const int semaforo3Verde = 7;
const int semaforo3Vermelho = 8;

// Definição do pino do sensor de proximidade
const int sensorProximidade = 9;

// Estados da máquina
enum Estado {E1, E2, E3, E4};
Estado estadoAtual = E1;

// Temporizadores
unsigned long tempoAnterior = 0;
const int tempoVerde = 10000;   // 10 segundos
const int tempoAmarelo = 3000;  // 3 segundos
const int delaySensor = 15000;  // 15 segundos de reativação

// Controle do sensor
unsigned long ultimaDeteccao = 0;
bool sensorHabilitado = true;

void setup() {
    pinMode(semaforo1Verde, OUTPUT);
    pinMode(semaforo1Vermelho, OUTPUT);
    pinMode(semaforo2Verde, OUTPUT);
    pinMode(semaforo2Amarelo, OUTPUT);
    pinMode(semaforo2Vermelho, OUTPUT);
    pinMode(semaforo3Verde, OUTPUT);
    pinMode(semaforo3Vermelho, OUTPUT);
    pinMode(sensorProximidade, INPUT);
    
    Serial.begin(9600);
}

void loop() {
    unsigned long tempoAtual = millis();

    // Controle de reativação do sensor
    if (!sensorHabilitado && (tempoAtual - ultimaDeteccao >= delaySensor)) {
        sensorHabilitado = true;
    }

    // Leitura do sensor de proximidade
    bool carroDetectado = digitalRead(sensorProximidade);
    
    switch (estadoAtual) {
        case E1:
            digitalWrite(semaforo1Verde, HIGH);
            digitalWrite(semaforo3Verde, HIGH);
            digitalWrite(semaforo2Vermelho, HIGH);
            digitalWrite(semaforo1Vermelho, LOW);
            digitalWrite(semaforo3Vermelho, LOW);
            digitalWrite(semaforo2Verde, LOW);
            digitalWrite(semaforo2Amarelo, LOW);

            // Se o sensor detectar um carro e estiver habilitado, muda para E2
            if (sensorHabilitado && carroDetectado) {
                ultimaDeteccao = tempoAtual;
                sensorHabilitado = false; // Desativa temporariamente o sensor
                tempoAnterior = tempoAtual;
                estadoAtual = E2;
            }
            break;
            
        case E2:
            digitalWrite(semaforo1Verde, LOW);
            digitalWrite(semaforo3Verde, LOW);
            digitalWrite(semaforo1Vermelho, HIGH);
            digitalWrite(semaforo3Vermelho, HIGH);
            digitalWrite(semaforo2Amarelo, HIGH);
            digitalWrite(semaforo2Vermelho, LOW);
            digitalWrite(semaforo2Verde, LOW);

            if (tempoAtual - tempoAnterior >= tempoAmarelo) {
                tempoAnterior = tempoAtual;
                estadoAtual = E3;
            }
            break;

        case E3:
            digitalWrite(semaforo2Amarelo, LOW);
            digitalWrite(semaforo2Verde, HIGH);
            digitalWrite(semaforo1Vermelho, HIGH);
            digitalWrite(semaforo3Vermelho, HIGH);
            digitalWrite(semaforo1Verde, LOW);
            digitalWrite(semaforo3Verde, LOW);

            if (tempoAtual - tempoAnterior >= tempoVerde) {
                tempoAnterior = tempoAtual;
                estadoAtual = E4;
            }
            break;

        case E4:
            digitalWrite(semaforo2Verde, LOW);
            digitalWrite(semaforo2Amarelo, HIGH);
            digitalWrite(semaforo1Vermelho, HIGH);
            digitalWrite(semaforo3Vermelho, HIGH);
            digitalWrite(semaforo1Verde, LOW);
            digitalWrite(semaforo3Verde, LOW);

            if (tempoAtual - tempoAnterior >= tempoAmarelo) {
                tempoAnterior = tempoAtual;
                estadoAtual = E1;
            }
            break;
    }
}
