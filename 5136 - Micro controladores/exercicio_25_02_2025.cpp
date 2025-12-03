#include <Arduino.h>

int pinoS1 (D10, output)
//D10 - verde
int pinoS1 (D11, output)
//D11 - amarelo
int pinoS1 (D13, output)
//D13 - vermelho
int pinoS2 (D5, output)
//D5 - verde
int pinoS2 (D6, output)
//D6 - amarelo
int pinoS3 (D7, output)
//D7 - vermelho
main void setup(
    {
        int S1=1
        int S2
        switch
        {
        case S1:
        digitalwrite(D10, HIGH);
        digitalwrite(D11, LOW);
        digitalwrite(D13, LOW);
        digitelwrite(D7, HIGH);
        digitelwrite(D6, LOW);
        digitelwrite(D5, LOW);
        //Espera (15 seg)

        delay(15000)

        digitalwrite(D11, HIGH);
        digitalwrite(D10, LOW);

        break;

        case S2:
        digitalwrite(D13, HIGH);
        digitalwrite(D11, LOW);
        digitalwrite(D10, LOW);
        digitalwrite(D5, HIGH);
        digitalwrite(D6, LOW);
        digitalwrite(D7, LOW);

        delay(15000)

        digitalwrite(D6, HIGH)
        digitalwrite(D5, LOW)

        break;
        }
    }
)

main void loop()