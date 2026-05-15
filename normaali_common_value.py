import marimo

__generated_with = "0.23.1"
app = marimo.App(width="medium")


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Common Value-huutokauppa: normaalijakautuneet signaalit

    ## Johdanto

     Motivoiduin pohtimaan huutokauppamekanismien vaikutusta myytävän tuotteen hintaan Helsingin asuinrakentamistonttien luovuttamisen kautta. Asuntotontit eivät vastaa täysin tätä ideaalista ympäristöä, missä myytävän kohteen arvo on tasan sama kaikille. Mutta tässä havainnollistetut huutokauppamekanismin vaikutukset hintaan pätevät myös silloin, kun huutokaupan kohteen arvo on osaksi yhteinen ja osaksi yksityinen rakennuttajien kesken.

     Huutokaupassa myydään kohde, jonka todellinen arvo $V$ on **sama kaikille** mutta
    **tuntematon** (common value). Kukin ostajaehdokas saa yksityisen, kohinaisen signaalin $V$:stä.

    Tässä muistiossa esitellään (ja johdetaan) tasapainostrategiat kolmelle
    huutokauppamuodolle analyyttisesti ja vahvistetaan tulokset Monte Carlo -simulaatiolla.

    Muistiossa vertaillaan kolmea eri huutokauppamekanismia:
    1. **Second-price sealed-bid auction** Huutokauppa, jossa tarjoajat jättävät tarjouksen suljettuun kirjekuoreen. Korkeimman tarjouksen jättänyt on velvollinen ostamaan huutokaupan kohteen toiseksi korkeimman tarjouksen hinnalla
    2. **First-price sealed-bid auction** Huutokauppa, jossa tarjoajat jättävät tarjouksen suljettuun kirjekuoreen. Korkeimman tarjouksen jättänyt on velvollinen ostamaan huutokaupan kohteen tarjoamallaan hinnalla.
    3. **Avoin huutokauppa** Huutokauppa, jossa hinta nousee jatkuvasti ja tarjoajat pysyvät mukana kunnes hinta ylittää oman kynnysarvonsa. Viimeisenä jäljelle jäävä voittaa ja maksaa hinnan, jolla toiseksi viimeinen tippui pois.

    Alla esitetään tulokset näiden protokollien välillä, kun tarjoajat käyttävät tarjoajien hyödyn maksimoivaa strategiaa tarjoamiseen ja vertailun vuoksi strategiaa, missä tarjoavat oman signaalinsa verran.

    **Keskeiset tulokset** (merkinnät: $c_n$, $d_n$, $E_k = \mathbb{E}[Z_{(k:n)}]$ lasketaan numeerisesti):

    | | Ostajan E[utility] | Myyjän E[tulo] |
    |---|---|---|
    | Tarjous = oma signaali | $-\sigma\,E_{n-1}$ | $V + \sigma\,E_{n-1}$ |
    | Suljettu 2nd price optimistrategia | $\sigma(c_n - E_{n-1})$ | $V - \sigma(c_n - E_{n-1})$ |
    | Suljettu 1st price optimistrategia | $\sigma(d_n - E_n)$ | $V - \sigma(d_n - E_n)$ |
    | Avoimen huutokaupan optimistrategia | $\dfrac{\sigma(E_n - E_{n-1})}{n}$ | $V - \dfrac{\sigma(E_n - E_{n-1})}{n}$ |

    **Johtopäätökset:**

    1. Vaikka tarjoajan saama tieto huutokaupan kohteen arvosta on harhaton, eli vastaa keskimäärin huutokaupan kohteen arvoa, niin jos tarjoaja tarjoaa oman tietonsa verran, niin huutokaupan voittaja maksaa keskimäärin liikaa, jos tarjoajia on yli 3. Optimistrategioissa tarjoukset ovat matalampia kuin yksityinen tieto kohteen arvosta.

    2. Suljettu 2nd price -huutokauppa tuottaa myyjälle enemmän tuloa kuin suljettu 1st price -huutokauppa. 1st price -huutokaupassa tarjoajan täytyy sheidaa tarjouksensa enemmän, koska oma bid on myös maksettu hinta — sheidaus kompensoi täsmälleen sen informaatioedun, jonka winner's curse aiheuttaa. Yhtälöisten tulojen periaate (revenue equivalence) pätee vain *yksityisten arvojen* tapauksessa, ei common value -huutokaupoissa.

    3. Avoin huutokauppa tuottaa myyjälle suuremman tulon kuin suljetut huutokaupat. Tämä johtuu siitä, että huutokaupan aikana muiden tarjoajien käyttäytyminen tuo julkiseksi tietoa huutokaupan kohteen arvosta, joka keskimäärin kasvattaa tarjoajien maksuhalukkuutta.


    ---

    ## 1. Malli

    Kohteella on **yksi todellinen arvo** $V$, joka on sama kaikille tarjoajille mutta tuntematon.
    Kukin $n$ tarjoajista saa yksityisen **signaalin**

    $$s_i = V + \varepsilon_i, \qquad \varepsilon_i \overset{\text{iid}}{\sim} N(0,\,\sigma^2)$$

    Tarjoaja tietää oman signaalinsa $s_i$ mutta ei muiden signaaleja eikä $V$:tä.

    ---

    ## 2. Protokollat

    ### 2.1 Suljettu second-price huutokauppa (Vickrey)

    Jokainen tarjoaja jättää salaisen tarjouksen. Korkein tarjoaja voittaa ja **maksaa toiseksi
    korkeimman tarjouksen**.

    ### 2.2 Suljettu first-price huutokauppa

    Jokainen tarjoaja jättää salaisen tarjouksen. Korkein tarjoaja voittaa ja **maksaa oman
    tarjouksensa**.

    ### 2.3 Avoin huutokauppa

    Hinta nousee jatkuvasti. Kukin tarjoaja pysyy mukana kunnes hinta ylittää oman strategiansa
    mukaisen kynnyksen. Viimeisenä jäljelle jäävä voittaa ja maksaa hinnan, jolla toiseksi
    viimeinen tippui pois.

    ---

    ## 3. Järjestysstatistiikat

    Kirjoitetaan $\varepsilon_i = \sigma Z_i$ missä $Z_i \sim N(0,1)$, ja merkitään $Z_{(k:n)}$
    standardinormaalijakauman $k$:nneksi pienimmäksi arvoksi (kasvavassa järjestyksessä).
    Tällöin $s_{(k:n)} = V + \sigma Z_{(k:n)}$ ja

    $$\mathbb{E}[s_{(k:n)}] = V + \sigma\,\mathbb{E}[Z_{(k:n)}]$$

    $Z_{(k:n)}$:n odotusarvoille ei ole suljettua muotoa. Keskeisimmät ominaisuudet:

    $$\mathbb{E}[Z_{(k:n)}] = -\mathbb{E}[Z_{(n-k+1:n)}] \qquad \text{(symmetria)}$$

    $$\sum_{k=1}^n \mathbb{E}[Z_{(k:n)}] = 0 \qquad \text{(summautuu nollaan)}$$

    Odotusarvot lasketaan numeerisesti Monte Carlo -simulaatiolla.

    ---

    ## 4. Benchmark strategia 2nd price huutokaupassa: jokainen ostaja tarjoaa oman signaalinsa verran

    Tarjoaja tarjoaa suoraan signaalinsa: $b_i = s_i$.

    **Myyjän odotettu tulo.** Voittaja on korkein signaali $s_{(n:n)}$, hinta on toiseksi
    korkein signaali $s_{(n-1:n)} = V + \sigma Z_{(n-1:n)}$:

    $$\mathbb{E}[P_\text{naiivi}] = \mathbb{E}[s_{(n-1:n)}] = V + \sigma\,\mathbb{E}[Z_{(n-1:n)}]$$

    Huomaa: kun $n > 3$, myyjä saa *enemmän* kuin $V$ — winner's curse siirtää rahaa ostajalta myyjälle.

    **Ostajan odotettu utility.** Koska $\mathbb{E}[U] = V - \mathbb{E}[P]$:

    $$\mathbb{E}[U_\text{naiivi}] = -\sigma\,\mathbb{E}[Z_{(n-1:n)}]$$

    Tämä on **negatiivinen kun $n > 3$** — winner's curse iskee.

    ---

    ## 5. Optimistrategia suljetussa 2nd price huutokaupassa

    $$\boxed{b^*(s_i) = s_i - \sigma\,c(n)}$$

    missä $c(n) \geq 0$ on numeerisesti laskettava winner's curse -korjaus.
    Suljettu muoto vain $n = 3$: $c(3) = 1/\!\sqrt{3\pi} \approx 0{,}326$.

    **Myyjän odotettu tulo.** Hinta = toiseksi korkein tarjous $= b^*(s_{(n-1:n)}) = s_{(n-1:n)} - \sigma\,c(n)$:

    $$\mathbb{E}[P_\text{2nd}] = \mathbb{E}[s_{(n-1:n)}] - \sigma\,c(n)
    = V + \sigma\,\mathbb{E}[Z_{(n-1:n)}] - \sigma\,c(n) = V - \sigma\bigl(c(n) - \mathbb{E}[Z_{(n-1:n)}]\bigr)$$

    **Ostajan odotettu utility.** Koska $\mathbb{E}[U] = V - \mathbb{E}[P]$:

    $$\mathbb{E}[U_\text{2nd}] = \sigma\bigl(c(n) - \mathbb{E}[Z_{(n-1:n)}]\bigr) \qquad \checkmark$$

    [→ Liite A: Optimistrategian johtaminen](#liite-a)

    ---

    ## 6. Optimistrategia suljetussa 1st price huutokaupassa

    $$\boxed{b^*(s_i) = s_i - \sigma\,d(n)}, \qquad d(n) = c(n) + \frac{1}{\mathbb{E}[Z_{(n:n)}]}$$

    **Myyjän odotettu tulo.** Voittaja on korkein signaali $s_{(n:n)}$ ja maksaa oman
    tarjouksensa $b^*(s_{(n:n)}) = s_{(n:n)} - \sigma\,d(n)$:

    $$\mathbb{E}[P_\text{1st}] = \mathbb{E}[b^*(s_{(n:n)})] = \mathbb{E}[s_{(n:n)}] - \sigma\,d(n)
    = V + \sigma\,\mathbb{E}[Z_{(n:n)}] - \sigma\,d(n) = V - \sigma\bigl(d(n) - \mathbb{E}[Z_{(n:n)}]\bigr)$$

    **Ostajan odotettu utility.** Koska $\mathbb{E}[U] = V - \mathbb{E}[P]$:

    $$\mathbb{E}[U_\text{1st}] = \sigma\bigl(d(n) - \mathbb{E}[Z_{(n:n)}]\bigr) \qquad \checkmark$$

    **Vertailu 2nd priceen:** $\mathbb{E}[P_\text{1st}] < \mathbb{E}[P_\text{2nd}]$ — 1st price tuottaa
    **matalamman** odotetun hinnan kuin 2nd price. Tarjoajan täytyy sheida enemmän, koska oma bid on myös maksettu hinta.

    [→ Liite B: Optimistrategian johtaminen](#liite-b)

    ---

    ## 7. Optimistrategia avoimessa huutokaupassa

    Avoimessa huutokaupassa tarjoajat eivät jätä suljettua tarjousta — he pysyvät
    mukana kunnes hinta ylittää oman kynnysarvonsa ja **tippuvat pois**. Strategia on siis
    tippumishinta $p(s_i)$, ei tarjous $b$. Optimaalinen poisjääntihinta ehdollistaa kaikkiin
    aiemmin paljastuneisiin signaaleihin. Voittaja maksaa hinnan, jolla toiseksi viimeinen tippui pois.

    $$\boxed{p_k = \frac{s_{(1)} + \cdots + s_{(k-1)} + 2\,s_{(k)}}{k+1}}, \qquad k = 1,\ldots,n-1$$

    Voittaja maksaa $p_{n-1} = \dfrac{s_{(1)} + \cdots + s_{(n-2)} + 2\,s_{(n-1)}}{n}$.

    **Myyjän odotettu tulo.** Käyttäen $\sum_{k=1}^n \mathbb{E}[Z_{(k:n)}] = 0$:

    $$\mathbb{E}[P_\text{avoin}] = V - \frac{\sigma\bigl(\mathbb{E}[Z_{(n:n)}] - \mathbb{E}[Z_{(n-1:n)}]\bigr)}{n}$$

    **Ostajan odotettu utility.** Koska $\mathbb{E}[U] = V - \mathbb{E}[P]$:

    $$\mathbb{E}[U_\text{avoin}] = \frac{\sigma\bigl(\mathbb{E}[Z_{(n:n)}] - \mathbb{E}[Z_{(n-1:n)}]\bigr)}{n} \qquad \checkmark$$

    **Tuottoranking myyjälle:**

    $$\mathbb{E}[\text{hinta}]:\quad \text{naiivi} \;\geq\; \text{avoin rat.} \;\geq\; \text{suljettu 2nd rat.} \;\geq\; \text{suljettu 1st rat.}$$

    Kytkentäperiaate: $\mathbb{E}[P_\text{avoin}] \geq \mathbb{E}[P_\text{2nd}] > \mathbb{E}[P_\text{1st}]$
    kaikilla $n \geq 2$. ✓

    [→ Liite C: Tippumishinnan johtaminen](#liite-c)

    ---

    <a id="liite-a"></a>
    ## Liite A: 2nd price optimistrategian johtaminen

    **Keskeinen oivallus.** 2nd price -huutokaupassa tasapainoehto ei ole
    "mikä on E[V] ehdolla, että voitan outright?" vaan
    **"millä tarjouksella olen välinpitämätön korottamaan tarjoustani, kun olen
    tasapisteessä toiseksi korkeimman tarjoajan kanssa?"**

    Merkitään $Y_1 = \max_{j \neq i} s_j$ (korkein kilpailijan signaali). Tasapainoehto:

    $$b^*(s) = \mathbb{E}[V \mid s_i = s,\; Y_1 = s]$$

    Johdetaan posteriori Bayesin kaavalla. Tiheys $Y_1 = s$ ehdolla $V$ on järjestysstatistiikan tiheys:
    yksi kilpailija saa signaalin $s$ (tiheys $\varphi(\frac{s-V}{\sigma})/\sigma$) ja loput $n-2$ saavat signaalin $< s$
    (todennäköisyys $\Phi(\frac{s-V}{\sigma})$ kullakin):

    $$f_{Y_1}(s \mid V) = (n-1)\cdot\frac{\varphi\!\left(\frac{s-V}{\sigma}\right)}{\sigma}\cdot\Phi\!\left(\frac{s-V}{\sigma}\right)^{n-2}$$

    Tasaisella priorilla $p(V) \propto 1$:

    $$f(V \mid s_i=s,\, Y_1=s) \;\propto\;
    \underbrace{\frac{\varphi\!\left(\frac{s-V}{\sigma}\right)}{\sigma}}_{f(s_i=s|V)}
    \cdot \underbrace{(n-1)\frac{\varphi\!\left(\frac{s-V}{\sigma}\right)}{\sigma}\Phi\!\left(\frac{s-V}{\sigma}\right)^{n-2}}_{f_{Y_1}(s|V)}
    \;\propto\; \varphi\!\left(\frac{s-V}{\sigma}\right)^{\!2} \cdot \Phi\!\left(\frac{s-V}{\sigma}\right)^{n-2}$$

    Sijoitus $z = (s-V)/\sigma$, $V = s - \sigma z$, $dV = -\sigma\,dz$. Optimaalinen tarjous:

    $$b^*(s) = s - \sigma \cdot \underbrace{\frac{\displaystyle\int_{-\infty}^{\infty} z\;\varphi(z)^2\;\Phi(z)^{n-2}\,dz}
    {\displaystyle\int_{-\infty}^{\infty} \varphi(z)^2\;\Phi(z)^{n-2}\,dz}}_{=\;c(n)}
    \;=\; s - \sigma\,c(n) \qquad \checkmark$$

    **Analyyttinen ratkaisu $n=3$:**

    *Nimittäjä:* symmetriaargumentilla $\int\varphi(z)^2\Phi(z)\,dz = \int\varphi(z)^2\Phi(-z)\,dz$,
    joten $2\int\varphi(z)^2\Phi(z)\,dz = \int\varphi(z)^2\,dz = \tfrac{1}{2\sqrt{\pi}}$,
    eli nimittäjä $= \tfrac{1}{4\sqrt{\pi}}$.

    *Osoittaja:* osin integroimalla $\int z\,\varphi(z)^2\,\Phi(z)\,dz = -\tfrac{1}{4\pi\sqrt{3}}$.

    $$c(3) = \frac{1/(4\pi\sqrt{3})}{1/(4\sqrt{\pi})} = \frac{1}{\sqrt{3\pi}} \approx 0{,}326$$

    **Yleiselle $n$:lle** integroidaan numeerisesti (`scipy.integrate.quad`).

    **Erikoistapaus $n=2$:** $c(2) = 0$ — sheidausta ei lainkaan. Marginaalivoittotilanteessa
    ainoa kilpailija on tasapisteessä $Y_1 = s$, joten posteriori on symmetrinen $N(s,\,\sigma^2)$
    ja $\mathbb{E}[V] = s$.

    ---

    <a id="liite-b"></a>
    ## Liite B: 1st price optimistrategian johtaminen

    **Siirtymäinvarianssi — lineaarinen tasapaino.** Koska signaalivirheet ovat normaalijakautuneita
    (siirtymäinvariantti jakauma), symmetrinen BNE on lineaarinen:
    $b^*(s) = s - \sigma\,d(n)$ jollakin vakiolla $d(n)$, ja $(b^*)'(s) = 1$.

    **Ensimmäisen kertaluvun ehto (FOC).** Symmetrisessä tasapainossa marginaalivoittajatilanteessa
    $Y_1 = s_i = s$:

    $$\bigl(\underbrace{\mathbb{E}[V \mid s_i, Y_1 = s_i]}_{=\;s - \sigma\,c(n)}
    \;-\; b^*(s)\bigr)\cdot f_{Y_1|s}(s)
    \;=\; (b^*)'(s)\cdot P(Y_1 < s \mid s)$$

    **Kilpailijoiden signaalit ovat korreloituneita.** Vaikka kukin $s_j \mid s_i = s$
    on marginaalisesti $N(s, 2\sigma^2)$, ne eivät ole riippumattomia — kaikkia yhdistää
    yhteinen tuntematon $V$. Oikea laskutapa käyttää odotusarvon lakia:

    $$P(Y_1 < s \mid s_i = s)
    = \mathbb{E}_{V \mid s}\!\left[\Phi\!\left(\tfrac{s-V}{\sigma}\right)^{n-1}\right]
    = \int_{-\infty}^{\infty} \Phi(z)^{n-1}\,\varphi(z)\,dz = \frac{1}{n}$$

    (sijoitus $u = \Phi(z)$: $\int_0^1 u^{n-1}\,du = 1/n$).

    **Tiheys pistessä $Y_1 = s$ ehdolla $s_i = s$:**

    $$f_{Y_1|s}(s) = \frac{n-1}{\sigma}\int_{-\infty}^{\infty}\Phi(z)^{n-2}\varphi(z)^2\,dz
    = \frac{\mathbb{E}[Z_{(n:n)}]}{n\sigma}$$

    Viimeisin yhtäsuuruus seuraa identiteetistä $\mathbb{E}[Z_{(n:n)}] = n(n-1)\int\Phi(z)^{n-2}\varphi(z)^2\,dz$
    (johdetaan osin integroimalla).

    **FOC:n ratkaisu.** Sijoitetaan $b^*(s) = s - \sigma d$, $(b^*)' = 1$:

    $$\sigma(d - c(n))\cdot\frac{\mathbb{E}[Z_{(n:n)}]}{n\sigma} = \frac{1}{n}$$

    $$\boxed{d(n) = c(n) + \frac{1}{\mathbb{E}[Z_{(n:n)}]}} \qquad \checkmark$$

    Strateginen alihinnoittelu 1st vs 2nd price on $\sigma/\mathbb{E}[Z_{(n:n)}]$: suurempi kun
    kilpailijoita on vähän, pienempi kun kilpailijoita on paljon.

    ---

    <a id="liite-c"></a>
    ## Liite C: Avoimen huutokaupan tippumishinnan johtaminen

    **Ensimmäinen tippuja ($k = 1$).**
    Ensimmäisen tippujan utility on **nolla riippumatta tippumishinnasta** — heillä on matalin
    signaali, joten he eivät koskaan voita. Siksi yksittäisen tarjoajan kannustin on
    välinpitämätön tippumishetken suhteen, ja mikä tahansa kasvava $\beta_1(s)$ voisi ensi
    näkemältä tuntua tasapainolta.

    Tasapaino on kuitenkin $p_1 = s_{(1)}$, eikä tämä ole vain sopimuskysymys. Osoitetaan,
    että $\beta(s) = s$ on Nashin tasapaino, kun otetaan huomioon muidenkin pelaajien kannustimet.

    **Miksi $\beta(s) = s - \varepsilon$ ei ole tasapaino ($\varepsilon > 0$)?**
    Jos kaikki pelaavat strategiaa $\beta(s) = s - \varepsilon$, pelaaja $i$ voi poiketa
    strategiaan $\beta(s) = s - \gamma$ missä $\gamma < \varepsilon$. Tällöin pelaaja $i$
    tippuu myöhemmin kuin kilpailijansa — mutta koska kilpailijat tippuvat ensin,
    pelaaja $i$ voittaa halvemmalla kuin ilman poikkeamaa.
    Siis mikä tahansa $\beta(s) = s - \varepsilon$ synnyttää kilpajuoksun ylöspäin.

    **Miksi kilpajuoksu pysähtyy $\beta(s) = s$:ään?**
    Kun kaikki pelaavat $\beta(s) = s$, pieni poikkeama ylöspäin ($+\delta$) tai alaspäin
    ($-\gamma$) tuottaa kumpikin $\Delta U < 0$. $\beta(s) = s$ on **Nashin tasapaino**.

    Kaava $p_k = (s_{(1)} + \cdots + s_{(k-1)} + 2\,s_{(k)})/(k+1)$ pätee myös $k=1$:lle, sillä
    $p_1 = 2s_{(1)}/2 = s_{(1)}$ ✓

    **Myöhemmät tippujat ($k \geq 2$).**
    Tarjoaja $k$ (signaali $s_{(k)}$) tietää oman signaalinsa ja on havainnut aiempien
    tippumisten hinnat $p_1 = s_{(1)}, \ldots, p_{k-1} = s_{(k-1)}$.

    Normaalijakauman konjugaattiominaisuus: ehdollistaen kaikille $k-1$ paljastuneelle signaalille
    ja omalle signaalille $s_{(k)}$ posteriori on $N\!\left(\frac{s_{(1)}+\cdots+s_{(k-1)}+s_{(k)}}{k},\; \frac{\sigma^2}{k}\right)$.

    Tasapainoehto: tipu kun hinta saavuttaa $V$:n posterioriodotusarvon
    **marginaalivoittotilanteessa** $s_{k+1} = s_{(k)}$. Ehdollistetaan $k+1$ signaalille
    (k-1 aiempaa $+$ oma $+$ marginaalinen kilpailija $s_{(k)}$). Normaaliposteriorin odotusarvo:

    $$p_k = \mathbb{E}\!\left[V \mid s_{(1)},\ldots,s_{(k-1)},\, s_{(k)},\, s_{k+1} = s_{(k)}\right]
    = \frac{s_{(1)} + \cdots + s_{(k-1)} + 2\,s_{(k)}}{k+1} \qquad \checkmark$$

    **Toiseksi viimeinen tippuja ($k = n-1$)** määrää hinnan.
    Kaikki $n-2$ matalampaa signaalia ovat jo paljastuneet:

    $$P = p_{n-1} = \frac{s_{(1)} + \cdots + s_{(n-2)} + 2\,s_{(n-1)}}{n} \qquad \checkmark$$

    **Odotetun hinnan johtaminen.** Koska $s_{(k)} = V + \sigma Z_{(k:n)}$ ja
    $\sum_{k=1}^n \mathbb{E}[Z_{(k:n)}] = 0$:

    $$\mathbb{E}[P_\text{avoin}] = V + \frac{\sigma}{n}\!\Bigl(\underbrace{\mathbb{E}[Z_{(1:n)}]+\cdots+\mathbb{E}[Z_{(n-2:n)}]}_{=-\,\mathbb{E}[Z_{(n-1:n)}]-\mathbb{E}[Z_{(n:n)}]} + 2\,\mathbb{E}[Z_{(n-1:n)}]\Bigr)
    = V - \frac{\sigma\bigl(\mathbb{E}[Z_{(n:n)}] - \mathbb{E}[Z_{(n-1:n)}]\bigr)}{n} \qquad \checkmark$$
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

    # --- Naiivi ---
    price_naive   = sorted_s[:, -2]
    utility_naive = V - price_naive

    # --- Suljettu second-price rationaalinen ---
    cn           = bid_adjustment(n)
    bids_2nd     = signals - sigma * cn
    price_2nd    = np.sort(bids_2nd, axis=1)[:, -2]
    utility_2nd  = V - price_2nd

    # --- Suljettu first-price rationaalinen ---
    dn           = bid_adjustment_1st(n)
    bids_1st     = signals - sigma * dn
    price_1st    = np.max(bids_1st, axis=1)
    utility_1st  = V - price_1st

    # --- Avoin rationaalinen: p_{n-1} = (s_(1)+...+s_(n-2) + 2*s_(n-1)) / n ---
    price_avoin   = (np.sum(sorted_s[:, :-1], axis=1) + sorted_s[:, -2]) / n
    utility_avoin = V - price_avoin

    # --- Järjestysstatistiikkojen odotusarvot (Monte Carlo) ---
    z_mc  = np.sort(np.random.default_rng(99).standard_normal(size=(200000, n)), axis=1)
    Ez_n1 = float(np.mean(z_mc[:, -2]))
    Ez_n  = float(np.mean(z_mc[:, -1]))

    # --- Analyyttiset odotusarvot ---
    eu_naive_formula = -sigma * Ez_n1
    eu_2nd_formula   = sigma * (cn - Ez_n1)
    eu_1st_formula   = sigma * (dn - Ez_n)
    eu_avoin_formula = sigma * (Ez_n - Ez_n1) / n
    return (
        Ez_n,
        Ez_n1,
        V,
        bids_1st,
        bids_2nd,
        cn,
        dn,
        eu_1st_formula,
        eu_2nd_formula,
        eu_avoin_formula,
        eu_naive_formula,
        n,
        price_1st,
        price_2nd,
        price_avoin,
        price_naive,
        sigma,
        signals,
        utility_1st,
        utility_2nd,
        utility_avoin,
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
    eu_avoin_formula,
    eu_naive_formula,
    mo,
    n,
    np,
    price_1st,
    price_2nd,
    price_avoin,
    price_naive,
    sigma,
    utility_1st,
    utility_2nd,
    utility_avoin,
    utility_naive,
):
    wc_naive = np.mean(utility_naive < 0) * 100
    wc_2nd   = np.mean(utility_2nd   < 0) * 100
    wc_1st   = np.mean(utility_1st   < 0) * 100
    wc_avoin = np.mean(utility_avoin  < 0) * 100
    mo.md(f"""
    ### Tulokset: n={n}, σ={sigma}, V={V}, c(n)={cn:.4f}, d(n)={dn:.4f}

    $\\mathbb{{E}}[Z_{{(n-1:n)}}] = {Ez_n1:.4f}$,
    $\\mathbb{{E}}[Z_{{(n:n)}}] = {Ez_n:.4f}$

    | | Naiivi | 2nd rat. | 1st rat. | Avoin rat. |
    |---|---|---|---|---|
    | **E[utility] — kaava** | {eu_naive_formula:.3f} | {eu_2nd_formula:.3f} | {eu_1st_formula:.3f} | {eu_avoin_formula:.3f} |
    | **E[utility] — simulaatio** | {np.mean(utility_naive):.3f} | {np.mean(utility_2nd):.3f} | {np.mean(utility_1st):.3f} | {np.mean(utility_avoin):.3f} |
    | **P(utility < 0)** | {wc_naive:.1f}% | {wc_2nd:.1f}% | {wc_1st:.1f}% | {wc_avoin:.1f}% |
    | **E[hinta myyjälle]** | {np.mean(price_naive):.2f} | {np.mean(price_2nd):.2f} | {np.mean(price_1st):.2f} | {np.mean(price_avoin):.2f} |

    Kytkentäperiaate: 1st ({np.mean(price_1st):.2f}) < 2nd ({np.mean(price_2nd):.2f}) < Avoin ({np.mean(price_avoin):.2f})
    """)
    return


@app.cell
def _(V, n, np, plt, price_1st, price_2nd, price_avoin, price_naive, sigma):
    fig1, ax1 = plt.subplots(figsize=(10, 4))
    all_p = np.concatenate([price_naive, price_2nd, price_1st, price_avoin])
    bins = np.linspace(all_p.min() - 1, all_p.max() + 1, 60)
    ax1.hist(price_naive, bins=bins, alpha=0.40, color="#e07b39", label="Naiivi")
    ax1.hist(price_2nd,   bins=bins, alpha=0.40, color="#4c8fd6", label="Suljettu 2nd rat.")
    ax1.hist(price_1st,   bins=bins, alpha=0.40, color="#9b59b6", label="Suljettu 1st rat.")
    ax1.hist(price_avoin, bins=bins, alpha=0.40, color="#3daa6a", label="Avoin rat.")
    ax1.axvline(V, color="black", linewidth=1.5, linestyle="--", label=f"V = {V}")
    for p_arr, col in [
        (price_naive, "#e07b39"),
        (price_2nd,   "#4c8fd6"),
        (price_1st,   "#9b59b6"),
        (price_avoin, "#3daa6a"),
    ]:
        ax1.axvline(np.mean(p_arr), color=col, linewidth=2)
    ax1.set_xlabel("Voittajan maksama hinta")
    ax1.set_ylabel("Frekvenssi")
    ax1.set_title(f"Maksettujen hintojen jakauma  (n={n}, σ={sigma}, V={V})")
    ax1.legend(fontsize=8)
    fig1.tight_layout()
    fig1
    return


@app.cell
def _(V, bids_1st, bids_2nd, cn, dn, n, np, plt, sigma, signals):
    idx = np.random.default_rng(0).integers(0, signals.shape[0], 300)
    s_sample  = signals[idx].ravel()
    b2_sample = bids_2nd[idx].ravel()
    b1_sample = bids_1st[idx].ravel()

    fig2, ax2 = plt.subplots(figsize=(6, 5))
    s_line = np.linspace(s_sample.min(), s_sample.max(), 100)
    ax2.plot(s_line, s_line,                  "k--",       linewidth=1,  label="b = s  (naiivi)")
    ax2.plot(s_line, s_line - sigma * cn, color="#4c8fd6", linewidth=2,  label=f"2nd rat.: b = s − σc(n)  (σc={sigma*cn:.2f})")
    ax2.plot(s_line, s_line - sigma * dn, color="#9b59b6", linewidth=2,  label=f"1st rat.: b = s − σd(n)  (σd={sigma*dn:.2f})")
    ax2.axvline(V, color="gray", linewidth=1, linestyle=":", label=f"V={V}")
    ax2.set_xlabel("Signaali $s_i$")
    ax2.set_ylabel("Tarjous $b_i$")
    ax2.set_title(f"Bid sheidaus vertailu  (n={n}, σ={sigma})")
    ax2.legend(fontsize=8)
    fig2.tight_layout()
    fig2
    return


@app.cell
def _(bid_adjustment, n, np, plt):
    ns    = np.arange(2, 31)
    cn_ns = np.array([bid_adjustment(ni) for ni in ns])

    eu_2nd_ns   = np.zeros(len(ns))
    eu_1st_ns   = np.zeros(len(ns))
    eu_avoin_ns = np.zeros(len(ns))
    wc_naive_ns = np.zeros(len(ns))
    wc_2nd_ns   = np.zeros(len(ns))
    wc_1st_ns   = np.zeros(len(ns))
    wc_avoin_ns = np.zeros(len(ns))

    for k, ni in enumerate(ns):
        z_k  = np.sort(np.random.default_rng(seed=k).standard_normal(size=(5000, ni)), axis=1)
        cn_k = cn_ns[k]
        dn_k = cn_k + 1.0 / np.mean(z_k[:, -1])
        eu_2nd_ns[k]   = cn_k - np.mean(z_k[:, -2])
        eu_1st_ns[k]   = dn_k - np.mean(z_k[:, -1])
        eu_avoin_ns[k] = (np.mean(z_k[:, -1]) - np.mean(z_k[:, -2])) / ni
        wc_naive_ns[k] = np.mean(z_k[:, -2] > 0) * 100
        wc_2nd_ns[k]   = np.mean(z_k[:, -2] > cn_k) * 100
        wc_1st_ns[k]   = np.mean(z_k[:, -1] > dn_k) * 100
        wc_avoin_ns[k] = np.mean(np.sum(z_k[:, :-2], axis=1) + 2 * z_k[:, -2] > 0) * 100

    fig3, axes = plt.subplots(1, 2, figsize=(12, 4))

    ax_eu = axes[0]
    ax_eu.plot(ns, eu_2nd_ns,   color="#4c8fd6", linewidth=2, label="Suljettu 2nd rat.")
    ax_eu.plot(ns, eu_1st_ns,   color="#9b59b6", linewidth=2, label="Suljettu 1st rat.")
    ax_eu.plot(ns, eu_avoin_ns, color="#3daa6a", linewidth=2, linestyle="--", label="Avoin rat.")
    ax_eu.axhline(0, color="black", linewidth=1, linestyle="--")
    ax_eu.axvline(n, color="gray", linewidth=1, linestyle=":", alpha=0.8)
    ax_eu.set_xlabel("Tarjoajien määrä n")
    ax_eu.set_ylabel("E[voittajan utility] / σ")
    ax_eu.set_title("Odotettu utility n:n funktiona (yksikköinä σ)")
    ax_eu.legend()

    ax_wc = axes[1]
    ax_wc.plot(ns, wc_naive_ns, color="#e07b39", linewidth=2, label="Naiivi")
    ax_wc.plot(ns, wc_2nd_ns,   color="#4c8fd6", linewidth=2, label="Suljettu 2nd rat.")
    ax_wc.plot(ns, wc_1st_ns,   color="#9b59b6", linewidth=2, label="Suljettu 1st rat.")
    ax_wc.plot(ns, wc_avoin_ns, color="#3daa6a", linewidth=2, linestyle="--", label="Avoin rat.")
    ax_wc.axhline(50, color="black", linewidth=1, linestyle="--", alpha=0.5)
    ax_wc.axvline(n, color="gray", linewidth=1, linestyle=":", alpha=0.8, label=f"Nykyinen n={n}")
    ax_wc.set_xlabel("Tarjoajien määrä n")
    ax_wc.set_ylabel("P(utility < 0)  [%]")
    ax_wc.set_title("Winner's curse -todennäköisyys")
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
