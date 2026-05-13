import marimo

__generated_with = "0.23.1"
app = marimo.App(width="medium")


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Selitys: Leibnizin säännön ylärajatermi

    ## Kysymys

    Miksi ylärajatermi pitää erikseen käsitellä? Eikö se ole nolla vain yhdessä
    pisteessä — äärettömän pienellä pätkällä? Ja mikä on $g'(t) = 1$:n merkitys?

    ---

    ## Leibnizin sääntö

    Kun integraalin **yläraja riippuu** derivoitavasta muuttujasta $t$, tavallinen
    derivointisääntö ei riitä — tarvitaan Leibnizin sääntö:

    $$\frac{d}{dt}\int_{a}^{g(t)} f(t,V)\,dV = f(t,g(t))\cdot g'(t) + \int_{a}^{g(t)}\frac{\partial f}{\partial t}\,dV$$

    Sääntö jakaa derivaatan kahteen osaan:

    1. **$f(t,g(t))\cdot g'(t)$** — ylärajan liikkumisen vaikutus: kuinka paljon uutta
       pinta-alaa integraali nielee kun $t$ kasvaa. Tätä kutsutaan **ylärajatermiksi**.
       Se on pistemäinen arvo (ei integraali): integrandin arvo juuri ylärajalla
       $V = g(t)$, kerrottuna ylärajan liikenopeudella $g'(t)$.

    2. **$\int \frac{\partial f}{\partial t}\,dV$** — integrandin itsensä muuttumisen vaikutus.

    ---

    ## Miksi ylärajatermi ylipäätään syntyy?

    Kun $t$ kasvaa, yläraja $g(t) = t+e$ liikkuu oikealle. Integraali "nielee" lisää aluetta.
    Ylärajatermi mittaa, **kuinka paljon uutta pinta-alaa** tulee mukaan per $dt$:

    $$\Delta A \approx f(t,\, g(t)) \cdot g'(t)\,dt$$

    eli integrandin arvo ylärajalla kerrottuna ylärajan siirtymällä $g'(t)\,dt$.

    Tämä on täsmälleen pistemäinen arvo — ei integraali. Ja kyllä: se on nolla täsmälleen
    vain yhdessä pisteessä $V = g(t)$. Mutta Leibnizin sääntö ei kysy "kuinka suuren alueen
    yli tämä on nolla", vaan "mikä on integrandin arvo juuri siinä pisteessä, johon yläraja
    osuu". Se arvo on nolla, joten ylärajatermi on nolla.

    ---

    ## Miksi $g'(t) = 1$?

    Yläraja on $g(t) = t + e$. Derivaatta $t$:n suhteen:

    $$g'(t) = \frac{d}{dt}(t + e) = 1$$

    Merkitys: kun $t$ kasvaa yhdellä, yläraja kasvaa myös yhdellä.
    Jos yläraja olisi esim. $g(t) = 2t$, niin $g'(t) = 2$ — yläraja liikkuisi
    kaksinkertaisella nopeudella ja ylärajatermi kerrottaisiin kahdella.

    Jos yläraja olisi vakio (ei riipu $t$:stä), $g'(t) = 0$ ja koko ylärajatermi
    häviäisi automaattisesti — tavallinen integraali ilman Leibnizia.

    ---

    ## Tässä tapauksessa

    Yläraja on $g(t) = t+e$, $g'(t) = 1$. Integrandin arvo ylärajalla:

    $$f(t,\; t+e) = \left(\frac{t-(t+e)+e}{2e}\right)^{n-1}\cdot((t+e)-b(t))
    = \left(\frac{0}{2e}\right)^{n-1}\cdot(\ldots) = 0$$

    Ensimmäinen tekijä on nolla (voittotodennäköisyys on nolla juuri ylärajalla),
    joten koko ylärajatermi $= 0 \cdot 1 = 0$.

    Vaikka $g'(t) = 1 \neq 0$, se ei pelasta termiä — kerroin on jo nolla.
    """)
    return


@app.cell
def _():
    import marimo as mo
    return (mo,)


if __name__ == "__main__":
    app.run()
