import marimo

__generated_with = "0.23.1"
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

    ### 2.2 Suljettu first-price auction

    Jokainen tarjoaja jättää salaisen tarjouksen. Korkein tarjoaja voittaa ja **maksaa oman
    tarjouksensa**.

    ### 2.3 Englantilainen huutokauppa

    Hinta nousee jatkuvasti. Kukin tarjoaja pysyy mukana kunnes hinta ylittää oman strategiansa
    mukaisen kynnyksen. Viimeisenä jäljelle jäävä voittaa ja maksaa hinnan, jolla toiseksi
    viimeinen tippui pois.

    ---

    ## 3. Järjestysstatistiikat

    Merkitään $\varepsilon_{(k:n)}$ signaalivirheiden $k$:nneksi pienimmäksi arvoksi
    (kasvavassa järjestyksessä). Koska $\varepsilon_i \sim \text{Uniform}(-e, e)$,
    $k$:nnen järjestysstatistiikan odotusarvo on

    $$\mathbb{E}[\varepsilon_{(k:n)}] = e \cdot \frac{2k - n - 1}{n+1}$$

    **Johtaminen.** Normalisoidaan $U_i = \frac{\varepsilon_i + e}{2e} \sim \text{Uniform}(0,1)$.
    $k$:nnen järjestysstatistiikan tiheysfunktio on

    $$f_{(k:n)}(u) = \frac{n!}{(k-1)!\,(n-k)!}\,u^{k-1}(1-u)^{n-k} \qquad u \in [0,1]$$

    (tämä on Beta$(k,\,n-k+1)$-jakauma). Odotusarvo:

    $$\mathbb{E}[U_{(k:n)}] = \frac{n!}{(k-1)!\,(n-k)!} \int_0^1 u^k(1-u)^{n-k}\,du
    = \frac{n!}{(k-1)!\,(n-k)!} \cdot \frac{k!\,(n-k)!}{(n+1)!} = \frac{k}{n+1}$$

    Skaalauksella $\varepsilon_i = -e + 2e\,U_i$:

    $$\mathbb{E}[\varepsilon_{(k:n)}] = -e + 2e \cdot \frac{k}{n+1} = e\cdot\frac{2k-n-1}{n+1} \qquad \checkmark$$

    ---

    ## 4. Benchmark strategia: jokainen ostaja tarjoaa oman signaalinsa verran

    Tarjoaja tarjoaa suoraan signaalinsa: $b_i = s_i$.

    $$\mathbb{E}[U_{\text{naiivi}}] = e \cdot \frac{3-n}{n+1}$$

    Tämä on **negatiivinen kun $n > 3$** — winner's curse iskee.

    ---

    ## 5. Suljettu second-price rationaalinen

    $$b_i^* = s_i - \delta, \qquad \delta = e\cdot\frac{n-1}{n+1}$$

    $$\mathbb{E}[U_{\text{2nd, rat}}] = \frac{2e}{n+1} > 0 \quad \text{aina}$$

    ---

    ## 6. Suljettu first-price rationaalinen

    Symmetrisessä BNE:ssä tarjoaja $i$ valitsee $b(s_i)$. Ensimmäisen asteen ehto johtaa ODE:hen:

    $$2e \cdot b'(s) + n \cdot b(s) = ns - e(n-2)$$

    Ratkaisu vakiovakiolla $C = 0$:

    $$\boxed{b^*(s_i) = s_i - e}$$

    Tarkistus: $2e \cdot 1 + n(s-e) = ns - e(n-2) \implies 2e - ne = -e(n-2)\ \checkmark$

    Sheidaus on $e$ — koko kohinan laajuus, enemmän kuin second-pricessa ($\delta < e$).
    Intuitio: tarjoaja sheidaa signaalinsa **alimpaan mahdolliseen** $V$:n arvioon,
    sillä $V \geq s_i - e$ aina.

    **Odotettu utility:**

    $$U_{\text{1st}} = V - b^*(s_{(n:n)}) = V - s_{(n:n)} + e = e - \varepsilon_{(n:n)}$$

    $$\mathbb{E}[U_{\text{1st, rat}}] = e - e\cdot\frac{n-1}{n+1} = \frac{2e}{n+1}$$

    **Revenue equivalence:** first-price ja second-price tuottavat **saman odotetun tulon
    myyjälle** ($V - 2e/(n+1)$). Tämä pätee vaikka kyseessä on common value -huutokauppa,
    koska signaalit ovat ehdollisesti riippumattomia $V$:n suhteen.

    **Miksi bid on deterministinen?** Koska signaali $s_i$ on jo satunnaisesti vedetty,
    $b^*(s_i) = s_i - e$ on deterministinen funktio tyypistä. Satunnaisuus syntyy signaalien
    vaihtelusta, ei ylimääräisestä sekoittamisesta (Harsanyin purifiointiperiaate).

    ---

    ## 7. Englantilainen rationaalinen strategia

    **Milgrom–Weber (1982) tasapainoehto** ("almost tied"):

    $$b^*_j = \frac{2s_j + \sum_{i=1}^k p_i}{k+2}$$

    Rekursiivinen tippumissekvenssi:

    $$\boxed{p_k = \frac{2\,s_{(k:n)} + \sum_{j=1}^{k-1} p_j}{k+1}}, \qquad k = 1, \ldots, n-1$$

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

    **Linkage Principle** (Milgrom–Weber 1982): informaatiopaljastus hyödyttää myyjää —
    englantilainen rationaalinen tuottaa aina pienemmän utiliteetin voittajalle kuin suljettu rationaalinen.

    **Miksi paljastuva informaatio nostaa hintaa eikä laske sitä?**

    Oikea vertailu on suljettuun *rationaaliseen* strategiaan, jossa sheidaus $\delta$ on vakio
    ja riippumaton $V$:stä. Englantilaisessa toiseksi korkein tarjoaja päivittää kynnystään
    havaittujen dropoutien perusteella — korkeat dropoutit (merkki korkeasta $V$:stä) nostavat
    kynnystä. **Hinta on positiivisesti korreloitunut $V$:n kanssa**: myyjä saa enemmän juuri
    silloin kun voittaminen on arvokkainta.

    **Tuottoranking myyjälle:**

    $$\mathbb{E}[\text{hinta}]:\quad \text{naiivi} \geq \text{eng. rat.} \geq \text{suljettu 2nd rat.} = \text{suljettu 1st rat.}$$

    ---

    ## 8. Englantilaisen huutokaupan oikea BNE tasajakaumalle

    Alkuperäinen koodi käytti Milgrom–Weber-kaavaa $p_k = \frac{2s_{(k)} + \sum_{j<k} p_j}{k+1}$,
    joka perustuu **aritmeettiseen keskiarvoon** estimaattina $V$:stä. Tämä on oikein
    normaalijakautuneille signaaleille, mutta **väärin tasajakautuneille**.

    **Oikea Bayesilainen päättely tasajakaumalla** ($s_i = V + \varepsilon_i$,
    $\varepsilon_i \sim U(-e,e)$, tasainen priori $V$:lle):

    Tarjoajan $k$ posteriori oman signaalin $s_k$ jälkeen: $V \sim U(s_k - e,\; s_k + e)$.

    Kun ekan tippumisen hinnasta inferoidaan $s_{(1)}$ (pienin signaali), posteriori päivittyy:

    $$V \sim U(s_k - e,\; s_{(1)} + e)$$

    Tämä **ei muutu** myöhempien tippumisten myötä — vain minimi $s_{(1)}$ ja oma signaali
    $s_k$ ratkaisevat (väliarvot $s_j \in (s_{(1)}, s_k)$ eivät kavenna tukijoukkoa).

    Posteriorin odotusarvo (= oikea tippumishinta): $\frac{s_k + s_{(1)}}{2}$

    **Oikea tippumisstrategia tasajakaumalle:**

    $$\boxed{p_k = \frac{s_{(k)} + s_{(1)}}{2}}$$

    Voittaja maksaa $p_{n-1} = \frac{s_{(n-1)} + s_{(1)}}{2}$, josta:

    $$\mathbb{E}[\text{myyjän tulo}] = V - \frac{e}{n+1}$$

    Vertailu suljettuun rationaaliseen ($V - \frac{2e}{n+1}$): englantilainen tuottaa enemmän
    kaikilla $n$. Linkage Principle pätee. ✓
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ---
    ## 8. Simulaatio
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

    eps = rng.uniform(-e, e, size=(N_sim, n))
    signals = V + eps
    sorted_s = np.sort(signals, axis=1)

    # --- Naiivi (suljettu 2nd = englantilainen) ---
    price_naive   = sorted_s[:, -2]
    utility_naive = V - price_naive

    # --- Suljettu second-price rationaalinen ---
    delta          = e * (n - 1) / (n + 1)
    bids_2nd       = signals - delta
    price_2nd_rat  = np.sort(bids_2nd, axis=1)[:, -2]
    utility_2nd_rat = V - price_2nd_rat

    # --- Suljettu first-price rationaalinen: b*(s) = s - e ---
    bids_1st       = signals - e
    price_1st_rat  = np.max(bids_1st, axis=1)   # voittaja maksaa oman tarjouksensa
    utility_1st_rat = V - price_1st_rat

    # --- Englantilainen rationaalinen (oikea BNE tasajakaumalle) ---
    # Posteriori V ~ U(s_k - e, s_(1) + e) → E[V] = (s_k + s_(1)) / 2
    # Voittaja maksaa: (s_(n-1) + s_(1)) / 2
    price_eng_rat   = (sorted_s[:, -2] + sorted_s[:, 0]) / 2
    utility_eng_rat = V - price_eng_rat

    # --- Analyyttiset odotusarvot ---
    eu_naive_formula = e * (3 - n) / (n + 1)
    eu_sealed_formula = 2 * e / (n + 1)   # sama first- ja second-pricelle
    eu_eng_formula    = e / (n + 1)        # = e/(n+1), aina > 0 ja < eu_sealed
    return (
        V,
        bids_1st,
        bids_2nd,
        delta,
        e,
        eu_eng_formula,
        eu_naive_formula,
        eu_sealed_formula,
        n,
        price_1st_rat,
        price_2nd_rat,
        price_eng_rat,
        price_naive,
        signals,
        utility_1st_rat,
        utility_2nd_rat,
        utility_eng_rat,
        utility_naive,
    )


