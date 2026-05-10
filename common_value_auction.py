import marimo

__generated_with = "0.23.4"
app = marimo.App(width="medium")


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Common Value Auction — Simulaatio

    ## 1. Malli

    Kohteella on **yksi todellinen arvo** $V$, joka on sama kaikille tarjoajille mutta tuntematon.
    Kukin $n$ tarjoajista saa yksityisen **signaalin**

    $$s_i = V + \varepsilon_i, \qquad \varepsilon_i \overset{\text{iid}}{\sim} \text{Uniform}(-e,\, e)$$

    Tarjoaja tietää oman signaalinsa $s_i$ mutta ei muiden signaaleja eikä $V$:tä.

    ---

    ## 2. Protokollat

    ### 2.1 Suljettu second-price auction (Vickrey)

    Jokainen tarjoaja jättää salaisen tarjouksen. Korkein tarjoaja voittaa ja **maksaa toiseksi
    korkeimman tarjouksen**.

    ### 2.2 Englantilainen huutokauppa

    Hinta nousee jatkuvasti. Kukin tarjoaja **pysyy mukana kunnes hinta ylittää oman strategiansa
    mukaisen kynnyksen**. Viimeisenä jäljelle jäävä voittaa ja maksaa hinnan, jolla toiseksi
    viimeinen tippui pois.

    > **Huomio (naiivi):** naiiveilla strategioilla molemmat protokollat tuottavat identtisen
    > tuloksen — voittaja on se, jonka signaali $s_{(n:n)}$ on korkein, ja hinta on $s_{(n-1:n)}$.

    ---

    ## 3. Järjestysstatistiikat

    Merkitään $\varepsilon_{(k:n)}$ signaalivirheiden $k$:nneksi pienimmäksi arvoksi
    (kasvavassa järjestyksessä). Koska $\varepsilon_i \sim \text{Uniform}(-e, e)$,
    $k$:nnen järjestysstatistiikan odotusarvo on

    $$\mathbb{E}[\varepsilon_{(k:n)}] = -e + 2e \cdot \frac{k}{n+1} = e \cdot \frac{2k - n - 1}{n+1}$$

    Erityisesti:

    | Järjestysstatistiikka | Odotusarvo |
    |---|---|
    | Maksimi $\varepsilon_{(n:n)}$ | $\displaystyle e\cdot\frac{n-1}{n+1}$ |
    | Toiseksi suurin $\varepsilon_{(n-1:n)}$ | $\displaystyle e\cdot\frac{n-3}{n+1}$ |

    ---

    ## 4. Naiivi strategia

    Tarjoaja tarjoaa suoraan signaalinsa: $b_i = s_i$.

    **Voittajan utility:**

    $$U_{\text{naiivi}} = V - s_{(n-1:n)} = -\varepsilon_{(n-1:n)}$$

    **Odotettu utility:**

    $$\mathbb{E}[U_{\text{naiivi}}] = e \cdot \frac{3-n}{n+1}$$

    Tämä on **negatiivinen kun $n > 3$** — winner's curse iskee.

    ---

    ## 5. Suljettu rationaalinen strategia

    Rationaalinen tarjoaja huomaa: *jos voitan, signaalini oli korkein, eli $\varepsilon_i = \varepsilon_{(n:n)}$.*
    Optimaalinen tarjous on ehdollinen odotusarvo siitä, mitä kohde on *jos voitan*:

    $$b_i^* = \mathbb{E}[V \mid s_i,\; \varepsilon_i = \varepsilon_{(n:n)}] = s_i - \underbrace{e\cdot\frac{n-1}{n+1}}_{\delta}$$

    **Odotettu utility:**

    $$\mathbb{E}[U_{\text{suljettu, rat}}] = \frac{2e}{n+1} > 0 \quad \text{aina}$$

    Tasapainoehto: marginaalivoitoilla $\mathbb{E}[U] = 0$, joten sheidauksesta ei kannata
    poiketa kumpaan suuntaan.

    ---

    ## 6. Englantilainen rationaalinen strategia

    Englantilaisen huutokaupan avoimuus paljastaa informaatiota: kun tarjoaja tippuu pois
    hinnalla $p_k$, muut oppivat hänen signaalinsa $s_{(k:n)} \approx p_k$.

    **Milgrom–Weber (1982) tasapainoehto** ("almost tied"):
    tarjoaja tippuu pois hinnalla, jolla hän olisi tasapelissä toiseksi viimeisen kanssa:

    $$b^*_j = \mathbb{E}\!\left[V \;\middle|\; s_j,\; s_{(1)}=p_1,\ldots,s_{(k)}=p_k,\; s_\text{tied}=s_j\right] = \frac{2s_j + \sum_{i=1}^k p_i}{k+2}$$

    Oma signaali lasketaan **kahdesti** (oma + kuvitteellinen tasapelissä olija).
    Tästä seuraa rekursiivinen tippumissekvenssi:

    $$\boxed{p_k = \frac{2\,s_{(k:n)} + \sum_{j=1}^{k-1} p_j}{k+1}}, \qquad k = 1, \ldots, n-1$$

    Voittaja maksaa $p_{n-1}$.

    **Kaavan intuitio merkki merkiltä:**

    - $p_k$ — hinta, jolla $k$:nneksi matalin tarjoaja tippuu pois. Jokainen dropout paljastaa
      signaalinsa: $s_{(k:n)} \approx p_k$.

    - $s_{(k:n)}$ — tippuvan tarjoajan oma signaali. Se on kohinainen mittaus $V$:stä:
      $s_{(k:n)} = V + \varepsilon_{(k:n)}$.

    - $2\,s_{(k:n)}$ — oma signaali lasketaan **kahdesti**. Tämä tulee siitä, että tippumispäätös
      on relevantti vain tilanteessa, jossa olet *juuri* tasapelissä seuraavaksi tippuvan kanssa.
      Tasapeli tarkoittaa: kuvittele, että joku toinen tarjoaja on täsmälleen sinun signaalisi
      kohdalla. Nyt sinulla on käytettävissä $k+1$ havaintoa $V$:stä — $k-1$ paljastunutta
      dropoutia plus oma signaali kahdesti (oma $+$ kuvitteellinen tasapelissä olija).

    - $\sum_{j=1}^{k-1} p_j$ — kaikkien aiempien dropoutien hinnat, jotka ovat paljastaneet
      $k-1$ signaalia $V$:stä.

    - Jako $(k+1)$ — nimittäjä on havaintojen lukumäärä $(k-1) + 2 = k+1$, joten kaava on
      yksinkertaisesti **kaikkien käytettävissä olevien havaintojen keskiarvo** $V$:stä.
      Tämä on paras estimaatti $V$:stä litteällä priorilla.

    Koko kaava sanottuna auki: *tipun pois sillä hinnalla, jolla — jos olisin tasapelissä
    toisen kanssa — paras estimaattini $V$:stä täsmälleen yhtäläinen hinnan kanssa.
    Alla siitä kannattaa jäädä, yllä siitä kannattaa nousta.*

    **Esimerkki $n=4$:**

    $$p_1 = s_{(1:4)}, \qquad p_2 = \frac{s_{(1:4)} + 2\,s_{(2:4)}}{3}, \qquad p_3 = \frac{2\,s_{(3:4)} + p_1 + p_2}{4}$$

    **Odotettu utility** (johdetaan rekursiivisesti järjestysstatistiikkojen odotusarvoista):

    | $n$ | $\mathbb{E}[U_{\text{eng, rat}}]$ | $\mathbb{E}[U_{\text{suljettu, rat}}]$ |
    |---|---|---|
    | 2 | $e/3$ | $2e/3$ |
    | 3 | $e/6$ | $e/2$ |
    | 4 | $2e/15$ | $2e/5$ |
    | 5 | $13e/90$ | $e/3$ |

    **Linkage Principle** (Milgrom–Weber 1982): informaatiopaljastus hyödyttää myyjää —
    englantilainen rationaalinen tuottaa aina pienemmän utiliteetin voittajalle kuin suljettu rationaalinen.

    **Miksi paljastuva informaatio nostaa hintaa eikä laske sitä?**

    Ensiajatus saattaa olla: näen muiden tippuvan matalilla hinnoilla → päivitän $V$:n estimaattini
    alaspäin → tipun aikaisemmin → hinta laskee. Mutta tämä vertaa väärään lähtökohtaan.

    Oikea vertailu on suljettuun *rationaaliseen* strategiaan. Siinä toiseksi korkein tarjoaja
    sheidaa signaalinsa kiinteällä $\delta$:lla riippumatta siitä, mitä muut tarjosivat:

    $$\text{suljettu hinta} = s_{(n-1:n)} - \delta$$

    Sheidaus $\delta$ on vakio — se ei riipu $V$:stä. Myyjä menettää aina saman summan.

    Englantilaisessa toiseksi korkein tarjoaja sen sijaan **päivittää kynnystään** havaittujen
    dropoutien perusteella. Kun dropoutit tapahtuvat korkeilla hinnoilla (merkki siitä, että $V$
    on korkea), toiseksi korkeimman kynnys nousee. Kun dropoutit ovat matalia ($V$ matala),
    kynnys laskee.

    Tämä tarkoittaa: **englantilaisessa hinta on positiivisesti korreloitunut $V$:n kanssa**,
    suljetussa ei. Voittaja saa "alennuksen" $\delta$ vain suljetussa — ja se on *vakio*,
    riippumaton siitä onko $V$ korkea vai matala.

    Konkreettisesti: kun $V$ on korkea ja voittaminen on arvokkainta, englantilaisessa hinta
    nousee eniten (korkeat dropoutit nostavat toiseksi korkeimman kynnystä). Juuri silloin
    voittajan surplus pienenee eniten. Myyjä saa siis suuremman osuuden nimenomaan
    hyvistä realisaatioista.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ---
    ## 7. Simulaatio
    """)
    return


@app.cell
def _(mo):
    slider_V = mo.ui.slider(10, 200, value=100, step=10, label="Todellinen arvo V")
    slider_n = mo.ui.slider(2, 20, value=5, step=1, label="Tarjoajien määrä n")
    slider_e = mo.ui.slider(1, 50, value=20, step=1, label="Signaalivirhe e")
    slider_N = mo.ui.slider(1000, 50000, value=10000, step=1000, label="Simulaatiokerrat N")
    mo.vstack([slider_V, slider_n, slider_e, slider_N])
    return slider_N, slider_V, slider_e, slider_n


@app.cell
def _(np, slider_N, slider_V, slider_e, slider_n):
    V = slider_V.value
    n = slider_n.value
    e = slider_e.value
    N_sim = slider_N.value
    rng = np.random.default_rng(42)

    # Signals: (N_sim, n)
    eps = rng.uniform(-e, e, size=(N_sim, n))
    signals = V + eps
    sorted_s = np.sort(signals, axis=1)  # ascending

    # --- Naive strategy (suljettu = englantilainen) ---
    price_naive   = sorted_s[:, -2]
    utility_naive = V - price_naive

    # --- Suljettu rationaalinen ---
    delta          = e * (n - 1) / (n + 1)
    bids_rational  = signals - delta
    sorted_rat     = np.sort(bids_rational, axis=1)
    price_rational = sorted_rat[:, -2]
    utility_rational = V - price_rational

    # --- Englantilainen rationaalinen (Milgrom-Weber) ---
    cumsums_eng      = np.zeros(N_sim)
    dropout_eng      = np.zeros((N_sim, n - 1))
    for _k in range(1, n):
        _p = (2 * sorted_s[:, _k - 1] + cumsums_eng) / (_k + 1)
        dropout_eng[:, _k - 1] = _p
        cumsums_eng += _p
    price_english_rational  = dropout_eng[:, -1]
    utility_english_rational = V - price_english_rational

    # --- Analyyttiset odotusarvot ---
    eu_naive_formula    = e * (3 - n) / (n + 1)
    eu_sealed_formula   = 2 * e / (n + 1)

    def _eu_eng(n_val, e_val):
        mu = np.array([e_val * (2*k - n_val - 1) / (n_val + 1) for k in range(1, n_val)])
        cum_err = 0.0
        for k in range(1, n_val):
            err = (2 * mu[k - 1] + cum_err) / (k + 1)
            cum_err += err
        return -err

    eu_english_formula = _eu_eng(n, e)

    return (
        V, n, e, N_sim, rng, eps, signals, sorted_s,
        price_naive, utility_naive,
        delta, bids_rational, price_rational, utility_rational,
        price_english_rational, utility_english_rational,
        eu_naive_formula, eu_sealed_formula, eu_english_formula,
    )


@app.cell(hide_code=True)
def _(
    V, n, e, delta, mo, np,
    eu_naive_formula, eu_sealed_formula, eu_english_formula,
    price_naive, price_rational, price_english_rational,
    utility_naive, utility_rational, utility_english_rational,
):
    wc_naive  = np.mean(utility_naive < 0) * 100
    wc_sealed = np.mean(utility_rational < 0) * 100
    wc_eng    = np.mean(utility_english_rational < 0) * 100
    mo.md(f"""
    ### Tulokset: n={n}, e={e}, V={V}, δ={delta:.2f}

    | | Naiivi | Suljettu rat. | Eng. rat. |
    |---|---|---|---|
    | **E[utility] — kaava** | {eu_naive_formula:.3f} | {eu_sealed_formula:.3f} | {eu_english_formula:.3f} |
    | **E[utility] — simulaatio** | {np.mean(utility_naive):.3f} | {np.mean(utility_rational):.3f} | {np.mean(utility_english_rational):.3f} |
    | **P(utility < 0)** | {wc_naive:.1f}% | {wc_sealed:.1f}% | {wc_eng:.1f}% |
    | **E[hinta myyjälle]** | {np.mean(price_naive):.2f} | {np.mean(price_rational):.2f} | {np.mean(price_english_rational):.2f} |

    Linkage Principle: myyjän saama hinta — eng. rat. ({np.mean(price_english_rational):.2f})
    {">" if np.mean(price_english_rational) > np.mean(price_rational) else "<"}
    suljettu rat. ({np.mean(price_rational):.2f})
    """)
    return wc_naive, wc_sealed, wc_eng


@app.cell
def _(V, e, n, np, plt, utility_naive, utility_rational, utility_english_rational):
    fig1, ax1 = plt.subplots(figsize=(9, 4))
    all_u = np.concatenate([utility_naive, utility_rational, utility_english_rational])
    bins = np.linspace(all_u.min() - 2, all_u.max() + 2, 60)
    ax1.hist(utility_naive,             bins=bins, alpha=0.45, color="#e07b39", label="Naiivi")
    ax1.hist(utility_rational,          bins=bins, alpha=0.45, color="#4c8fd6", label="Suljettu rat.")
    ax1.hist(utility_english_rational,  bins=bins, alpha=0.45, color="#3daa6a", label="Eng. rat.")
    ax1.axvline(0, color="black", linewidth=1.2, linestyle="--", label="Utility = 0")
    for u_arr, col in [
        (utility_naive, "#e07b39"),
        (utility_rational, "#4c8fd6"),
        (utility_english_rational, "#3daa6a"),
    ]:
        ax1.axvline(np.mean(u_arr), color=col, linewidth=2)
    ax1.set_xlabel("Voittajan utility  (V − maksettu hinta)")
    ax1.set_ylabel("Frekvenssi")
    ax1.set_title(f"Voittajan utiliteetin jakauma  (n={n}, e={e}, V={V})")
    ax1.legend()
    fig1.tight_layout()
    fig1
    return fig1, ax1, bins, all_u


@app.cell
def _(V, bids_rational, delta, e, n, np, plt, signals):
    idx = np.random.default_rng(0).integers(0, signals.shape[0], 300)
    s_sample = signals[idx].ravel()
    b_sample = bids_rational[idx].ravel()

    fig2, ax2 = plt.subplots(figsize=(6, 5))
    ax2.scatter(s_sample, b_sample, alpha=0.25, s=12, color="#4c8fd6", label="Rationaalinen tarjous")
    s_line = np.linspace(s_sample.min(), s_sample.max(), 100)
    ax2.plot(s_line, s_line, "k--", linewidth=1, label="b = s  (naiivi)")
    ax2.plot(s_line, s_line - delta, color="#4c8fd6", linewidth=2, label=f"b = s − δ  (δ={delta:.2f})")
    ax2.axvline(V, color="gray", linewidth=1, linestyle=":", label=f"V={V}")
    ax2.set_xlabel("Signaali $s_i$")
    ax2.set_ylabel("Tarjous $b_i$")
    ax2.set_title(f"Bid sheidaus — suljettu rationaalinen  (n={n}, e={e})")
    ax2.legend(fontsize=8)
    fig2.tight_layout()
    fig2
    return fig2, ax2, idx, s_sample, b_sample, s_line


@app.cell
def _(plt, np, e, n):
    ns = np.arange(2, 31)
    eu_naive_n  = e * (3 - ns) / (ns + 1)
    eu_sealed_n = 2 * e / (ns + 1)

    def _eu_eng_arr(e_val):
        out = []
        for n_val in ns:
            mu = np.array([e_val*(2*k-n_val-1)/(n_val+1) for k in range(1, n_val)])
            cum_err = 0.0
            for k in range(1, n_val):
                err = (2*mu[k-1] + cum_err) / (k+1)
                cum_err += err
            out.append(-err)
        return np.array(out)

    eu_english_n = _eu_eng_arr(e)

    wc_naive_n = np.array([
        np.mean(
            -np.sort(np.random.default_rng(seed=k).uniform(-e, e, size=(5000, ni)), axis=1)[:, -2] < 0
        )
        for k, ni in enumerate(ns)
    ])

    fig3, axes = plt.subplots(1, 2, figsize=(12, 4))

    ax_eu = axes[0]
    ax_eu.plot(ns, eu_naive_n,  color="#e07b39", linewidth=2, label="Naiivi")
    ax_eu.plot(ns, eu_sealed_n, color="#4c8fd6", linewidth=2, label="Suljettu rat.")
    ax_eu.plot(ns, eu_english_n, color="#3daa6a", linewidth=2, linestyle="--", label="Eng. rat.")
    ax_eu.axhline(0, color="black", linewidth=1, linestyle="--")
    ax_eu.axvline(n, color="gray", linewidth=1, linestyle=":", alpha=0.8)
    ax_eu.set_xlabel("Tarjoajien määrä n")
    ax_eu.set_ylabel("E[voittajan utility]")
    ax_eu.set_title("Odotettu utility n:n funktiona")
    ax_eu.legend()

    ax_wc = axes[1]
    ax_wc.plot(ns, wc_naive_n * 100, color="#e07b39", linewidth=2, label="Naiivi")
    ax_wc.axhline(50, color="black", linewidth=1, linestyle="--", alpha=0.5)
    ax_wc.axvline(n, color="gray", linewidth=1, linestyle=":", alpha=0.8, label=f"Nykyinen n={n}")
    ax_wc.set_xlabel("Tarjoajien määrä n")
    ax_wc.set_ylabel("P(utility < 0)  [%]")
    ax_wc.set_title("Winner's curse -todennäköisyys (naiivi)")
    ax_wc.set_ylim(0, 100)
    ax_wc.legend()

    fig3.tight_layout()
    fig3
    return fig3, axes, ax_eu, ax_wc, ns, eu_naive_n, eu_sealed_n, eu_english_n, wc_naive_n


@app.cell
def __():
    import marimo as mo
    import numpy as np
    import matplotlib.pyplot as plt
    return mo, np, plt
