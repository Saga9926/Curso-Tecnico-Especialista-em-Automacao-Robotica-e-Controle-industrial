#include <Arduino.h>
#include <WiFi.h>
#include <PubSubClient.h>

// Definição de pinos para sensores e atuadores
#define SENSOR_CAUDAL 34
#define SENSOR_UMIDADE 35
#define SENSOR_FILTRO_1 32
#define SENSOR_FILTRO_2 33
#define SENSOR_FILTRO_3 25
#define SENSOR_FILTRO_4 26
#define LED_VERDE 2
#define LED_AMARELO 4
#define LED_VERMELHO 16
#define ELETRO_VALVULA 5

// Configuração Wi-Fi e MQTT
const char* ssid = "SEU_SSID";
const char* password = "SUA_SENHA";
const char* mqtt_server = "SEU_BROKER_MQTT";
const char* mqtt_topic = "sistema/filtros/alerta";

WiFiClient espClient;
PubSubClient client(espClient);

class Filtro {
public:
    int pinoSensor;
    bool precisaTroca;

    Filtro(int pino) {
        pinoSensor = pino;
        precisaTroca = false;
        pinMode(pinoSensor, INPUT);
    }

    void verificarTroca() {
        precisaTroca = digitalRead(pinoSensor) == HIGH;
    }
};

Filtro filtro1(SENSOR_FILTRO_1);
Filtro filtro2(SENSOR_FILTRO_2);
Filtro filtro3(SENSOR_FILTRO_3);
Filtro filtro4(SENSOR_FILTRO_4);

void setup_wifi() {
    Serial.print("Conectando ao WiFi...");
    WiFi.begin(ssid, password);
    while (WiFi.status() != WL_CONNECTED) {
        delay(500);
        Serial.print(".");
    }
    Serial.println("Conectado ao WiFi");
}

void reconnect_mqtt() {
    while (!client.connected()) {
        Serial.print("Conectando ao MQTT...");
        if (client.connect("ESP32_Client")) {
            Serial.println("Conectado!");
        } else {
            Serial.print("Falha, rc=");
            Serial.print(client.state());
            Serial.println(" Tentando novamente em 5 segundos...");
            delay(5000);
        }
    }
}

void setup() {
    Serial.begin(115200);
    pinMode(SENSOR_CAUDAL, INPUT);
    pinMode(SENSOR_UMIDADE, INPUT);
    pinMode(LED_VERDE, OUTPUT);
    pinMode(LED_AMARELO, OUTPUT);
    pinMode(LED_VERMELHO, OUTPUT);
    pinMode(ELETRO_VALVULA, OUTPUT);
    
    setup_wifi();
    client.setServer(mqtt_server, 1883);
}

void loop() {
    if (!client.connected()) {
        reconnect_mqtt();
    }
    client.loop();

    bool caudalInstavel = digitalRead(SENSOR_CAUDAL);
    bool fugaAgua = digitalRead(SENSOR_UMIDADE);

    filtro1.verificarTroca();
    filtro2.verificarTroca();
    filtro3.verificarTroca();
    filtro4.verificarTroca();

    bool trocaFiltroNecessaria = filtro1.precisaTroca || filtro2.precisaTroca || filtro3.precisaTroca || filtro4.precisaTroca;

    if (caudalInstavel || fugaAgua || trocaFiltroNecessaria) {
        digitalWrite(LED_AMARELO, HIGH);
        digitalWrite(LED_VERDE, LOW);
        digitalWrite(LED_VERMELHO, HIGH);
        digitalWrite(ELETRO_VALVULA, HIGH);
        Serial.println("Atenção: Problema detectado no sistema de filtragem!");
        client.publish(mqtt_topic, "ALERTA: Problema detectado no sistema de filtragem!");
    } else {
        digitalWrite(LED_AMARELO, LOW);
        digitalWrite(LED_VERDE, HIGH);
        digitalWrite(LED_VERMELHO, LOW);
        digitalWrite(ELETRO_VALVULA, LOW);
        Serial.println("Sistema funcionando corretamente.");
    }
    
    delay(2000);
}
