# RC522 - Raspberry Pi 3 B

<!-- https://pimylifeup.com/raspberry-pi-rfid-rc522/ -->

## Wiring

|RC522	|Raspberry|
|-	|-|
|SDA	|Pin 24|
|SCK	|Pin 23|
|MOSI	|Pin 19|
|MISO	|Pin 21|
|GND	|Pin 6|
|RST	|Pin 22|
|3.3v	|Pin 1|

## Setting up

- `# raspi-config`

- `-> 5 Interfacing Options`

- `-> P4 SPI`

- `-> Yes`

- `ESC`

- `# reboot`

- `$ lsmod | grep spi`

- se modulo `spi_bcm2835` non è attivo

	`# nano /boot/config.txt`

- rimuovi commento (`#`) per `dtparam=spi=on`  
oppure aggiungi `dtparam=spi=on` in coda al file

- `# reboot`

## Python

- `# apt update`

- `# apt upgrade`

- `# apt install python3-dev python3-pip`

- `# pip3 install spidev`

- `# pip3 install mfrc522`

## Write RFID

- `# ./scripts/write-rfid.py`

## Read RFID

- `# ./scripts/read-rfid.py`

---

# screen

- `# apt install screen`

- avviare nuova sessione `$ screen`

- lanciare command nella sessione `$ command`

- detach dalla sessione `Ctrl + A` + `D`

- visualizzare sessioni attive `$ screen -list`

- riconnettere a una sessione `$ screen -r`

- terminare sessione `Ctrl + D`

---

# NFC/RFID

|RFID		|NFC		|Altri|
|-|-|-|
|125 kHz	|13.56 MHz	|868 MHz|
|bassa frequenza|alta frequenza	|Ultra High Frequency (UHF)|
|EM4XX, HID Prox, Indala, Honeywell, AWID, ...|Mifare/DESFire, iClass, Legic, Calypso, pagamenti contactless, ...|Vehicle id, asset tracking, ...|

Ogni card ha un Unique Identifier (UID) di 3-10 byte, molto spesso 4 byte, che è read-only.
L'UID viene impostato dal costruttore.  
T5577 (RFID) o MAGIC UID (NFC) permettono di alterare il proprio UID.
RFID Duplicator o 125kHz-13.56MHz Duplicator fanno da clonatori.

- `$ nfc-list`

- `$ nfc-mfsetuid <X>`

	X: UID da impostare, es. `3b3cf00e`

Applicazioni per smart phone: NFC Tool, Mifare Classic Tool, NFC card emulator.

(RFID) UID non protetto: EM41XX, HID Prox II, Indala  
(NFC) UID non protetto: Mifare  
(NFC) UID protetto: iClass

(RFID) contiene solo UID  
(NFC) contiene UID e DATI

Applicazioni per smart phone: MIFARE++ Ultralight

#### Struttura dati Mifare Classic

|Sector 0|
|-|
|Block 0 - read-only UID|
|Block 1|
|Block 2|
|KeyA \| access right \| KeyB |


|Sector 1|
|-|
|Block 4|
|Block 5|
|Block 6|
|KeyA \| access right \| KeyB |

KeyA e KeyB per diritti di read/write  
access right per le chiavi KeyA e KeyB

Chiavi

- FFFFFFFFFFFF (default)
- A0A1A2A3A4A5
- D3F7D3F7D3F7
- 000000000000
- ...

### Processo crack Mifare Classic

- prova le key di default

- se conosci almeno una key di un settore prova *netsted attack*: sfrutta debolezze in RNG e autentica gli altri settori basandoti sulle autenticazioni precedenti

	`https://github.com/nfc-tools/mfoc`

- prova:

	- *darkside attack*:

	- `https://github.com/nfc-tools/mfcuk`

- prova uno degli attacchi contro i reader

---

##### Miscellaneous

`https://github.com/micolous/metrodroid/`

---

### NFCulT

NFC - 64 byte - 14 pagine da 4 byte

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

##### Lock attack

Procedimento:

- settare il lock bit corretto

Il settore corrispondente al bit settato diventa read-only

Note: rendendo read-only un settore la validatrice non è in grado di scrivere su di esso e il numero di corse resta congelato.

##### Time attack

Precondizioni:

- conoscere il formato del timestamp
- conoscere la posizione del timestamp
- timestamp non cifrato

Processo:

- individuare la pagina giusta
- impostare la data del timestamp
- impostare l'ora del timestamp

##### Replay attack

Precondizioni:

- il biglietto non viene validato tramite un server
- un biglietto valido
- tag clone MIFARE Ultralight

Processo:

- copia il contenuto del biglietto
- modifica le informazioni della chiave
- scrivere sul tag clone

---

- IC type: MIFARE Ultralight EV1 (MF0UL11)
- Memory size: 48 bytes
- Technologies supported: Type A
- Android technology information:
	- android.nfc.tech.NfcA
	- android.nfc.tech.MifareUltralight
	- android.nfc.tech.NdefFormatable

---

MIFARE Classic EV1 MF1S50

1kb
16 sectors, 4 blocks per sectors
64 blocks, 16 bytes per blocks

Type A

---

IEC 14443-3

