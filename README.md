<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->
**Table of Contents**  *generated with [DocToc](https://github.com/thlorenz/doctoc)*

- [NFC/RFID](#nfcrfid)
  - [Mifare](#mifare)
    - [Mifare Classic](#mifare-classic)
    - [Mifare Ultralight](#mifare-ultralight)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

# NFC/RFID

Proximity Inductive Coupling Card (PICC): transponder basato sullo standard ISO1443.
Non ha una batteria, ma si alimenta dal campo magnetico generato da un PCD.

Proximity Coupling Device (PCD): trasmettitore che legge tag PICC.

|RFID		|NFC		|Altri|
|-|-|-|
|125 kHz	|13.56 MHz	|868 MHz|
|bassa frequenza|alta frequenza	|Ultra High Frequency (UHF)|
|EM4XX, HID Prox, Indala, Honeywell, AWID, ...|Mifare/DESFire, iClass, Legic, Calypso, pagamenti contactless, ...|Vehicle id, asset tracking, ...|

Ogni card ha un Unique Identifier (UID) di 3-10 byte, molto spesso 4 byte, che è read-only.
L'UID viene impostato dal costruttore.
T5577 (RFID) o MAGIC UID (NFC) permettono di alterare il proprio UID.
RFID Duplicator o 125kHz-13.56MHz Duplicator fanno da clonatori.

Applicazioni per smart phone: NFC Tools, Mifare Classic Tool, NFC card emulator.

(RFID) UID non protetto: EM41XX, HID Prox II, Indala  
(NFC) UID non protetto: Mifare  
(NFC) UID protetto: iClass

(RFID) contiene solo UID  
(NFC) contiene UID e DATI

Applicazioni per smart phone: MIFARE++ Ultralight

I valori di ATQA, SAK e ATS possono essere usati per identificare il costruttore, il tipo di tag e l'applicazione.

## Mifare

### Mifare Classic

#### Struttura

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

#### Processo crack

- prova le key di default

- se conosci almeno una key di un settore prova *netsted attack*: sfrutta debolezze in RNG e autentica gli altri settori basandoti sulle autenticazioni precedenti

	`https://github.com/nfc-tools/mfoc`

- prova:

	- *darkside attack*:

	- `https://github.com/nfc-tools/mfcuk`

- prova uno degli attacchi contro i reader

### Mifare Ultralight

- IC type: MIFARE Ultralight EV1 (MF0UL11)
- Memory size: 48 bytes
- Technologies supported: Type A
- Android technology information:
	- android.nfc.tech.NfcA
	- android.nfc.tech.MifareUltralight
	- android.nfc.tech.NdefFormatable

UID di 7 byte

