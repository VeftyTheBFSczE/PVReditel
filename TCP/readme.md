# P2P Bankovní Systém

Tento projekt představuje P2P (peer-to-peer) bankovní systém, kde každý uzel (node) reprezentuje banku. Systém umožňuje:
- **Vytváření bankovních účtů (AC)**
- **Vklady na účet (AD)**
- **Výběry z účtu (AW)**
- **Kontrolu zůstatku (AB)**
- **Mazání účtu, pokud je zůstatek 0 (AR)**
- **Zjištění celkového součtu finančních prostředků na všech účtech (BA)**
- **Zjištění počtu klientů (BN)**

**Klíčovou vlastností systému** je proxy mechanismus – pokud je účet registrován u jiné banky (identifikován pomocí IP adresy uvedené u účtu), příkaz se automaticky přeposílá na odpovídající bankovní uzel. Tímto způsobem lze posílat peníze na účty, které jsou spravovány jinými bankami v síti.



---

## Instalace

### Požadavky
- Python 3.x (projekt byl testován na Python 3.11)
- Všechny použité moduly (socketserver, socket, threading, logging, json) jsou součástí standardní knihovny Pythonu.

### Stažení projektu
 - Projekt by měl být dostupný ze školních stránek
```


---

## Spuštění

### Konfigurace
Otevřete soubor `config.py` a upravte hodnoty podle vašich potřeb:

BANK_IP = "10.2.7.14"  # Změňte podle potřeby
ALLOWED_PORT_RANGE = range(65525, 65536)
```

### Spuštění serveru
```bash
python main.py
```

Server se spustí a začne naslouchat na definovaném portu.

### Testování
- Připojte se pomocí PuTTY  v režimu **Raw**:

- Nastavte ip adresu a port na který je server spuštěn

---

## Použité zdroje

- **[Python dokumentace k socketserver](https://docs.python.org/3/library/socketserver.html)**  
- **[Python dokumentace k threading a RLock](https://docs.python.org/3/library/threading.html)**  
- **[Python dokumentace k modulu logging](https://docs.python.org/3/library/logging.html)**  
- **Inspirační zdroje z předchozích projektů jako zámky a tcp komunikaci**  


---

## Úvod

Cílem tohoto projektu je demonstrovat koncept P2P bankovního systému, který využívá TCP/IP komunikaci, paralelní obsluhu klientů a persistentní ukládání dat. Klíčovým prvkem je proxy mechanismus, který umožňuje přeposílat příkazy (např. vklady, výběry, kontrola zůstatků) na banky, jež běží na jiných uzlech (různých IP a portech). Projekt je navržen pro školní prostředí a demonstruje znalosti z oblasti síťové komunikace, paralelního programování a správy dat.

