# Počítadlo kroků za týden

Jednoduchý program v Pythonu, který slouží k evidenci týdenní pohybové aktivity uživatele. Program vznikl jako řešení školní úlohy.

## Jak program funguje
1. Spustí cyklus, který se **7krát** (pro každý den v týdnu) zeptá uživatele na počet ušlých kroků.
2. Všechny vstupy průběžně sčítá do celkové hodnoty.
3. Na konci vypíše celkový součet kroků za celý týden a vyhodnotí aktivitu uživatele:
   * **Máš málo pohybu** – pokud je součet menší než 50 000 kroků.
   * **Tvoje aktivita je dobrá** – pokud je součet mezi 50 000 a 80 000 kroky.
   * **Skvělá práce!** – pokud uživatel ušel více než 80 000 kroků.

## Použité technologie
* **Python 3**
* Využití cyklu `for` a podmínek `if`, `elif`, `else`.
