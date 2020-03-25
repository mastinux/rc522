<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->
**Table of Contents**  *generated with [DocToc](https://github.com/thlorenz/doctoc)*

- [NFCulT](#nfcult)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

# NFCulT

NFC - 64 byte - 16 pagine da 4 byte

||Byte0|Byte1|Byte2|Byte3|
||-|-|-|-|
|Indirizzo pagina|||||
|0|UID (SN0)|UID (SN1)|UID (SN2)|UID (CB0)|
|1|UID (SN3)|UID (SN4)|UID (SN5)|UID (SN6)|
|2|UID (CB1)|Internal|Lock Byte 0|Lock Byte 1|
|3|OTP|OTP|OTP|OTP|
|4-15|Data|Data|Data|Data|

CB0 = 0x88 ⊕ SN0 ⊕ SN1 ⊕ SN2  
CB1 = SN3 ⊕ SN4 ⊕ SN5 ⊕ SN6

Lock Byte 0 = \| L-7 \| L-6 \| L-5 \| L-4 \| L-OTP \| BL-10 to 15 \| BL-4 to 9 \| BL - OTP \|  
Lock Byte 1 = \| L-15 \| L-14 \| L-13 \| L-12 \| L-11 \| L-10 \| L-9 \| L-8 \|

One-Time Programmable (OTP) = default 0x00

## Lock attack

Procedimento:

- settare il lock bit corretto

Il settore corrispondente al bit settato diventa read-only

Note: rendendo read-only un settore la validatrice non è in grado di scrivere su di esso e il numero di corse resta congelato.

## Time attack

Precondizioni:

- conoscere il formato del timestamp
- conoscere la posizione del timestamp
- timestamp non cifrato

Processo:

- individuare la pagina giusta
- impostare la data del timestamp
- impostare l'ora del timestamp

## Replay attack

Precondizioni:

- il biglietto non viene validato tramite un server
- un biglietto valido
- tag clone MIFARE Ultralight

Processo:

- copia il contenuto del biglietto
- modifica le informazioni della chiave
- scrivere sul tag clone

