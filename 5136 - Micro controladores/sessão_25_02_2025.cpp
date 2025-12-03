#include <arduino.h>

enum state
{
    S1=1
    S2
};

State state = S1;

void setup()
{
    //configurar os pinos como saidas
    //semáforo 1 verde
    pinMode (D10,output)
    //semáforo 1 amarelo
    pinMode (D11,output)
    //semáforo 1 vermelho
    pinMode (D12,output)
    //semáforo 2 verde
    pinMode (D10,output)
    //semáforo 2 amarelo
    pinMode (D11,output)
    //semáforo 2 vermelho
    pinMode (D12,output)

}

void loop()
{
    //criar máquina de estados
    switch (state)
    {
        case S1:
        //Semáforo 1 a verde
        digitalwrite(D10,High)

        //Semáforo 2 a vermelho
        digitalwrite(D11,Low)

        //semáforo 1 a amarelo
        digitalwrite(D11,High)

        //semáforo 1 desliga o verde
        digitalwrite(D10,Low)

        // espera
        delay (5000)

        //Semáforo 1 a amarelo
    }
}