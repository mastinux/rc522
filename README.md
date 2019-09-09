# RC522 - Raspberry Pi 3 B

<!--

https://pimylifeup.com/raspberry-pi-rfid-rc522/

-->

## Wiring

|RC522	|Raspberry|
|-		|-|
|SDA	|Pin 24|
|SCK	|Pin 23|
|MOSI	|Pin 19|
|MISO	|Pin 21|
|GND	|Pin 6|
|RST	|Pin 22|
|3.3v	|Pin 1|

## Setting up

- `sudo raspi-config`

- `-> 5 Interfacing Options`

- `-> P4 SPI`

- `-> Yes`

- `ESC`

	`sudo reboot`

- `lsmod | grep spi`

- se modulo `spi_bcm2835` non è attivo

	`sudo nano /boot/config.txt`

- rimuovi commento (`#`) per `dtparam=spi=on`

	oppure aggiungi `dtparam=spi=on` in coda al file

	`sudo reboot`

## Python

- `sudo apt update`

	`sudo apt upgrade`

- `sudo apt install python3-dev python3-pip`

- `sudo pip3 install spidev`

- `sudo pip3 install mfrc522`

## Write RFID

- `sudo ./scripts/write-rfid.py`

## Read RFID

- `sudo ./scripts/read-rfid.py`


# Screen command on raspberry pi

`# apt install screen`

`$ screen` avvia nuova sessione

`$ command` lancia command nella sessione

`Ctrl + A` + `D` detach dalla sessione

`$ screen -list` visualizza sessioni attive

`$ screen -r` riconnette a sessione

`Ctrl + D` termina sessione
