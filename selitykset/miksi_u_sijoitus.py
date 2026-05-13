import marimo

__generated_with = "0.23.1"
app = marimo.App(width="medium")


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Selitys: miksi sijoitus $u = (s-V+e)/(2e)$?

    ## Tilanne ennen sijoitusta

    Kun $t = s$ ja ylärajatermi on poistettu, derivaattaehto on:

    $$\frac{1}{2e}\int_{s-e}^{s+e}\left[\frac{n-1}{2e}\left(\frac{s-V+e}{2e}\right)^{n-2}(V-b(s)) - \left(\frac{s-V+e}{2e}\right)^{n-1}b'(s)\right]dV = 0$$

    Integrandi sisältää toistuvasti lausekkeen $\frac{s-V+e}{2e}$. Se on hankala integroida
    suoraan, koska se esiintyy potenssiin $n-2$ ja $n-1$ sekä kertoimena $(V - b(s))$:lle.

    ## Sijoituksen idea

    Valitaan $u = \dfrac{s-V+e}{2e}$ niin, että tuo toistuva lauseke yksinkertaisesti **muuttuu $u$:ksi**.

    Ratkaistaan muuttujan vaihto:

    $$u = \frac{s-V+e}{2e} \implies V = s+e-2eu \implies dV = -2e\,du$$

    Rajat muuttuvat:
    - $V = s-e$: $u = \dfrac{s-(s-e)+e}{2e} = \dfrac{2e}{2e} = 1$
    - $V = s+e$: $u = \dfrac{s-(s+e)+e}{2e} = \dfrac{0}{2e} = 0$

    Siis $V: s-e \to s+e$ vastaa $u: 1 \to 0$.

    ## Mitä tapahtuu sijoituksen jälkeen

    Integrandi yksinkertaistuu:

    - $\left(\frac{s-V+e}{2e}\right)^{n-2}$ muuttuu $u^{n-2}$:ksi
    - $\left(\frac{s-V+e}{2e}\right)^{n-1}$ muuttuu $u^{n-1}$:ksi
    - $V - b(s) = (s+e-2eu) - b(s)$
    - $dV = -2e\,du$, ja rajat kääntyvät: $\int_1^0 \cdots (-2e\,du) = \int_0^1 \cdots 2e\,du$

    Tuloksena integraali sisältää vain yksinkertaisia polynomeja $u^k$:

    $$\int_0^1 u^{n-2}(\ldots)\,du \quad \text{ja} \quad \int_0^1 u^{n-1}\,du$$

    Nämä integroituvat suoraan kaavalla $\int_0^1 u^k\,du = \dfrac{1}{k+1}$.

    ## Yhteenveto

    Sijoitus tehdään **laskuteknisistä syistä**: se muuttaa hankalan lausekkeen
    $(s-V+e)/(2e)$ yksinkertaiseksi muuttujaksi $u$, jolloin integraalit redusoituvat
    polynomien $u^k$ integroinniksi välillä $[0,1]$.
    """)
    return


@app.cell
def _():
    import marimo as mo
    return (mo,)


if __name__ == "__main__":
    app.run()
