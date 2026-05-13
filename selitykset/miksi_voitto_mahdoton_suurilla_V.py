import marimo

__generated_with = "0.23.1"
app = marimo.App(width="medium")


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Selitys: miksi voittaminen on mahdotonta kun $V > t+e$?

    ## Kysymys

    Integrointialueen yläraja on $t+e$ eikä $s+e$, koska voittotodennäköisyys on nolla
    kun $V > t+e$. Tarkoittaako tämä, että tarjoaja harkitsee vain poikkeamia $t$,
    jotka ovat "V:n posteriorin sisällä"?

    ## Vastaus: ei — se on matemaattinen seuraus, ei oletus

    Tarjoaja integroi $V$:n yli koko posteriorinsa $(s-e,\; s+e)$ yli. Hän ei rajoita
    poikkeamiaan mitenkään. Mutta:

    Kun $V > t+e$, kilpailijan signaali $s_j = V + \varepsilon_j > (t+e) + (-e) = t$
    **aina**, riippumatta $\varepsilon_j$:n arvosta.

    Siis kun $V > t+e$: kaikilla kilpailijoilla $s_j > t$ varmuudella, joten tarjoaja
    **ei voi voittaa** — voittotodennäköisyys on rakenteellisesti nolla.

    Nämä $V$:n arvot ovat kyllä posteriorissa mahdollisia (jos $t+e < s+e$, eli $t < s$),
    mutta ne eivät vaikuta integraaliin koska integrandi on siellä nolla.

    ---

    ## Konkreettinen esimerkki

    Olkoon $e = 10$, $s = 100$, $t = 90$ (tarjoaja harkitsee poikkeamaa alaspäin).

    - Tarjoajan posteriori: $V \in (90,\; 110)$
    - Voittaminen mahdollista: $V \leq t+e = 100$
    - Integrointialue: $V \in (90,\; 100)$
    - Alue $(100,\; 110)$: posteriorissa mahdollinen, mutta jokaisella kilpailijalla
      $s_j = V + \varepsilon_j > 100 - 10 = 90 = t$... ei, tarkemmin:
      kun $V > 100$, $s_j = V + \varepsilon_j > 100 + (-10) = 90 = t$ ei vielä riitä.

    Tarkemmin: $s_j > t$ varmuudella kun $V + \varepsilon_j > t$ kaikilla $\varepsilon_j \in (-e,e)$,
    eli kun $V - e > t$, eli $V > t + e = 100$. ✓

    Niin: kun $V = 105$, kilpailijan signaali $s_j = 105 + \varepsilon_j \in (95, 115)$,
    ja koska $95 > t = 90$, kilpailija on **aina** tarjoajan yläpuolella. Voitto mahdoton.

    ---

    ## Yhteenveto

    Ylärajan $t+e$ ei ole tarjoajan valinta eikä rajoite posteriorille.
    Se on kohta, jossa $V$ on niin suuri, että kilpailijoiden signaalit ylittävät $t$:n
    rakenteellisesti — ei sattumalta vaan väistämättä.

    Integraali luonnollisesti katkeaa sinne, koska integrandi on nolla sen yläpuolella.
    """)
    return


@app.cell
def _():
    import marimo as mo
    return (mo,)


if __name__ == "__main__":
    app.run()
