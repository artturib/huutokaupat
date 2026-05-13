import marimo

__generated_with = "0.23.1"
app = marimo.App(width="medium")


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Common Value Auction — Simulaatio

    ## Johdanto

    Huutokaupassa myydään kohde, jonka todellinen arvo $V$ on **sama kaikille** mutta
    **tuntematon** (common value). Tyypillisiä esimerkkejä ovat öljykenttä, yrityskauppa
    tai taidehuutokauppa. Kukin ostajaehdokas saa yksityisen, kohinaisen signaalin $V$:stä.

    **Mitä tässä tehdään.** Johdetaan analyyttiset tasapainostrategiat kolmelle
    huutokauppamuodolle ja vahvistetaan tulokset Monte Carlo -simulaatiolla.

    **Kolme protokollaa:** suljettu second-price (Vickrey), suljettu first-price,
    englantilainen (nouseva hinta).

    Alla esitetään tulokset näiden protokollien välillä, kun tarjoajat käyttävät tarjoajien hyödyn maksimoivaa strategiaa tarjoamiseen ja vertailun vuoksi strategiaa, missä tarjoavat oman signaalinsa verran.

    **Keskeiset tulokset:**

    | | Ostajan E[utility] | Myyjän E[tulo] |
    |---|---|---|
    | Tarjous = oma sigaali | $e\,\frac{3-n}{n+1}$ | $V + e\,\frac{n-3}{n+1}$ |
    | Suljetun huutokaupan optimistrategia (1st = 2nd) | $\dfrac{2e}{n+1}$ | $V - \dfrac{2e}{n+1}$ |
    | Avoimen huutokaupan (englantilainen) optimistrategia | $\dfrac{e}{n+1}$ | $V - \dfrac{e}{n+1}$ |

    **Johtopäätökset:**

    1. **Winner's curse:** naiivi ostaja maksaa odotetusti liikaa aina kun $n > 3$.
       Optimistrategioissa tarjoukset ovat matalampia kuin signaali.

    2. **Revenue equivalence:** suljettu first-price ja second-price tuottavat myyjälle
       täsmälleen saman odotetun tulon, vaikka voittajan maksu määräytyy eri tavalla.

    3. **Linkage Principle:** englantilainen huutokauppa tuottaa myyjälle enemmän kuin
       suljettu kaikilla $n$. Tippumishinnat paljastavat informaatiota, joka nostaa hintaa.

    ---

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

    ## 4. Benchmark strategia 2nd price huutokaupassa: jokainen ostaja tarjoaa oman signaalinsa verran

    Tarjoaja tarjoaa suoraan signaalinsa: $b_i = s_i$.

    **Myyjän odotettu tulo.** Voittaja on korkein signaali $s_{(n:n)}$, hinta on toiseksi
    korkein signaali $s_{(n-1:n)} = V + \varepsilon_{(n-1:n)}$:

    $$\mathbb{E}[P_\text{naiivi}] = \mathbb{E}[s_{(n-1:n)}] = V + e\cdot\frac{2(n-1)-n-1}{n+1} = V + e\cdot\frac{n-3}{n+1}$$

    Huomaa: kun $n > 3$, myyjä saa *enemmän* kuin $V$ — winner's curse siirtää rahaa ostajalta myyjälle.

    **Ostajan odotettu utility.** Koska $\mathbb{E}[U] = V - \mathbb{E}[P]$:

    $$\mathbb{E}[U_\text{naiivi}] = V - \mathbb{E}[P_\text{naiivi}] = -e\cdot\frac{n-3}{n+1} = e\cdot\frac{3-n}{n+1}$$

    Tämä on **negatiivinen kun $n > 3$** — winner's curse iskee.

    ---

    ## 5. Optimistrategia suljetussa 2nd price huutokaupassa

    $$b^*(s) = s - e\cdot\frac{n-1}{n+1}$$

    **Myyjän odotettu tulo.** Hinta = toiseksi korkein tarjous $= b^*(s_{(n-1:n)}) = s_{(n-1:n)} - e\cdot\frac{n-1}{n+1}$:

    $$\mathbb{E}[P_\text{2nd}] = \mathbb{E}[s_{(n-1:n)}] - e\cdot\frac{n-1}{n+1}
    = V + e\cdot\frac{n-3}{n+1} - e\cdot\frac{n-1}{n+1} = V - \frac{2e}{n+1}$$

    **Ostajan odotettu utility.** Koska $\mathbb{E}[U] = V - \mathbb{E}[P]$:

    $$\mathbb{E}[U] = V - \left(V - \frac{2e}{n+1}\right) = \frac{2e}{n+1} \qquad \checkmark$$

    **Johtaminen.** Tasapainoehto: tarjoajan tulee tarjota odotettu $V$:n
    arvo ehdollisena sille, että hän on korkein tarjoaja:

    $$b^*(s) = \mathbb{E}[V \mid s_i = s,\; s_i > \text{kaikki muut}]$$

    Johdetaan posteriori Bayesin kaavalla. Tasaisella priorilla $p(V) \propto 1$:

    $$f(V \mid \text{voitto},\, s_i=s) \;\propto\; \underbrace{p(V)}_{\propto\,1}
    \cdot \underbrace{f(s_i = s \mid V)}_{\frac{1}{2e},\; V\in(s-e,s+e)}
    \cdot \underbrace{P(\text{kaikki muut} < s \mid V)}_{\left(\frac{s-V+e}{2e}\right)^{n-1}}$$

    Oma signaali $s_i = s$ rajaa $V \in (s-e, s+e)$ (muuten $s_i = s$ on mahdoton).
    Kullekin muulle tarjoajalle $s_j = V + \varepsilon_j < s$ tapahtuu todennäköisyydellä
    $P(\varepsilon_j < s - V) = \frac{s - V + e}{2e}$, koska $\varepsilon_j \sim U(-e,e)$.
    Vakiotekijät absorboituvat normalisointivakioon:

    $$f(V \mid \text{voitto},\, s_i=s) \;\propto\; \left(\frac{s-V+e}{2e}\right)^{n-1}, \quad V \in (s-e,\,s+e)$$

    Sijoituksella $t = s+e-V \in (0,2e)$, tiheys $\propto t^{n-1}$:

    $$\mathbb{E}[t] = \frac{\int_0^{2e} t^n\,dt}{\int_0^{2e} t^{n-1}\,dt} = \frac{(2e)^{n+1}/(n+1)}{(2e)^n/n} = \frac{2en}{n+1}$$

    $$b^*(s) = \mathbb{E}[V] = (s+e) - \frac{2en}{n+1} = s - e\cdot\frac{n-1}{n+1} \qquad \checkmark$$

    ---

    ## 6. Optimistrategia suljetussa 1st price huutokaupassa

    $$\boxed{b^*(s_i) = s_i - e}$$

    **Myyjän odotettu tulo.** Voittaja on korkein signaali $s_{(n:n)}$ ja maksaa oman
    tarjouksensa $b^*(s_{(n:n)}) = s_{(n:n)} - e$:

    $$\mathbb{E}[P_\text{1st}] = \mathbb{E}[b^*(s_{(n:n)})] = \mathbb{E}[s_{(n:n)}] - e
    = V + e\cdot\frac{n-1}{n+1} - e = V - \frac{2e}{n+1}$$

    **Ostajan odotettu utility.** Koska $\mathbb{E}[U] = V - \mathbb{E}[P]$:

    $$\mathbb{E}[U_\text{1st}] = V - \left(V - \frac{2e}{n+1}\right) = \frac{2e}{n+1} \qquad \checkmark$$

    **Revenue equivalence:** first-price ja second-price tuottavat **saman odotetun tulon
    myyjälle** ($V - 2e/(n+1)$). Tämä pätee vaikka kyseessä on common value -huutokauppa,
    koska signaalit ovat ehdollisesti riippumattomia $V$:n suhteen.

    **Johtaminen: ODE.**

    Symmetrisessä BNE:ssä tarjoaja $i$ valitsee $b(s_i)$. Ensimmäisen asteen ehto johtaa ODE:hen:

    $$2e \cdot b'(s) + n \cdot b(s) = ns - e(n-2)$$

    *Askel 1: optimointiongelman asetus.*
    Etsitään symmetristä BNE:tä: kaikki tarjoajat käyttävät samaa kasvavaa tarjousfunktiota
    $b(\cdot)$, ja me haluamme löytää sen funktion. Koska $b$ on kasvava, tarjoaja $i$ voittaa
    täsmälleen silloin kun hänen signaalinsa on korkein: $s_i > s_j$ kaikille $j \neq i$.

    Tarjoaja $i$:n signaali on $s$. Hän harkitsee tarjousta $b(t)$, missä $t$ on
    **kuvitteellinen signaali** — ikään kuin hän esittäisi olevansa tyyppiä $t$.
    - Jos $t = s$: hän tarjoaa tasapainon mukaisen tarjouksen
    - Jos $t \neq s$: hän poikkeaa tasapainosta

    $\pi(t \mid s)$ on tarjoajan $i$ **odotettu hyöty** (sama asia kuin $U$, käytetään $\pi$-merkintää
    korostamaan, että optimoidaan $t$:n suhteen) kun hän tarjoaa $b(t)$ mutta tietää signaalinsa
    olevan $s$.

    *Askel 2: odotetun hyödyn kaava.*
    Tarjoaja voittaa jos $b(t) > b(s_j)$ kaikille $j$, eli $t > s_j$ kaikille $j$ (koska $b$ on
    kasvava). Voittaessaan hän maksaa $b(t)$ ja saa kohteen arvoltaan $V$. Koska $V$ on tuntematon,
    integroidaan posteriorin $f(V \mid s_i = s) = \frac{1}{2e}$ yli:

    $$\pi(t \mid s) = \frac{1}{2e}\int \underbrace{P(\text{kaikki } s_j < t \mid V)}_{\text{voittotodennäköisyys}} \cdot \underbrace{(V - b(t))}_{\text{hyöty voittaessa}}\,dV$$

    Voittotodennäköisyys: kukin $s_j = V + \varepsilon_j < t$ tapahtuu kun $\varepsilon_j < t - V$,
    todennäköisyydellä $\frac{t-V+e}{2e}$ kun $V \in (t-e, t+e)$, ja nolla kun $V > t+e$.
    Integrointialue: $V \in (s-e, s+e)$ (oma signaali) leikataan $V \leq t+e$ (muuten P=0).
    Koska tarkastellaan $t \leq s$, ylärajaksi tulee $t+e$:

    $$\pi(t \mid s) = \frac{1}{2e}\int_{s-e}^{t+e} \underbrace{\left(\frac{t-V+e}{2e}\right)^{n-1}}_{P(\text{kaikki muut} < t \mid V)}\underbrace{(V - b(t))}_{\text{hyöty}}\,dV$$

    *Askel 3: tasapainoehto ja derivointi.*
    Tasapainossa $t = s$ on optimaalinen, joten $\frac{\partial \pi}{\partial t}\big|_{t=s} = 0$.
    Leibnizin sääntö: $\frac{d}{dt}\int_{a}^{g(t)} f(t,V)\,dV = f(t,g(t))\cdot g'(t) + \int_a^{g(t)}\frac{\partial f}{\partial t}\,dV$.

    **Ylärajatermi** ($V = t+e$, $g'(t) = 1$):

    $$\left(\frac{t-(t+e)+e}{2e}\right)^{n-1}\cdot((t+e)-b(t)) = 0^{n-1}\cdot(\ldots) = 0 \quad (n > 1)$$

    Ylärajatermi häviää, koska voittotodennäköisyys on nolla kun $V = t+e$.

    **Integrandin osittaisderivaatat** $t$:n suhteen — integrandi on tulo kahdesta $t$:stä
    riippuvasta tekijästä, joten käytetään tulon derivoimissääntöä:

    $$\frac{\partial}{\partial t}\left[\left(\frac{t-V+e}{2e}\right)^{n-1}(V-b(t))\right]
    = \underbrace{(n-1)\left(\frac{t-V+e}{2e}\right)^{n-2}\frac{1}{2e}(V-b(t))}_{\text{1. tekijä derivoituu, 2. pysyy}}
    \;-\; \underbrace{\left(\frac{t-V+e}{2e}\right)^{n-1}b'(t)}_{\text{1. pysyy, 2. derivoituu}}$$

    *Askel 4: evaluoidaan $t = s$, sijoitetaan $u = (s-V+e)/(2e)$.*
    Kun $u = (s-V+e)/(2e)$: $V = s+e-2eu$, $dV = -2e\,du$, rajat $u: 1 \to 0$:

    $$\frac{\partial\pi}{\partial t}\bigg|_{t=s}
    = \frac{1}{2e}\int_0^1\left[\frac{n-1}{2e}\cdot u^{n-2}(s+e-b(s)-2eu) - u^{n-1}b'(s)\right]2e\,du = 0$$

    *Askel 5: lasketaan integraalit ja järjestetään.*

    $$\frac{n-1}{2e}\int_0^1 u^{n-2}(s+e-b(s)-2eu)\,du
    = \frac{n-1}{2e}\left[\frac{s+e-b(s)}{n-1} - \frac{2e}{n}\right]
    = \frac{s+e-b(s)}{2e} - \frac{n-1}{n}$$

    $$\int_0^1 u^{n-1}b'(s)\,du = \frac{b'(s)}{n}$$

    Yhdistämällä ja kertomalla $2en$:

    $$n(s+e-b(s)) - 2e(n-1) - 2e\,b'(s) = 0$$

    $$\boxed{2e\,b'(s) + n\,b(s) = ns - e(n-2)}$$

    **Ratkaisu.** Partikulaariratkaisu $b_p = s-e$ (tarkistus: $2e\cdot1 + n(s-e) = ns-e(n-2)$ ✓).
    Yleinen ratkaisu: $b(s) = Ce^{-ns/(2e)} + s - e$. Eksponenttiterm divergoi $s\to-\infty$
    ellei $C=0$, joten $b^*(s) = s - e$. $\checkmark$

    Sheidaus on $e$ — koko kohinan laajuus, enemmän kuin second-pricessa ($e\cdot\frac{n-1}{n+1} < e$).
    Intuitio: tarjoaja sheidaa signaalinsa **alimpaan mahdolliseen** $V$:n arvioon,
    sillä $V \geq s_i - e$ aina.

    **Miksi bid on deterministinen?** Koska signaali $s_i$ on jo satunnaisesti vedetty,
    $b^*(s_i) = s_i - e$ on deterministinen funktio tyypistä. Satunnaisuus syntyy signaalien
    vaihtelusta, ei ylimääräisestä sekoittamisesta (Harsanyin purifiointiperiaate).

    ---

    ## 7. Englantilainen rationaalinen strategia

    $$\boxed{p_k = \frac{s_{(k)} + s_{(1)}}{2}}, \qquad k = 1,\ldots,n-1$$

    Voittaja maksaa $p_{n-1} = \frac{s_{(n-1)} + s_{(1)}}{2}$.

    **Myyjän odotettu tulo.** Voittaja maksaa $p_{n-1} = (s_{(n-1)} + s_{(1)})/2$:

    $$\mathbb{E}[P_\text{eng}] = \frac{\mathbb{E}[s_{(n-1:n)}] + \mathbb{E}[s_{(1:n)}]}{2}
    = V + \frac{e\cdot\frac{n-3}{n+1} + e\cdot\frac{1-n}{n+1}}{2}
    = V + \frac{e\cdot\frac{-2}{n+1}}{2} = V - \frac{e}{n+1}$$

    **Ostajan odotettu utility.** Koska $\mathbb{E}[U] = V - \mathbb{E}[P]$:

    $$\mathbb{E}[U_\text{eng}] = V - \left(V - \frac{e}{n+1}\right) = \frac{e}{n+1} \qquad \checkmark$$

    **Tuottoranking myyjälle:**

    $$\mathbb{E}[\text{hinta}]:\quad \text{naiivi} \;\geq\; \text{eng. rat.} \;\geq\; \text{suljettu 2nd rat.} = \text{suljettu 1st rat.}$$

    Linkage Principle: $\mathbb{E}[P_\text{eng}] = V - \frac{e}{n+1} > V - \frac{2e}{n+1} = \mathbb{E}[P_\text{suljettu}]$
    kaikilla $n$. ✓

    **Johtaminen: tippumishinta tasajakaumalla.**

    Tarjoaja $k$ (signaali $s_k$) tietää oman signaalinsa ja on havainnut ensimmäisen
    tippumisen hinnasta $p_1 = s_{(1)}$ (pienin signaali). Posteriorista $V \sim U(s_k - e,\; s_k + e)$
    päivittyy Bayesilaisesti:

    $$V \mid s_{(1)},\, s_k \;\sim\; U\!\bigl(s_k - e,\; s_{(1)} + e\bigr)$$

    Tämä **ei muutu** myöhempien tippumisten myötä. Syy: väliarvot $s_j \in (s_{(1)}, s_k)$
    lisäävät ehdon $V \in (s_j-e, s_j+e)$, mutta
    $\max(s_k-e,\, s_j-e) = s_k - e$ ja $\min(s_{(1)}+e,\, s_j+e) = s_{(1)}+e$,
    joten tukijoukko ei kavennu.

    Tasapainoehto: tipu, kun hinta saavuttaa posteriorin odotusarvon:

    $$p_k = \mathbb{E}[V \mid s_{(1)},\, s_k] = \frac{(s_k - e) + (s_{(1)} + e)}{2} = \frac{s_k + s_{(1)}}{2}$$
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


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
