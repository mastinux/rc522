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

--------------------------------------------------------------------------------

# screen

- `# apt install screen`

- avviare nuova sessione `$ screen`

- lanciare command nella sessione `$ command`

- detach dalla sessione `Ctrl + A` + `D`

- visualizzare sessioni attive `$ screen -list`

- riconnettere a una sessione `$ screen -r`

- terminare sessione `Ctrl + D`

--------------------------------------------------------------------------------

- MIFARE Classic EV1 MF1S50

	1kb
	16 sectors, 4 blocks per sectors
	64 blocks, 16 bytes per blocks

	Type A

- IEC 14443-3

