# Huutokaupat — Common Value Auction Simulaatiot

Interaktiiviset Marimo-notebookit huutokauppateoriasta.

## common_value_auction.py

Simuloi ja vertailee kolmea strategiaa kahdessa protokollassa:

| Strategia | Protokolla | Kuvaus |
|---|---|---|
| Naiivi | Suljettu = Englantilainen | Tarjoaja tarjoaa suoraan signaalinsa |
| Suljettu rationaalinen | Vickrey (second-price) | Bid shading: `b = s - δ`, missä `δ = e(n-1)/(n+1)` |
| Englantilainen rationaalinen | Englantilainen | Milgrom–Weber (1982) rekursiivinen tippumisstrategia |

### Teoriaa

- **Common value**: kohteella on yksi todellinen arvo `V`, kukin tarjoaja saa kohinaisen signaalin `sᵢ = V + εᵢ`
- **Winner's curse**: naiivi voittaja maksaa systemaattisesti yli `V`:n kun tarjoajia on yli 3
- **Linkage Principle**: englantilainen huutokauppa tuottaa myyjälle enemmän tuloa kuin suljettu, koska tippumishinnat paljastavat informaatiota joka on positiivisesti korreloitunut `V`:n kanssa

### Ajaminen

```bash
pip install marimo numpy matplotlib
marimo edit common_value_auction.py
```

### Interaktiiviset sliderit

- `V` — todellinen arvo (tuntematon tarjoajille)
- `n` — tarjoajien määrä
- `e` — signaalivirheen laajuus
- `N` — simulaatiokertojen määrä