@app.cell(hide_code=True)
def _(
    V,
    delta,
    e,
    eu_eng_formula,
    eu_naive_formula,
    eu_sealed_formula,
    mo,
    n,
    np,
    price_1st_rat,
    price_2nd_rat,
    price_eng_rat,
    price_naive,
    utility_1st_rat,
    utility_2nd_rat,
    utility_eng_rat,
    utility_naive,
):
    wc_naive  = np.mean(utility_naive < 0) * 100
    wc_2nd    = np.mean(utility_2nd_rat < 0) * 100
    wc_1st    = np.mean(utility_1st_rat < 0) * 100
    wc_eng    = np.mean(utility_eng_rat < 0) * 100
    mo.md(f"""
    ### Tulokset: n={n}, e={e}, V={V}, δ={delta:.2f}

    | | Naiivi | 2nd rat. | 1st rat. | Eng. rat. |
    |---|---|---|---|---|
    | **E[utility] — kaava** | {eu_naive_formula:.3f} | {eu_sealed_formula:.3f} | {eu_sealed_formula:.3f} | {eu_eng_formula:.3f} |
    | **E[utility] — simulaatio** | {np.mean(utility_naive):.3f} | {np.mean(utility_2nd_rat):.3f} | {np.mean(utility_1st_rat):.3f} | {np.mean(utility_eng_rat):.3f} |
    | **P(utility < 0)** | {wc_naive:.1f}% | {wc_2nd:.1f}% | {wc_1st:.1f}% | {wc_eng:.1f}% |
    | **E[hinta myyjälle]** | {np.mean(price_naive):.2f} | {np.mean(price_2nd_rat):.2f} | {np.mean(price_1st_rat):.2f} | {np.mean(price_eng_rat):.2f} |

    Revenue equivalence: 2nd rat. ({np.mean(price_2nd_rat):.2f}) vs 1st rat. ({np.mean(price_1st_rat):.2f})
    """)
    return


