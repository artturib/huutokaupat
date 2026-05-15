import marimo

__generated_with = "0.23.1"
app = marimo.App(width="medium")


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Yhteisvara-huutokauppa: normaalijakautuneet signaalit

    ## Johdanto

    Sama perusrakenne kuin tasajakautuneiden signaalien mallissa: huutokaupassa myydään kohde,
    jonka todellinen arvo $V$ on **sama kaikille** mutta **tuntematon** (common value).
    Kukin ostajaehdokas saa yksityisen, kohinaisen signaalin $V$:stä.

    **Ero tasajakaumaan:** Normaalijakaumassa signaalivirheellä ei ole rajattua tukijoukkoa,
    ja posteriori $V$:lle päivittyy konjugaattiominaisuuden nojalla *jokaisesta* paljastuneesta
    signaalista — ei vain ääripäistä. Tästä syystä englantilaisen huutokaupan strategia
    poikkeaa tasajakaumasta: kaikki aiemmin tippuneiden signaalit vaikuttavat tippumishintaan.

    Koska siistejä suljettuja kaavoja ei ole yleiselle $n$:lle, tulokset ilmaistaan numeerisesti
    laskettavien korjaustermien $c(n)$ ja $d(n)$ sekä järjestysstatistiikkojen odotusarvojen
    $\mathbb{E}[Z_{(k:n)}]$ avulla.

    **Merkinnät:** $Z_{(k:n)}$ on standardinormaalijakauman $k$:s järjestysstatistiikka
    ($n$ i.i.d. $N(0,1)$-muuttujaa kasvavassa järjestyksessä). Symmetriasta:
    $\mathbb{E}[Z_{(k:n)}] = -\mathbb{E}[Z_{(n-k+1:n)}]$ ja $\sum_{k=1}^n \mathbb{E}[Z_{(k:n)}] = 0$.

    **Keskeiset tulokset:**

    | | Ostajan E[utility] | Myyjän E[tulo] |
    |---|---|---|
    | Tarjous = oma signaali | $-\sigma\,\mathbb{E}[Z_{(n-1:n)}]$ | $V + \sigma\,\mathbb{E}[Z_{(n-1:n)}]$ |
    | Suljettu 2nd price | $\sigma\!\left(c(n) - \mathbb{E}[Z_{(n-1:n)}]\right)$ | $V - \sigma\!\left(c(n) - \mathbb{E}[Z_{(n-1:n)}]\right)$ |
    | Suljettu 1st price | $\sigma\!\left(d(n) - \mathbb{E}[Z_{(n:n)}]\right)$ | $V - \sigma\!\left(d(n) - \mathbb{E}[Z_{(n:n)}]\right)$ |
    | Avoin huutokauppa | $\dfrac{\sigma\!\left(\mathbb{E}[Z_{(n:n)}] - \mathbb{E}[Z_{(n-1:n)}]\right)}{n}$ | $V - \dfrac{\sigma\!\left(\mathbb{E}[Z_{(n:n)}] - \mathbb{E}[Z_{(n-1:n)}]\right)}{n}$ |

    missä $c(n)$ on 2nd price -tarjouskorjaus ja $d(n) = c(n) + 1/\mathbb{E}[Z_{(n:n)}]$
    on 1st price -tarjouskorjaus (molemmat lasketaan numeerisesti).

    **Johtopäätökset:**

    1. Naiivi strategia (tarjoa oma signaali) on voittajalle tappiollinen kun $n \geq 3$
       (jolloin $\mathbb{E}[Z_{(n-1:n)}] > 0$) — winner's curse.

    2. Suljettu 1st price -huutokauppa tuottaa myyjälle **vähemmän** kuin 2nd price.
       Revenue equivalence **ei päde** common value -huutokaupoissa — toisin kuin
       yksityisten arvojen huutokaupoissa.

    3. Avoin huutokauppa tuottaa myyjälle **eniten** (kytkentäperiaate, Milgrom–Weber 1982):
       muiden tippumishinnat paljastavat tietoa $V$:stä ja nostavat jäljelle jäävien arvioita.

    ---

    ## 1. Malli

    Kohteella on **yksi todellinen arvo** $V$, joka on sama kaikille tarjoajille mutta tuntematon.
    Kukin $n$ tarjoajista saa yksityisen **signaalin**

    $$s_i = V + \varepsilon_i, \qquad \varepsilon_i \overset{\text{iid}}{\sim} N(0,\sigma^2)$$

    **Posteriori tasaisella priorilla $p(V) \propto 1$:**

    $$V \mid s_i \;\sim\; N(s_i,\; \sigma^2)$$

    Kun tiedossa on $k$ signaalia $s_1, \ldots, s_k$:

    $$V \mid s_1, \ldots, s_k \;\sim\; N\!\left(\bar{s}_k,\; \frac{\sigma^2}{k}\right), \qquad \bar{s}_k = \frac{s_1 + \cdots + s_k}{k}$$

    Normaalijakauman konjugaattiominaisuus: jokainen lisähavainto siirtää posterioria
    kohti signaalien juoksevaa keskiarvoa ja kaventaa epävarmuutta.
    Tasajakaumassa sen sijaan vain ääriarvot (min ja max) rajaavat posterioria —
    väliarvot ovat redundantteja.

    ---

    ## 2. Protokollat

    ### 2.1 Suljettu second-price huutokauppa (Vickrey)

    Jokainen tarjoaja jättää salaisen tarjouksen. Korkein tarjoaja voittaa ja **maksaa toiseksi
    korkeimman tarjouksen**.

    ### 2.2 Suljettu first-price huutokauppa

    Jokainen tarjoaja jättää salaisen tarjouksen. Korkein tarjoaja voittaa ja **maksaa oman
    tarjouksensa**.

    ### 2.3 Avoin huutokauppa

    Hinta nousee jatkuvasti. Kukin tarjoaja pysyy mukana kunnes hinta ylittää oman
    tippumishintansa $p(s_i)$. Viimeisenä jäljelle jäävä voittaa ja maksaa hinnan,
    jolla toiseksi viimeinen tippui pois.

    ---

    ## 3. Benchmark: tarjoaja tarjoaa oman signaalinsa

    Tarjoaja tarjoaa suoraan signaalinsa: $b_i = s_i$.

    **Myyjän odotettu tulo.** Voittaja on korkein signaali $s_{(n:n)} = V + \sigma Z_{(n:n)}$,
    hinta on toiseksi korkein signaali $s_{(n-1:n)} = V + \sigma Z_{(n-1:n)}$:

    $$\mathbb{E}[P_\text{naiivi}] = V + \sigma\,\mathbb{E}[Z_{(n-1:n)}]$$

    **Ostajan odotettu utility:** $\mathbb{E}[U_\text{naiivi}] = -\sigma\,\mathbb{E}[Z_{(n-1:n)}]$

    Tämä on **negatiivinen kun $n \geq 3$** — winner's curse iskee.

    ---

    ## 4. Optimistrategia suljetussa 2nd price huutokaupassa

    $$\boxed{b^*(s_i) = s_i - \sigma\,c(n)}$$

    missä $c(n) \geq 0$ on numeerisesti laskettava winner's curse -korjaus.
    Suljettu muoto $n = 3$: $c(3) = 1/\!\sqrt{3\pi} \approx 0{,}326$.

    [→ Liite A: Optimistrategian johtaminen](#liite-a)

    **Myyjän odotettu tulo.** Hinta = toiseksi korkein tarjous $= b^*(s_{(n-1:n)})$:

    $$\mathbb{E}[P_\text{2nd}] = \mathbb{E}[s_{(n-1:n)}] - \sigma\,c(n)
    = V + \sigma\,\mathbb{E}[Z_{(n-1:n)}] - \sigma\,c(n)
    = V - \sigma\!\left(c(n) - \mathbb{E}[Z_{(n-1:n)}]\right)$$

    **Ostajan odotettu utility:**

    $$\mathbb{E}[U_\text{2nd}] = \sigma\!\left(c(n) - \mathbb{E}[Z_{(n-1:n)}]\right) > 0 \qquad \checkmark$$

    ---

    ## 5. Optimistrategia suljetussa 1st price huutokaupassa

    $$\boxed{b^*(s_i) = s_i - \sigma\,d(n)}, \qquad d(n) = c(n) + \frac{1}{\mathbb{E}[Z_{(n:n)}]}$$

    missä $c(n)$ on sama winner's curse -korjaus kuin 2nd pricessa, ja lisätermi
    $1/\mathbb{E}[Z_{(n:n)}]$ on strateginen alihinnoittelu — tarjoajan täytyy sheida enemmän,
    koska oma bid on myös maksettu hinta.

    [→ Liite B: Optimistrategian johtaminen](#liite-b)

    **Myyjän odotettu tulo.** Voittaja (korkein signaali) maksaa oman tarjouksensa:

    $$\mathbb{E}[P_\text{1st}] = \mathbb{E}[s_{(n:n)}] - \sigma\,d(n)
    = V + \sigma\,\mathbb{E}[Z_{(n:n)}] - \sigma\,d(n)
    = V - \sigma\!\left(d(n) - \mathbb{E}[Z_{(n:n)}]\right)$$

    **Ostajan odotettu utility:**

    $$\mathbb{E}[U_\text{1st}] = \sigma\!\left(d(n) - \mathbb{E}[Z_{(n:n)}]\right) > 0 \qquad \checkmark$$

    **Vertailu 2nd priceen:** $\mathbb{E}[P_\text{1st}] < \mathbb{E}[P_\text{2nd}]$ —
    1st price tuottaa myyjälle vähemmän. Revenue equivalence ei päde common value
    -huutokaupoissa (vrt. yksityisten arvojen huutokauppa, jossa $\mathbb{E}[P_\text{1st}] = \mathbb{E}[P_\text{2nd}]$).

    ---

    ## 6. Optimistrategia avoimessa huutokaupassa

    Avoimessa huutokaupassa tarjoajat eivät jätä suljettua tarjousta — he pysyvät mukana
    kunnes hinta ylittää oman tippumishintansa. Strategia on tippumishinta $p_k(s_k)$,
    joka riippuu omasta signaalista ja kaikista aiemmin paljastuneista signaaleista.

    $$\boxed{p_k = \frac{s_{(1)} + \cdots + s_{(k-1)} + 2\,s_{(k)}}{k+1}} \qquad k = 1,\ldots,n-1$$

    **Ero tasajakaumaan:** Tasajakaumassa $p_k = (s_{(1)} + s_{(k)})/2$ — vain alin signaali ja oma signaali.
    Normaalijakaumassa mukaan tulevat **kaikki** välisignaalit, koska normaaliposteriori on
    konjugaatti ja jokainen havainto siirtää posterioriodotusarvoa.

    [→ Liite C: Tippumishinnan johtaminen](#liite-c)

    Voittajan maksama hinta ($k = n-1$, kaikki $n-2$ matalampaa signaalia paljastuneita):

    $$P = p_{n-1} = \frac{s_{(1)} + \cdots + s_{(n-2)} + 2\,s_{(n-1)}}{n}$$

    **Myyjän odotettu tulo.** Käyttäen $\sum_{k=1}^n \mathbb{E}[Z_{(k:n)}] = 0$:

    $$\mathbb{E}[P_\text{eng}] = V - \frac{\sigma\!\left(\mathbb{E}[Z_{(n:n)}] - \mathbb{E}[Z_{(n-1:n)}]\right)}{n}$$

    **Ostajan odotettu utility:**

    $$\mathbb{E}[U_\text{eng}] = \frac{\sigma\!\left(\mathbb{E}[Z_{(n:n)}] - \mathbb{E}[Z_{(n-1:n)}]\right)}{n} > 0 \qquad \checkmark$$

    **Tuottoranking myyjälle:**

    $$\mathbb{E}[\text{hinta}]:\quad \text{naiivi} \;\geq\; \mathbb{E}[P_\text{eng}] \;>\; \mathbb{E}[P_\text{2nd}] \;>\; \mathbb{E}[P_\text{1st}]$$

    Kytkentäperiaate (Milgrom–Weber 1982): avoin huutokauppa paljastaa muiden signaaleja
    tippumishintojen kautta — tieto nostaa tarjoajien arvioita $V$:stä ja siten myyjän tuloa.

    ---

    <a id="liite-a"></a>
    ## Liite A: 2nd price optimistrategian johtaminen

    **Tasapainoehto.** Ratkaiseva tilanne on marginaalivoitto: tarjoaja on tasapisteessä
    toiseksi korkeimman kilpailijan kanssa ($Y_1 = s$, missä $Y_1 = \max_{j \neq i} s_j$).
    Optimaalinen tarjous on $V$:n posterioriodotusarvo tässä tilanteessa:

    $$b^*(s) = \mathbb{E}[V \mid s_i = s,\; Y_1 = s]$$

    **Likelihood $V$:n funktiona.** Tiheys $Y_1 = s$ ehdolla $V$ on järjestysstatistiikan tiheys
    (yksi kilpailija täsmälleen $s$:ssä, loput $n-2$ alle $s$, kerrottuna $(n-1)$ valintatavalla):

    $$f_{Y_1}(s \mid V) = (n-1)\cdot\frac{\varphi\!\left(\frac{s-V}{\sigma}\right)}{\sigma}\cdot
    \Phi\!\left(\frac{s-V}{\sigma}\right)^{n-2}$$

    Tasaisella priorilla $p(V) \propto 1$:

    $$f(V \mid s_i=s,\, Y_1=s) \;\propto\;
    \frac{\varphi\!\left(\frac{s-V}{\sigma}\right)}{\sigma}
    \cdot \frac{\varphi\!\left(\frac{s-V}{\sigma}\right)}{\sigma}
    \cdot \Phi\!\left(\frac{s-V}{\sigma}\right)^{n-2}
    \;\propto\; \varphi\!\left(\frac{s-V}{\sigma}\right)^{\!2} \cdot \Phi\!\left(\frac{s-V}{\sigma}\right)^{n-2}$$

    **Sijoitus $z = (s-V)/\sigma$.** Optimaalinen tarjous on posterioriodotusarvo $V = s - \sigma z$:

    $$b^*(s) = s - \sigma \cdot \underbrace{\frac{\displaystyle\int_{-\infty}^{\infty} z\;\varphi(z)^2\;\Phi(z)^{n-2}\,dz}
    {\displaystyle\int_{-\infty}^{\infty} \varphi(z)^2\;\Phi(z)^{n-2}\,dz}}_{=\;c(n)}
    \;=\; s - \sigma\,c(n)$$

    **Analyyttinen ratkaisu $n=3$:**

    *Nimittäjä:* symmetriaargumentilla (sijoitus $z \to -z$):
    $\int\varphi(z)^2\Phi(z)\,dz = \int\varphi(z)^2\Phi(-z)\,dz$,
    joten $2\int\varphi(z)^2\Phi(z)\,dz = \int\varphi(z)^2\,dz = \tfrac{1}{2\sqrt{\pi}}$,
    eli nimittäjä $= \tfrac{1}{4\sqrt{\pi}}$.

    *Osoittaja:* osin integroimalla $\int z\,\varphi(z)^2\,\Phi(z)\,dz = -\tfrac{1}{4\pi\sqrt{3}}$.

    $$c(3) = \frac{1/(4\pi\sqrt{3})}{1/(4\sqrt{\pi})} = \frac{\sqrt{\pi}}{\pi\sqrt{3}} = \frac{1}{\sqrt{3\pi}} \approx 0{,}326$$

    **Yleiselle $n$:lle** integroidaan numeerisesti (`scipy.integrate.quad`).

    ---

    <a id="liite-b"></a>
    ## Liite B: 1st price optimistrategian johtaminen

    **Siirtymäinvarianssi — lineaarinen tasapaino.** Koska signaalivirheet ovat normaalijakautuneita
    (tasajakauma on siirtymäinvariantti), symmetrinen BNE on lineaarinen:
    $b^*(s) = s - \sigma\,d(n)$ jollakin vakiolla $d(n)$, ja $(b^*)'(s) = 1$.

    **Ensimmäisen kertaluvun ehto (FOC).** Symmetrisessä tasapainossa $s_i$:n tulee olla optimaalinen.
    Marginaalivoittajatilanteessa $Y_1 = s_i = s$:

    $$\bigl(\underbrace{\mathbb{E}[V \mid s_i, Y_1 = s_i]}_{=\;s - \sigma c(n)}
    \;-\; b^*(s)\bigr)\cdot f_{Y_1|s}(s)
    \;=\; (b^*)'(s)\cdot P(Y_1 < s \mid s)$$

    **Kilpailijoiden signaalit ovat korreloituneita.** Vaikka kukin $s_j \mid s_i = s$ on
    marginaalisesti $N(s, 2\sigma^2)$, ne eivät ole riippumattomia — kaikkia yhdistää
    yhteinen tuntematon $V$. Oikea laskutapa käyttää odotusarvon lakia:

    $$P(Y_1 < s \mid s_i = s)
    = \mathbb{E}_{V \mid s}\!\left[\Phi\!\left(\tfrac{s-V}{\sigma}\right)^{n-1}\right]
    = \int_{-\infty}^{\infty} \Phi(z)^{n-1}\,\varphi(z)\,dz = \frac{1}{n}$$

    (sijoitus $u = \Phi(z)$: $\int_0^1 u^{n-1}\,du = 1/n$).

    **Tiheys pistessä $Y_1 = s$ ehdolla $s_i = s$:**

    $$f_{Y_1|s}(s) = \frac{n-1}{\sigma}\int_{-\infty}^{\infty}\Phi(z)^{n-2}\varphi(z)^2\,dz
    = \frac{\mathbb{E}[Z_{(n:n)}]}{n\sigma}$$

    Viimeisin yhtäsuuruus seuraa identiteetistä $\mathbb{E}[Z_{(n:n)}] = n(n-1)\int\Phi(z)^{n-2}\varphi(z)^2\,dz$,
    joka johdetaan osin integroimalla.

    **FOC:n ratkaisu.** Sijoitetaan $b^*(s) = s - \sigma d$, $(b^*)' = 1$:

    $$\sigma(d - c(n))\cdot\frac{\mathbb{E}[Z_{(n:n)}]}{n\sigma} = \frac{1}{n}$$

    $$\boxed{d(n) = c(n) + \frac{1}{\mathbb{E}[Z_{(n:n)}]}}$$

    Strateginen alihinnoittelu 1st vs 2nd price on $\sigma/\mathbb{E}[Z_{(n:n)}]$: suurempi kun
    kilpailijoita on vähän (voittaja tietää olevansa selvästi paremman signaalin haltija),
    pienempi kun kilpailijoita on paljon.

    ---

    <a id="liite-c"></a>
    ## Liite C: Englantilaisen tippumishinnan johtaminen

    **Ensimmäinen tippuja ($k=1$).** Tasapaino on $p_1 = s_{(1)}$.

    Osoitetaan, että $\beta(s) = s$ on Nashin tasapaino poikkeama-argumentilla.
    Jos kaikki pelaavat $\beta(s) = s - \varepsilon$ ($\varepsilon > 0$), pelaaja $i$ voi
    pelaata $\beta(s) = s - \gamma$ ($\gamma < \varepsilon$) ja tippua myöhemmin — kilpailijat
    tippuvat ensin, joten pelaaja $i$ voittaa halvemmalla. Kilpajuoksu ylöspäin ei pysähdy
    ennen $\beta(s) = s$.

    Kun kaikki pelaavat $\beta(s) = s$: pieni poikkeama ylöspäin ($+\delta$) tai alaspäin
    ($-\gamma$) tuottaa kumpikin $\Delta U < 0$ (lasketaan samoin kuin tasajakaumassa).
    Ensimmäinen tippumishinta paljastaa $s_{(1)}$.

    **Myöhemmät tippujat ($k \geq 2$).** Tarjoaja $k$ tietää oman signaalinsa $s_{(k)}$ ja on
    havainnut $k-1$ aiempaa tippumishintaa, jotka paljastavat $s_{(1)}, \ldots, s_{(k-1)}$.

    Normaalijakauman konjugaattiominaisuus: ehdollistaen kaikille $k-1$ paljastuneelle
    signaalille ja omalle signaalille:

    $$V \mid s_{(1)},\ldots,s_{(k-1)},\, s_{(k)} \;\sim\; N\!\left(\frac{s_{(1)}+\cdots+s_{(k-1)}+s_{(k)}}{k},\; \frac{\sigma^2}{k}\right)$$

    Tasapainoehto: tipu, kun hinta saavuttaa $V$:n posterioriodotusarvon
    **marginaalivoittotilanteessa** $s_{k+1} = s_{(k)}$ (olet tasapisteessä seuraavan tippujan kanssa):

    $$p_k = \mathbb{E}\!\left[V \;\middle|\; s_{(1)},\ldots,s_{(k-1)},\, s_{(k)},\, s_{k+1} = s_{(k)}\right]$$

    Ehdollistetaan siis $k+1$ signaalille, joista $k-1$ on välillä $(s_{(1)},\ldots,s_{(k-1)})$
    ja kaksi on arvoltaan $s_{(k)}$ (oma + marginaalinen kilpailija). Normaaliposteriorin odotusarvo:

    $$p_k = \frac{s_{(1)} + \cdots + s_{(k-1)} + 2\,s_{(k)}}{k+1}$$

    **Toiseksi viimeinen tippuja ($k = n-1$)** määrää hinnan.
    Kaikki $n-2$ matalampaa signaalia ovat jo paljastuneet:

    $$P = p_{n-1} = \frac{s_{(1)} + \cdots + s_{(n-2)} + 2\,s_{(n-1)}}{n} \qquad \checkmark$$

    **Odotetun hinnan johtaminen.** Koska $s_{(k)} = V + \sigma Z_{(k:n)}$:

    $$\mathbb{E}[P_\text{eng}] = V + \frac{\sigma}{n}\!\left(\sum_{k=1}^{n-2}\mathbb{E}[Z_{(k:n)}] + 2\,\mathbb{E}[Z_{(n-1:n)}]\right)$$

    Käyttäen $\sum_{k=1}^n \mathbb{E}[Z_{(k:n)}] = 0$, eli $\sum_{k=1}^{n-2}\mathbb{E}[Z_{(k:n)}] = -\mathbb{E}[Z_{(n-1:n)}] - \mathbb{E}[Z_{(n:n)}]$:

    $$\mathbb{E}[P_\text{eng}] = V + \frac{\sigma}{n}\!\left(-\mathbb{E}[Z_{(n-1:n)}] - \mathbb{E}[Z_{(n:n)}] + 2\,\mathbb{E}[Z_{(n-1:n)}]\right)
    = V - \frac{\sigma\!\left(\mathbb{E}[Z_{(n:n)}] - \mathbb{E}[Z_{(n-1:n)}]\right)}{n} \qquad \checkmark$$
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
    slider_V     = mo.ui.slider(10, 200, value=100, step=10, label="Todellinen arvo V")
    slider_n     = mo.ui.slider(2, 20, value=5, step=1, label="Tarjoajien määrä n")
    slider_sigma = mo.ui.slider(1, 50, value=20, step=1, label="Signaalivirhe σ")
    slider_N     = mo.ui.slider(1000, 50000, value=10000, step=1000, label="Simulaatiokerrat N")
    mo.vstack([slider_V, slider_n, slider_sigma, slider_N])
    return slider_N, slider_V, slider_n, slider_sigma


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

    def bid_adjustment_1st(n_bidders):
        """d(n) = c(n) + 1/E[Z_(n:n)]: winner's curse + strateginen alihinnoittelu"""
        if n_bidders <= 1:
            return 0.0
        def ez_fn(z):
            return n_bidders * z * _sci_norm.pdf(z) * _sci_norm.cdf(z)**(n_bidders - 1)
        ez_n, _ = _sci_int.quad(ez_fn, -15, 15)
        return bid_adjustment(n_bidders) + 1.0 / ez_n

    return bid_adjustment, bid_adjustment_1st


@app.cell
def _(bid_adjustment, bid_adjustment_1st, np, slider_N, slider_V, slider_n, slider_sigma):
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

    dn          = bid_adjustment_1st(n)
    price_1st   = sorted_s[:, -1] - sigma * dn
    utility_1st = V - price_1st

    # Järjestysstatistiikkojen odotusarvot (Monte Carlo, V kumoutuu)
    z_mc  = np.sort(np.random.default_rng(99).standard_normal(size=(200000, n)), axis=1)
    Ez_n1 = float(np.mean(z_mc[:, -2]))
    Ez_n  = float(np.mean(z_mc[:, -1]))

    eu_2nd_formula = sigma * (cn - Ez_n1)
    eu_eng_formula = sigma * (Ez_n - Ez_n1) / n
    eu_1st_formula = sigma * (dn - Ez_n)
    return (
        Ez_n,
        Ez_n1,
        V,
        cn,
        dn,
        eu_1st_formula,
        eu_2nd_formula,
        eu_eng_formula,
        n,
        price_1st,
        price_2nd,
        price_eng,
        price_naive,
        sigma,
        utility_1st,
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
    dn,
    eu_1st_formula,
    eu_2nd_formula,
    eu_eng_formula,
    mo,
    n,
    np,
    price_1st,
    price_2nd,
    price_eng,
    price_naive,
    sigma,
    utility_1st,
    utility_2nd,
    utility_eng,
    utility_naive,
):
    wc_naive = np.mean(utility_naive < 0) * 100
    wc_1st   = np.mean(utility_1st   < 0) * 100
    wc_2nd   = np.mean(utility_2nd   < 0) * 100
    wc_eng   = np.mean(utility_eng   < 0) * 100
    mo.md(f"""
    ### Tulokset: n={n}, σ={sigma}, V={V}

    $c(n) = {cn:.4f}$, $d(n) = {dn:.4f}$,
    $\\mathbb{{E}}[Z_{{(n-1:n)}}] = {Ez_n1:.4f}$,
    $\\mathbb{{E}}[Z_{{(n:n)}}] = {Ez_n:.4f}$

    | | Naiivi | 2nd rat. | 1st rat. | Eng. rat. |
    |---|---|---|---|---|
    | **E[utility] — kaava** | — | {eu_2nd_formula:.3f} | {eu_1st_formula:.3f} | {eu_eng_formula:.3f} |
    | **E[utility] — simulaatio** | {np.mean(utility_naive):.3f} | {np.mean(utility_2nd):.3f} | {np.mean(utility_1st):.3f} | {np.mean(utility_eng):.3f} |
    | **P(utility < 0)** | {wc_naive:.1f}% | {wc_2nd:.1f}% | {wc_1st:.1f}% | {wc_eng:.1f}% |
    | **E[hinta myyjälle]** | {np.mean(price_naive):.2f} | {np.mean(price_2nd):.2f} | {np.mean(price_1st):.2f} | {np.mean(price_eng):.2f} |

    Linkage Principle: 1st ({np.mean(price_1st):.2f}) < 2nd ({np.mean(price_2nd):.2f}) < Eng. ({np.mean(price_eng):.2f})
    """)
    return


@app.cell
def _(V, n, np, plt, price_1st, price_2nd, price_eng, price_naive, sigma):
    fig1, ax1 = plt.subplots(figsize=(10, 4))
    all_p = np.concatenate([price_naive, price_1st, price_2nd, price_eng])
    bins  = np.linspace(all_p.min() - 1, all_p.max() + 1, 60)
    ax1.hist(price_naive, bins=bins, alpha=0.35, color="#e07b39", label="Naiivi")
    ax1.hist(price_2nd,   bins=bins, alpha=0.35, color="#4c8fd6", label="Suljettu 2nd rat.")
    ax1.hist(price_1st,   bins=bins, alpha=0.35, color="#9b59b6", label="Suljettu 1st rat.")
    ax1.hist(price_eng,   bins=bins, alpha=0.35, color="#3daa6a", label="Eng. rat.")
    ax1.axvline(V, color="black", linewidth=1.5, linestyle="--", label=f"V = {V}")
    for p_arr, col in [(price_naive, "#e07b39"), (price_2nd, "#4c8fd6"), (price_1st, "#9b59b6"), (price_eng, "#3daa6a")]:
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
    ns    = np.arange(2, 31)
    cn_ns = np.array([bid_adjustment(ni) for ni in ns])

    eu_1st_ns   = np.zeros(len(ns))
    eu_2nd_ns   = np.zeros(len(ns))
    eu_eng_ns   = np.zeros(len(ns))
    wc_naive_ns = np.zeros(len(ns))
    wc_1st_ns   = np.zeros(len(ns))
    wc_2nd_ns   = np.zeros(len(ns))
    wc_eng_ns   = np.zeros(len(ns))

    for k, ni in enumerate(ns):
        z_k  = np.sort(np.random.default_rng(seed=k).standard_normal(size=(5000, ni)), axis=1)
        cn_k = cn_ns[k]
        dn_k = cn_k + 1.0 / np.mean(z_k[:, -1])
        eu_1st_ns[k]   = dn_k - np.mean(z_k[:, -1])
        eu_2nd_ns[k]   = cn_k - np.mean(z_k[:, -2])
        eu_eng_ns[k]   = (np.mean(z_k[:, -1]) - np.mean(z_k[:, -2])) / ni
        wc_naive_ns[k] = np.mean(z_k[:, -2] > 0) * 100
        wc_1st_ns[k]   = np.mean(z_k[:, -1] > dn_k) * 100
        wc_2nd_ns[k]   = np.mean(z_k[:, -2] > cn_k) * 100
        wc_eng_ns[k]   = np.mean(np.sum(z_k[:, :-2], axis=1) + 2 * z_k[:, -2] > 0) * 100

    fig2, axes = plt.subplots(1, 2, figsize=(12, 4))

    ax_eu = axes[0]
    ax_eu.plot(ns, eu_2nd_ns,  color="#4c8fd6", linewidth=2, label="Suljettu 2nd rat.")
    ax_eu.plot(ns, eu_1st_ns,  color="#9b59b6", linewidth=2, label="Suljettu 1st rat.")
    ax_eu.plot(ns, eu_eng_ns,  color="#3daa6a", linewidth=2, linestyle="--", label="Eng. rat.")
    ax_eu.axhline(0, color="black", linewidth=1, linestyle="--")
    ax_eu.axvline(n, color="gray", linewidth=1, linestyle=":", alpha=0.8)
    ax_eu.set_xlabel("Tarjoajien määrä n")
    ax_eu.set_ylabel("E[utility] / σ")
    ax_eu.set_title("Odotettu utility n:n funktiona (yksikköinä σ)")
    ax_eu.legend()

    ax_wc = axes[1]
    ax_wc.plot(ns, wc_naive_ns, color="#e07b39", linewidth=2, label="Naiivi")
    ax_wc.plot(ns, wc_2nd_ns,   color="#4c8fd6", linewidth=2, label="Suljettu 2nd rat.")
    ax_wc.plot(ns, wc_1st_ns,   color="#9b59b6", linewidth=2, label="Suljettu 1st rat.")
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
