import marimo

__generated_with = "0.23.1"
app = marimo.App(width="medium")


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Selitys: voittotodennäköisyys ja integrointialue 1st price ODE:ssa

    ## Tilanne

    Tarjoaja $i$:n signaali on $s$. Hän harkitsee tarjousta $b(t)$ — ikään kuin esittäisi
    olevansa tyyppiä $t$. Haluamme laskea hänen odotetun hyötynsä:

    $$\pi(t \mid s) = \frac{1}{2e}\int_? \left(\frac{t-V+e}{2e}\right)^{n-1}(V - b(t))\,dV$$

    Kaksi kysymystä: mistä tulee kerroin $\frac{t-V+e}{2e}$, ja miksi integrointialue on
    $(s-e,\; t+e)$ eikä $(s-e,\; s+e)$?

    ---

    ## Osa 1: mistä tulee $\frac{t-V+e}{2e}$?

    Kilpailija $j$:n signaali on $s_j = V + \varepsilon_j$.

    Tarjoaja $i$ voittaa (tarjouksella $b(t)$) jos $b(t) > b(s_j)$ kaikille $j$.
    Koska $b$ on kasvava: $b(t) > b(s_j) \iff t > s_j$.

    Siis tarjoaja voittaa kilpailijan $j$:ltä kun $s_j < t$, eli $V + \varepsilon_j < t$, eli

    $$\varepsilon_j < t - V$$

    Koska $\varepsilon_j \sim U(-e,\, e)$, tämän todennäköisyys on:

    $$P(\varepsilon_j < t-V) = \frac{(t-V) - (-e)}{2e} = \frac{t - V + e}{2e}$$

    Tämä on voimassa kun $t - V \in (-e,\, e)$, eli $V \in (t-e,\, t+e)$.

    | $V$:n arvo | Mitä tapahtuu |
    |---|---|
    | $V < t - e$ | $t - V > e$, eli $\varepsilon_j < t-V$ on **varma** — $P = 1$ |
    | $V \in (t-e,\, t+e)$ | $P = \dfrac{t-V+e}{2e} \in (0,1)$ |
    | $V > t + e$ | $t - V < -e$, eli $\varepsilon_j < t-V$ on **mahdoton** — $P = 0$ |

    Koska $(n-1)$ kilpailijaa ovat riippumattomia:

    $$P(\text{kaikki } s_j < t \mid V) = \left(\frac{t-V+e}{2e}\right)^{n-1}$$

    ---

    ## Osa 2: integrointialueen rajat

    $V$ saa esiintyä integraaleissa vain arvoilla, joilla molemmat seuraavat ehdot pätevät.

    **Ehto A — oma signaali on mahdollinen:**
    $s_i = V + \varepsilon_i = s$ vaatii $\varepsilon_i = s - V \in (-e, e)$, joten

    $$V \in (s-e,\; s+e)$$

    **Ehto B — voitto on mahdollinen:**
    Taulukosta yllä: kun $V > t+e$, voittotodennäköisyys on $0$. Näillä $V$:n arvoilla
    integrandi on nolla, joten ne eivät vaikuta integraaliin. Yläraja voidaan leikata $t+e$:hen.

    **Alaraja:** $\max(s-e,\; t-e)$. Kun $t \leq s$: $t-e \leq s-e$, joten alaraja $= s-e$.

    **Yläraja:** $\min(s+e,\; t+e)$. Kun $t \leq s$: $t+e \leq s+e$, joten yläraja $= t+e$.

    Visuaalisesti ($t \leq s$):

    $$\underbrace{s-e}_{\text{alaraja}} \;\;\leq\;\; V \;\;\leq\;\; \underbrace{t+e}_{\text{yläraja}} \;\;\leq\;\; s+e$$

    Harmaalla alue $(t+e,\; s+e)$: $V$ olisi teknisesti mahdollinen signaalisi perusteella,
    mutta voittotodennäköisyys on siellä $0$ — ei siis vaikutusta integraaliin.

    Tuloksena integrointialue on $(s-e,\; t+e)$, ja integraali:

    $$\pi(t \mid s) = \frac{1}{2e}\int_{s-e}^{t+e} \left(\frac{t-V+e}{2e}\right)^{n-1}(V - b(t))\,dV$$
    """)
    return


@app.cell
def _():
    import marimo as mo
    return (mo,)


if __name__ == "__main__":
    app.run()