@app.cell
def _(
    V,
    e,
    n,
    np,
    plt,
    utility_1st_rat,
    utility_2nd_rat,
    utility_eng_rat,
    utility_naive,
):
    fig1, ax1 = plt.subplots(figsize=(10, 4))
    all_u = np.concatenate([utility_naive, utility_2nd_rat, utility_1st_rat, utility_eng_rat])
    bins = np.linspace(all_u.min() - 2, all_u.max() + 2, 60)
    ax1.hist(utility_naive,    bins=bins, alpha=0.40, color="#e07b39", label="Naiivi")
    ax1.hist(utility_2nd_rat,  bins=bins, alpha=0.40, color="#4c8fd6", label="Suljettu 2nd rat.")
    ax1.hist(utility_1st_rat,  bins=bins, alpha=0.40, color="#9b59b6", label="Suljettu 1st rat.")
    ax1.hist(utility_eng_rat,  bins=bins, alpha=0.40, color="#3daa6a", label="Eng. rat.")
    ax1.axvline(0, color="black", linewidth=1.2, linestyle="--", label="Utility = 0")
    for u_arr, col in [
        (utility_naive, "#e07b39"),
        (utility_2nd_rat, "#4c8fd6"),
        (utility_1st_rat, "#9b59b6"),
        (utility_eng_rat, "#3daa6a"),
    ]:
        ax1.axvline(np.mean(u_arr), color=col, linewidth=2)
    ax1.set_xlabel("Voittajan utility  (V − maksettu hinta)")
    ax1.set_ylabel("Frekvenssi")
    ax1.set_title(f"Voittajan utiliteetin jakauma  (n={n}, e={e}, V={V})")
    ax1.legend(fontsize=8)
    fig1.tight_layout()
    fig1
    return


