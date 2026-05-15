import marimo

__generated_with = "0.23.1"
app = marimo.App(width="medium")


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Yhteisvara-huutokauppa: normaalijakautuneet signaalit

    Sama perusrakenne kuin tasajakautuneiden signaalien mallissa, mutta signaalivirhe on
    nyt normaalijakautunut. Analyysimme kattaa:

    - Suljettu second-price huutokauppa — tasapainostrategia numeerisella korjauksella
    - Englantilainen huutokauppa — tippumisstrategia eroaa tasajakaumasta
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 1. Malli

    - Kohteen arvo $V$ — kaikille sama, tuntematon
    - Tarjoaja $i$ saa signaalin $s_i = V + \varepsilon_i$, missä $\varepsilon_i \overset{iid}{\sim} N(0, \sigma^2)$
    - $n$ tarjoajaa, symmetrinen tilanne

    **Ero tasajakaumaan:** Tasajakaumassa $\varepsilon_i \sim U(-e,e)$ virheellä on rajattu
    tukijoukko $[-e, e]$. Normaalijakaumassa virhe voi periaatteessa olla mielivaltaisen suuri,
    joskin $|\varepsilon_i| > 3\sigma$ on epätodennäköistä ($< 0.3\%$).
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 2. Posteriori

    Tasaisella priorilla $V$:lle (tietämättömyys a priori) Bayesin kaavasta seuraa:

    $$V \mid s_i \;\sim\; N(s_i,\; \sigma^2)$$

    Kun tiedossa on $k$ signaalia $s_1, \ldots, s_k$:

    $$V \mid s_1, \ldots, s_k \;\sim\; N\!\left(\bar{s}_k,\; \frac{\sigma^2}{k}\right), \qquad \bar{s}_k = \frac{s_1 + \cdots + s_k}{k}$$

    Jokainen uusi havainto siirtää posterioria kohti signaalien juoksevaa keskiarvoa ja
    kaventaa epävarmuutta. Tämä on normaalijakauman konjugaattiominaisuus: tasajakaumassa
    vastaava ilmiö ei esiinny — siellä vain ääripäät (minimi ja maksimi) rajaavat
    posterioria, eivät väliarvot.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 3. Suljettu second-price huutokauppa

    ### Tasapainostrategia

    Symmetrisessä BNE:ssä tarjoaja $i$ signaalilla $s$ tarjoaa:
    $$b^*(s) = \mathbb{E}[V \mid s_i = s,\; Y_1 = s]$$

    missä $Y_1 = \max_{j \neq i}(s_j)$. Ehto $Y_1 = s$ on "marginaalivoittajan ehto":
    optimaalinen tarjous on se, joka tekee tarjoajan välinpitämättömäksi voittamisen ja
    häviämisen välillä.

    ### Miksi ei suljettua muotoa?

    Tasaisella priorilla ja normaalisignaaleilla:
    $$f(V \mid s_i=s,\; Y_1=s) \;\propto\; \varphi\!\left(\tfrac{s-V}{\sigma}\right)^2
    \cdot \Phi\!\left(\tfrac{s-V}{\sigma}\right)^{n-2}$$

    Tasajakaumassa vastaava posteriori oli tasainen $[s_k-e,\; s_{(1)}+e]$:llä, josta
    saatiin suljettu muoto. Normaalijakaumassa tiheys ei yksinkertaistu polynomiksi,
    joten integrointi tehdään numeerisesti.

    Sijoituksella $z = (V - s)/\sigma$:

    $$b^*(s) = s - \sigma \cdot c(n), \qquad
    c(n) = -\frac{\displaystyle\int_{-\infty}^{\infty} z\;\varphi(z)^2\;\Phi(-z)^{n-2}\,dz}
                  {\displaystyle\int_{-\infty}^{\infty} \varphi(z)^2\;\Phi(-z)^{n-2}\,dz}
    \;\geq\; 0$$

    Erityisesti $c(2) = 0$ symmetriasta ($n=2$:lla $b^*(s) = s$), ja $c(n)$ kasvaa $n$:n
    kasvaessa.
    """)
    return


@app.cell
def _():
    from scipy import integrate as _sci_int
    from scipy.stats import norm as _sci_norm

    def bid_adjustment(n_bidders):
        """c(n) >= 0: winner's curse -korjaus, b*(s) = s - sigma*c(n)"""
        if n_bidders <= 2:
            return 0.0
        def num_fn(z):
            return z * _sci_norm.pdf(z)**2 * _sci_norm.cdf(-z)**(n_bidders - 2)
        def den_fn(z):
            return _sci_norm.pdf(z)**2 * _sci_norm.cdf(-z)**(n_bidders - 2)
        num, _ = _sci_int.quad(num_fn, -15, 15)
        den, _ = _sci_int.quad(den_fn, -15, 15)
        return -num / den

    return (bid_adjustment,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 4. Englantilainen huutokauppa

    ### Tippumisstrategia

    **Ensimmäinen tippuja:** tippuu hinnalla $p_1 = s_{(1)}$ (Nashin tasapaino — poikkeamat
    kumpaankin suuntaan tuottavat $\Delta U < 0$).

    **Toiseksi viimeinen tippuja** (se joka määrää hinnan)**:** Kun jäljellä on kaksi
    pelaajaa, on ratkaistava heidän keskinäinen tasapainonsa. Pelaaja $k$ ehdollistaa
    marginaalitapaukseen "tiputaan samassa hinnassa" eli $s_{k+1} = s_k$. Tällöin hän
    konditionoi aiempiin paljastuneisiin signaaleihin $T = s_{(1)}+\cdots+s_{(k-1)}$
    ($m = k-1$ kappaletta) sekä kahteen omaan signaaliinsa:

    $$p_k = \mathbb{E}[V \mid s_{(1)},\ldots,s_{(k-1)},\; s_{(k)},\; s_{k+1} = s_{(k)}]
    = \frac{T + 2\,s_{(k)}}{m + 2}$$

    Hinnan kannalta ratkaiseva on toiseksi viimeisen tippujan ($k = n-1$) päätös.
    Hänen pudotessaan kaikki $n-2$ matalampaa signaalia ovat jo paljastuneet
    ($T = s_{(1)}+\cdots+s_{(n-2)}$, $m = n-2$):

    $$P = p_{n-1} = \frac{s_{(1)} + \cdots + s_{(n-2)} + 2\,s_{(n-1)}}{n}$$

    **Ero tasajakaumaan:** Tasajakaumassa $p_k = (s_{(1)} + s_{(k)})/2$ — vain alin signaali
    ja oma signaali, kerrottuna kahdella. Normaalijakaumassa mukaan tulevat kaikki
    välisignaalit, koska normaaliposteriori on konjugaatti ja jokainen havainto
    vaikuttaa posterioriodotusarvoon.

    **Kaunis sivutulos:** voittaja maksaa *aina* alle $V$:n:
    $$P = V + \frac{\sigma(Z_{(n-1:n)} - Z_{(n:n)})}{n} < V \quad \text{aina}$$
    koska $Z_{(n-1:n)} < Z_{(n:n)}$ aina. Winner's curse -todennäköisyys on täsmälleen 0.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 5. Odotetut hinnat ja ostajan utility

    Merkitään $Z_{(k:n)}$ = standardinormaalijakauman $k$:s järjestysstatistiikka
    ($n$ i.i.d. $N(0,1)$). Symmetrian nojalla $Z_{(1:n)} \overset{d}{=} -Z_{(n:n)}$.

    Koska $s_{(k)} = V + \sigma Z_{(k:n)}$:

    **Suljettu 2nd price:**
    $$\mathbb{E}[U_{2nd}] = \sigma\!\left(c(n) - \mathbb{E}[Z_{(n-1:n)}]\right)$$

    **Englantilainen:** Voittaja maksaa $P = (s_{(1)}+\cdots+s_{(n-2)}+2s_{(n-1)})/n$.
    Kaikkien $n$ järjestysstatistiikkojen summa on nolla odotusarvossa, joten
    $\mathbb{E}[Z_{(1:n)}]+\cdots+\mathbb{E}[Z_{(n-2:n)}] = -\mathbb{E}[Z_{(n:n)}]-\mathbb{E}[Z_{(n-1:n)}]$:
    $$\mathbb{E}[P_{eng}] = V - \frac{\sigma\!\left(\mathbb{E}[Z_{(n:n)}] - \mathbb{E}[Z_{(n-1:n)}]\right)}{n}$$
    $$\mathbb{E}[U_{eng}] = \frac{\sigma\!\left(\mathbb{E}[Z_{(n:n)}] - \mathbb{E}[Z_{(n-1:n)}]\right)}{n} > 0$$

    Englantilainen tuottaa myyjälle enemmän kuin suljettu second-price (linkage-periaate).
    Järjestysstatistiikkojen odotusarvot lasketaan numeerisesti simulaatiossa.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ---
    ## 6. Simulaatio
    """)
    return


@app.cell
def _(mo):
    slider_V     = mo.ui.slider(10, 200, value=100, step=10, label="Todellinen arvo V")
    slider_n     = mo.ui.slider(2, 20, value=5, step=1, label="Tarjoajien määrä n")
    slider_sigma = mo.ui.slider(1, 50, value=20, step=1, label="Signaalivirhe σ")
    slider_N     = mo.ui.slider(1000, 50000, value=10000, step=1000, label="Simulaatiokerrat N")
    mo.vstack([slider_V, slider_n, slider_sigma, slider_N])
    return slider_N, slider_V, slider_n, slider_sigma


@app.cell
def _(bid_adjustment, np, slider_N, slider_V, slider_n, slider_sigma):
    V     = slider_V.value
    n     = slider_n.value
    sigma = slider_sigma.value
    N_sim = slider_N.value

    rng      = np.random.default_rng(42)
    eps      = rng.standard_normal(size=(N_sim, n)) * sigma
    signals  = V + eps
    sorted_s = np.sort(signals, axis=1)

    cn        = bid_adjustment(n)
    bids_2nd  = signals - sigma * cn
    price_2nd = np.sort(bids_2nd, axis=1)[:, -2]
    utility_2nd = V - price_2nd

    # (s_(1)+...+s_(n-2) + 2*s_(n-1)) / n
    price_eng   = (np.sum(sorted_s[:, :-1], axis=1) + sorted_s[:, -2]) / n
    utility_eng = V - price_eng

    price_naive   = sorted_s[:, -2]
    utility_naive = V - price_naive

    # Järjestysstatistiikkojen odotusarvot (Monte Carlo, V kumoutuu)
    z_mc  = np.sort(np.random.default_rng(99).standard_normal(size=(200000, n)), axis=1)
    Ez_n1 = float(np.mean(z_mc[:, -2]))
    Ez_n  = float(np.mean(z_mc[:, -1]))

    eu_2nd_formula = sigma * (cn - Ez_n1)
    eu_eng_formula = sigma * (Ez_n - Ez_n1) / n
    return (
        Ez_n,
        Ez_n1,
        V,
        cn,
        eu_2nd_formula,
        eu_eng_formula,
        n,
        price_2nd,
        price_eng,
        price_naive,
        sigma,
        utility_2nd,
        utility_eng,
        utility_naive,
    )


@app.cell(hide_code=True)
def _(
    Ez_n,
    Ez_n1,
    V,
    cn,
    eu_2nd_formula,
    eu_eng_formula,
    mo,
    n,
    np,
    price_2nd,
    price_eng,
    price_naive,
    sigma,
    utility_2nd,
    utility_eng,
    utility_naive,
):
    wc_naive = np.mean(utility_naive < 0) * 100
    wc_2nd   = np.mean(utility_2nd   < 0) * 100
    wc_eng   = np.mean(utility_eng   < 0) * 100
    mo.md(f"""
    ### Tulokset: n={n}, σ={sigma}, V={V}

    Numeerinen winner's curse -korjaus: $c(n) = {cn:.4f}$,
    $\\mathbb{{E}}[Z_{{(n-1:n)}}] = {Ez_n1:.4f}$,
    $\\mathbb{{E}}[Z_{{(n:n)}}] = {Ez_n:.4f}$

    | | Naiivi | 2nd rat. | Eng. rat. |
    |---|---|---|---|
    | **E[utility] — kaava** | — | {eu_2nd_formula:.3f} | {eu_eng_formula:.3f} |
    | **E[utility] — simulaatio** | {np.mean(utility_naive):.3f} | {np.mean(utility_2nd):.3f} | {np.mean(utility_eng):.3f} |
    | **P(utility < 0)** | {wc_naive:.1f}% | {wc_2nd:.1f}% | {wc_eng:.1f}% |
    | **E[hinta myyjälle]** | {np.mean(price_naive):.2f} | {np.mean(price_2nd):.2f} | {np.mean(price_eng):.2f} |
    """)
    return


@app.cell
def _(V, n, np, plt, price_2nd, price_eng, price_naive, sigma):
    fig1, ax1 = plt.subplots(figsize=(10, 4))
    all_p = np.concatenate([price_naive, price_2nd, price_eng])
    bins  = np.linspace(all_p.min() - 1, all_p.max() + 1, 60)
    ax1.hist(price_naive, bins=bins, alpha=0.40, color="#e07b39", label="Naiivi")
    ax1.hist(price_2nd,   bins=bins, alpha=0.40, color="#4c8fd6", label="2nd rat.")
    ax1.hist(price_eng,   bins=bins, alpha=0.40, color="#3daa6a", label="Eng. rat.")
    ax1.axvline(V, color="black", linewidth=1.5, linestyle="--", label=f"V = {V}")
    for p_arr, col in [(price_naive, "#e07b39"), (price_2nd, "#4c8fd6"), (price_eng, "#3daa6a")]:
        ax1.axvline(np.mean(p_arr), color=col, linewidth=2)
    ax1.set_xlabel("Voittajan maksama hinta")
    ax1.set_ylabel("Frekvenssi")
    ax1.set_title(f"Maksettujen hintojen jakauma  (n={n}, σ={sigma}, V={V})")
    ax1.legend(fontsize=8)
    fig1.tight_layout()
    fig1
    return


@app.cell
def _(bid_adjustment, n, np, plt):
    ns     = np.arange(2, 31)
    cn_ns  = np.array([bid_adjustment(ni) for ni in ns])

    eu_2nd_ns   = np.zeros(len(ns))
    eu_eng_ns   = np.zeros(len(ns))
    wc_naive_ns = np.zeros(len(ns))
    wc_2nd_ns   = np.zeros(len(ns))
    wc_eng_ns   = np.zeros(len(ns))

    for k, ni in enumerate(ns):
        z_k  = np.sort(np.random.default_rng(seed=k).standard_normal(size=(5000, ni)), axis=1)
        cn_k = cn_ns[k]
        eu_2nd_ns[k]   = cn_k - np.mean(z_k[:, -2])
        eu_eng_ns[k]   = (np.mean(z_k[:, -1]) - np.mean(z_k[:, -2])) / ni
        wc_naive_ns[k] = np.mean(z_k[:, -2] > 0) * 100
        wc_2nd_ns[k]   = np.mean(z_k[:, -2] > cn_k) * 100
        wc_eng_ns[k]   = 0.0   # aina 0: Z_(n-1:n) < Z_(n:n) aina

    fig2, axes = plt.subplots(1, 2, figsize=(12, 4))

    ax_eu = axes[0]
    ax_eu.plot(ns, eu_2nd_ns, color="#4c8fd6", linewidth=2, label="2nd rat.")
    ax_eu.plot(ns, eu_eng_ns, color="#3daa6a", linewidth=2, linestyle="--", label="Eng. rat.")
    ax_eu.axhline(0, color="black", linewidth=1, linestyle="--")
    ax_eu.axvline(n, color="gray", linewidth=1, linestyle=":", alpha=0.8)
    ax_eu.set_xlabel("Tarjoajien määrä n")
    ax_eu.set_ylabel("E[utility] / σ")
    ax_eu.set_title("Odotettu utility n:n funktiona (yksikköinä σ)")
    ax_eu.legend()

    ax_wc = axes[1]
    ax_wc.plot(ns, wc_naive_ns, color="#e07b39", linewidth=2, label="Naiivi")
    ax_wc.plot(ns, wc_2nd_ns,   color="#4c8fd6", linewidth=2, label="2nd rat.")
    ax_wc.plot(ns, wc_eng_ns,   color="#3daa6a", linewidth=2, linestyle="--", label="Eng. rat.")
    ax_wc.axhline(50, color="black", linewidth=1, linestyle="--", alpha=0.5)
    ax_wc.axvline(n, color="gray", linewidth=1, linestyle=":", alpha=0.8, label=f"Nykyinen n={n}")
    ax_wc.set_xlabel("Tarjoajien määrä n")
    ax_wc.set_ylabel("P(utility < 0)  [%]")
    ax_wc.set_title("Winner's curse -todennäköisyys")
    ax_wc.set_ylim(0, 100)
    ax_wc.legend()

    fig2.tight_layout()
    fig2
    return


@app.cell
def _():
    import marimo as mo
    import numpy as np
    import matplotlib.pyplot as plt

    return mo, np, plt


if __name__ == "__main__":
    app.run()
