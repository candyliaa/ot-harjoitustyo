```mermaid
classDiagram
    Monopolipeli "1" -- "2" Noppa
    Monopolipeli "1" -- "1" Pelilauta
    Monopolipeli "1" -- "1" Aloitusruutu
    Monopolipeli "1" -- "1" Vankila
    Ruutu "1" -- "1" Ruutu : toiminto
    Aloitusruutu "1" -- "40" Ruutu
    Vankila "1" -- "40" Ruutu
    Sattuma "3" -- "40" Ruutu
    Sattuma "1" -- "1" Sattuma : kortti
    Asema "4" -- "40" Ruutu
    Laitos "2" -- "40" Ruutu
    Pelilauta "1" -- "40" Ruutu
    Katu "22" -- "40" Ruutu
    Talo "4" -- "22" Katu
    Hotelli "1" -- "22" Katu
    Katu "1" -- "1" Pelaaja
    Raha "1" -- "1" Pelaaja
    Ruutu "1" -- "1" Ruutu : seuraava
    Ruutu "1" -- "0..8" Pelinappula
    Pelinappula "1" -- "1" Pelaaja
    Pelaaja "2..8" -- "1" Monopolipeli
```