@app.cell
def _(V, bids_1st, bids_2nd, delta, e, n, np, plt, signals):
    idx = np.random.default_rng(0).integers(0, signals.shape[0], 300)
    s_sample  = signals[idx].ravel()
    b2_sample = bids_2nd[idx].ravel()
    b1_sample = bids_1st[idx].ravel()

    fig2, ax2 = plt.subplots(figsize=(6, 5))
    s_line = np.linspace(s_sample.min(), s_sample.max(), 100)
    ax2.plot(s_line, s_line,         "k--",  linewidth=1,  label="b = s  (naiivi)")
    ax2.plot(s_line, s_line - delta, color="#4c8fd6", linewidth=2, label=f"2nd rat.: b = s − δ  (δ={delta:.2f})")
    ax2.plot(s_line, s_line - e,     color="#9b59b6", linewidth=2, label=f"1st rat.: b = s − e  (e={e})")
    ax2.axvline(V, color="gray", linewidth=1, linestyle=":", label=f"V={V}")
    ax2.set_xlabel("Signaali $s_i$")
    ax2.set_ylabel("Tarjous $b_i$")
    ax2.set_title(f"Bid sheidaus vertailu  (n={n}, e={e})")
    ax2.legend(fontsize=8)
    fig2.tight_layout()
    fig2
    return


@app.cell
def _(e, n, np, plt):
    ns = np.arange(2, 31)
    eu_naive_n  = e * (3 - ns) / (ns + 1)
    eu_sealed_n = 2 * e / (ns + 1)   # sama 1st ja 2nd
    eu_english_n = e / (ns + 1)       # oikea BNE tasajakaumalle

    wc_naive_n = np.array([
        np.mean(
            -np.sort(np.random.default_rng(seed=k).uniform(-e, e, size=(5000, ni)), axis=1)[:, -2] < 0
        )
        for k, ni in enumerate(ns)
    ])

    fig3, axes = plt.subplots(1, 2, figsize=(12, 4))

    ax_eu = axes[0]
    ax_eu.plot(ns, eu_naive_n,   color="#e07b39", linewidth=2, label="Naiivi")
    ax_eu.plot(ns, eu_sealed_n,  color="#4c8fd6", linewidth=2, label="Suljettu 2nd rat. = 1st rat.")
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
    return


@app.cell
def _():
    import marimo as mo
    import numpy as np
    import matplotlib.pyplot as plt

    return mo, np, plt


if __name__ == "__main__":
    app.run()
