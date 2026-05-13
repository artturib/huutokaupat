import marimo

__generated_with = "0.23.1"
app = marimo.App(width="medium")


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Selitys: harkitseeko tarjoaja vain alaspäin suuntautuvia poikkeamia?

    ## Kysymys

    Johtamisessa käytetään ehtoa $t \leq s$, josta seuraa alaraja $s-e$.
    Tarkoittaako tämä, että tarjoaja harkitsee vain alemman "tyypin" esittämistä?

    ## Vastaus: ei — mutta vain $t \leq s$ -tapauksen analysointi riittää

    Tarjoaja voisi periaatteessa harkita mitä tahansa $t$:tä — sekä $t < s$ että $t > s$.

    Mutta ODE johdetaan tasapainoehdosta $\frac{\partial \pi}{\partial t}\big|_{t=s} = 0$.
    Tämä on **derivaatta yhdessä pisteessä** $t = s$. Riittää analysoida integraali
    lähellä $t = s$, ja $t \leq s$ -tapaus antaa sen vasemmanpuoleisen rajan kautta.

    ---

    ## Mitä tapahtuisi $t > s$ -tapauksessa?

    Kun $t > s$, integrointialueen rajat vaihtuvat:

    - **Yläraja:** $\min(s+e,\; t+e) = s+e$ (nyt $s+e < t+e$, joten posteriori sitoo)
    - **Alaraja:** $\max(s-e,\; t-e) = t-e$ (nyt $t-e > s-e$)

    Mutta lisäksi: kun $V < t-e$, kaikki kilpailijat ovat varmuudella tarjoajan
    alapuolella ($P = 1$), joten integraali pitää jakaa kahteen osaan:

    $$\pi(t \mid s) = \frac{1}{2e}\left[
    \int_{s-e}^{t-e} 1^{n-1}(V-b(t))\,dV
    + \int_{t-e}^{s+e}\left(\frac{t-V+e}{2e}\right)^{n-1}(V-b(t))\,dV
    \right]$$

    Analyysi on raskaampi, mutta FOC:sta saadaan täsmälleen sama ODE.

    ---

    ## Miksi kumpikaan suunta ei ole "luontevampi"?

    Tasapainossa $t = s$ on optimaalinen — FOC:n nollakohdassa kumpikin suunta on
    yhtä huono marginaalisesti. Alaspäin poikkeaminen pienentää voittotodennäköisyyttä,
    ylöspäin poikkeaminen nostaa maksettavaa hintaa: nämä voimat tasapainottavat
    toisensa täsmälleen pisteessä $t = s$. Ei ole mitään strategista syytä tarkastella
    vain toista suuntaa.

    $t \leq s$ on **puhtaasti tekninen valinta** — se antaa yksinkertaisemman
    integrointialueen. Koska $\pi(t \mid s)$ on sileä, vasemmanpuoleinen ja
    oikeanpuoleinen derivaatta ovat samat, ja sama ODE saadaan kummastakin.

    ---

    ## Yhteenveto

    - Tarjoaja voi harkita mitä tahansa $t$:tä
    - Derivaatta evaluoidaan pisteessä $t = s$: $\frac{\partial \pi}{\partial t}\big|_{t=s} = 0$
    - $t \leq s$ -tapauksen analyysi riittää ODE:n johtamiseen
    - $t > s$ -tapaus antaa saman ODE:n, analysointi on vain teknisesti raskaampi
    """)
    return


@app.cell
def _():
    import marimo as mo
    return (mo,)


if __name__ == "__main__":
    app.run()
