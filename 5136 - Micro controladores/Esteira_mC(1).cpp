#include <iostream>
#include <arduino.h>
#include <thread> // Para usar o delay
#include <chrono> // Para usar o delay

using namespace std;

// Estrutura para representar o Sensor de Proximidade
struct Sensor {
    bool detectaPeca; // Flag para indicar se o sensor detectou uma peça
    Sensor() : detectaPeca(false) {} // Construtor padrão, inicializa como não detectado
};

// Classe que representa o Motor
class Motor {
public:
    bool ligado; // Estado do motor (ligado/desligado)

    Motor() : ligado(false) {} // Construtor padrão, inicializa o motor como desligado

    void ligar() {
        if (!ligado) {
            ligado = true;
            cout << "Motor ligado!" << endl;
        }
    }

    void desligar() {
        if (ligado) {
            ligado = false;
            cout << "Motor desligado!" << endl;
        }
    }
};

// Classe que representa a Esteira
class Esteira {
private:
    Motor motor1, motor2;    // Dois motores
    Sensor sensor1, sensor2; // Dois sensores

public:
    // Método para detectar a peça no sensor1
    void detectarPeca1() {
        sensor1.detectaPeca = true;
        cout << "Sensor 1 detectou a peça!" << endl;

        // Desliga o motor 1 após um delay
        motor1.desligar();
        // Aguarda um tempo de delay antes de ligar o motor 2
        this_thread::sleep_for(chrono::seconds(2));
        motor2.ligar();
    }

    // Método para detectar a peça no sensor2
    void detectarPeca2() {
        sensor2.detectaPeca = true;
        cout << "Sensor 2 detectou a peça!" << endl;

        // Desliga o motor 2 após um delay
        motor2.desligar();
        // Aguarda um tempo de delay antes de ligar o motor 1
        this_thread::sleep_for(chrono::seconds(2));
        motor1.ligar();
    }

    // Método para iniciar a operação dos motores com sensores
    void iniciarEsteira() {
        motor1.ligar(); // Inicializa o motor 1
        motor2.ligar(); // Inicializa o motor 2
        cout << "Esteira em funcionamento..." << endl;
    }

    // Método para parar a esteira
    void pararEsteira() {
        motor1.desligar();
        motor2.desligar();
        cout << "Esteira parada!" << endl;
    }
};

int main() {
    Esteira esteira; // Criação de um objeto de esteira

    // Inicia a esteira
    esteira.iniciarEsteira();

    // Simulação de detecção de peças pelos sensores
    esteira.detectarPeca1(); // Simula a detecção pela peça do sensor 1
    this_thread::sleep_for(chrono::seconds(3)); // Aguarda um tempo para simulação
    esteira.detectarPeca2(); // Simula a detecção pela peça do sensor 2

    // Para a esteira após o processo
    esteira.pararEsteira();

    return 0;
}