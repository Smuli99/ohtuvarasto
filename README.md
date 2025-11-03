# Ohjelmistotuotanto, TEKA2500
[![GHA workflow badge](https://github.com/Smuli99/ohtuvarasto/workflows/CI/badge.svg)](https://github.com/Smuli99/ohtuvarasto/actions)
[![codecov](https://codecov.io/github/Smuli99/ohtuvarasto/graph/badge.svg?token=C9F1QW344Q)](https://codecov.io/github/Smuli99/ohtuvarasto)

Kurssin ensimmäisen viikon tehtävä palautuksia varten luotu repositorio

## 1. Gitin alkeen [versionhallinta]

<details>
<summary>Tehtävät</summary>

**Tee nyt seuraavat asiat:**

- Mene edellisessä tehtävässä luotuun repositorion klooniin (eli komennon ```git clone``` luomaan hakemistoon)
- Lisää ja committaa repositorioon kaksi tiedostoa ja kaksi hakemistoa, joiden sisällä on tiedostoja
  - Muista hyödyllinen komento ```git status```
- Muuta ainakin kahden tiedoston sisältöä ja committaa muutokset repositorioon
- Tee .gitignore-tiedosto, jossa määrittelet, että repositorion juurihakemistossa olevat tiedostot, joiden pääte on tmp, ja hakemistot joiden nimi on __pycache__ ja .pytest_cache ignoroidaan
  - Toinen ignorattava hakemisto on siis .pytest_cache, jonka nimi alkaa pisteellä
  - Pistealkuiset hakemistot ja tiedostot eivät näy oletusarvoisesti komennon ls listauksissa, saat ne        näkyville komennolla ls -a
- Lisää tmp-päätteisiä tiedostoja hakemistoon ja varmista että Git jättää ne huomioimatta
  - Saat asian tarkastettua komennolla ```git status```
- Lisää myös hakemisto nimeltä __pycache__ ja hakemiston sisälle joku tiedosto. Varmista, että hakemisto sisältöineen ei mene versionhallinnan alaisuuteen
- Lisää ja commitoi .gitignore-tiedosto repositorioosi
- Seuraavat kohdat puhuvat Gitin staging-alueesta. Jos et tiedä mistä on kysymys, selvitä mistä kyse. Asia kyllä selviää ylle linkitetyistä ohjeista
- Tee muutos johonkin tiedostoon. Älä lisää tiedostoa “staging”-alueelle
  - Peru muutos (```git status```-komento antaa vihjeen miten tämä tapahtuu)
- Tee muutos ja lisää tiedosto “staging”-alueelle, varmista että muutosta ei enää näy tiedostossa
  - Peru muutos (```git status```-komento antaa vihjeen miten tämä tapahtuu), varmista että muutosta ei enää näy tiedostossa

**git add -p**

- Tutoriaaleissa ei valitettavasti käytetä git add-komennon hyödyllistä muotoa ```git add -p``` (katso https://gist.github.com/mattlewissf/9958704)
- Tee muutoksia muutamiin tiedostoihin ja lisää muutokset staging-alueelle komennon ```git add -p``` avulla
- Jos lisäät projektiin uusia tiedostoja, ei ```git add -p``` huomaa niitä, eli ne on lisättävä staging-alueelle erikseen
- Käytä jatkossa komentoa ```git add -p``` aina kun se on suinkin mahdollista!

Komennolla ```man git add``` saat lisätietoa optiosta ja mm. vastausvaihtoehtojen selitykset.
</details>

## 2. Tiedostojen lisääminen GitHubiin [versionhallinta]

<details>
<summary>Tehtävät</summary>

Tehtävässä 2 tehtiin GitHubiin "ohtuvarasto", joka liitettiin paikalliselle koneelle luotuun repositorioon "remote repositoryksi".

- “Pushaa” nämä GitHubissa olevaan etärepositorioon antamalla komento ```git push```
- Varmista selaimella, että lisätyt tiedostot menevät GitHubiin

</details>

## 3. Monta kloonia samasta repositoriosta [versionhallinta]

<details>
<summary>Tehtävät</summary>

Luodaan nyt harjoituksen vuoksi paikalliselle koneelle repositoriosta toinen klooni:

- Mene komentoriville ja esim. kotihakemistoosi (tai johonkin paikkaan, joka ei ole Git-repositorio)
- Anna komento ```git clone git@github.com:githubtunnus/repositorionNimi.git nimiKloonille```
  - githubtunnus ja repositorionNimi selviävät GitHubista repositoriosi tehtävän 2 toisen kuvan osoittamasta paikasta
  - nimiKloonille tulee olemaan kloonatun repositorion nimi, varmista että annat nimen, jonka nimistä tiedostoa tai hakemistoa ei jo ole kansiossa
- Mene kloonattuun repositorioon ja lisää sinne jotain tiedostoja. Committaa lopuksi
- “Pushaa” muutokset GitHubiin
- Varmista selaimella, että lisätyt tiedostot menevät GitHubiin

**Mene nyt tehtävässä 2 tehtyyn GitHub-repositorion klooniin.**

- Alkuperäinen paikallinen klooni ei ole enää ajantasalla, “pullaa” sinne muutokset komennolla ```git pull```
- Varmista että molempien paikallisten repositorioiden sisältö on nyt sama
- Lisää alkuperäiseen klooniin joitain tiedostoja ja pushaa ne GitHubiin
- Mene jälleen tässä tehtävässä tehtyyn klooniin ja pullaa

</details>

## 4. Repositorion siivous [versionhallinta]

<details>
<summary>Tehtävät</summary>

Valmistaudutaan seuraavaan tehtävään siivoamalla repositoriostamme ylimääräiset tiedostot

- Mene repositoriosi alkuperäiseen, tehtävässä 2 tekemääsi klooniin
  - Voit poistaa tehtävää 3 varten tekemäsi harjoituskloonin
- Poista repositorioistasi kaikki hakemistot sekä muut tiedostot paitsi .git, .gitignore ja README.md
- Committaa muutokset
  - Varmista komennolla git status että kaikki muutokset ovat versionhallinnassa, eli että Git ei ilmoita joidenkin tiedostojen olevan Changes not staged for commit
  - Joudut ehkä kertaamaan tehtävän 3 linkittämistä tutoriaaleista sitä miten tiedostojen poistaminen Gitistä tapahtuu
- Pushaa muutokset GitHubiin. Katso selaimella, että GitHubissa kaikki on ajan tasalla, eli että repositoriossa ei ole mitään muuta kuin tiedostot .gitignore ja README.md

**Haetaan sitten seuraavissa tehtävissä käytettävä koodi:**

- Hae osoitteesta https://github.com/ohjelmistotuotanto-jyu/tehtavat/raw/main/viikko1/varasto.zip löytyvä zipattu paketti
- Pura paketti sopivaan paikkaan
- Siirrä paketin sisällä olevat tiedostot kloonattuun repositorioon siten, että **paketissa olevat tiedostot ja hakemistot tulevat repositorion juureen**
- Lisää ja committoi zipistä puretut tavarat repositorioosi ja pushaa ne GitHubiin
- Katso vielä kerran selaimella, että GitHubissa kaikki on ajan tasalla

</details>

## 5. Poetry

<details>
<summary>Tehtävät</summary>

- Edellisessä tehtävässä lisättiin repositorioon Poetry-muodossa oleva varasto-projekti. Projekti sisältää erittäin yksinkertaisen varaston hallintaan soveltuvaa koodia. Varaston hallinnasta vastaa src/varasto.py-tiedossa määritelty luokka ```Varasto```. Luokkaa käyttää src/index.py-tiedossa määritelty funktio ```main```
- Tutki Poetry-muotoisen projektin hakemistorakennetta esim. antamalla komento ```tree``` projektin sisältävän hakemiston juuressa (tree ei ole Poetryyn liittyvä käsky vaan normaali shell-komento)
- Tarkastele projektin määrittelevän tiedoston pyproject.toml sisältöä
- Tarkastele juurihakemistossa olevan poetry.lock-tiedoston sisältöä

**Tee nyt seuraavat toimenpiteet.**

- Asenna varasto-projektin riippuvuudet suorittamalla sen juurihakemistossa komento ```poetry install```
- Käynnistä sovellus komennolla poetry run ```python3 src/index.py```
  - Run-komento suorittaa annetun komennon (tässä tapauksessa ```python3 src/index.py```) virtuaaliympäristössä
- Siirry virtuaaliympäristöön komennolla ```poetry shell```.
- Suorita komento ```python3 src/index.py```
- Poistu virtuaaliympäristöstä komennolla ```exit```
- Suorita testit komennolla ```poetry run pytest```

</details>

## 6. Unittest

<details>
<summary>Tehtävät</summary>

- Täydennä varasto-projektin testejä siten, että luokan ```Varasto``` testien haarautumakattavuudeksi (branch coverage) tulee 100%
- Testauksen rivikattavuuden saat selville coverage-työkalun avulla. Tutustu työkaluun lukemalla Coverage-ohje
- Ota työkalu projektissasi käyttöön asentamalla se projektin kehityksen aikaiseksi riippuvuudeksi komennolla:

```poetry add coverage --group dev```

Komennon muoto riippuu siitä kuinka uusi Poetryn versio käytössäsi on.

- Lisää projektin juurihakemistoon konfiguraatiotiedosto .coveragerc, jossa kerrotaan, mistä projektin tiedostoista testikattavuutta kerätään. Tiedoston sisällön tulee olla seuraava:

```
[run]
source = src
```

- Siirry virtuaaliympäristöön komennolla ```poetry shell```
  - Suorita komento ```coverage run --branch -m pytest```. Komento suorittaa testit ja kerää testien haarautumakattavuuden
  - Tämän jälkeen suorita komento ```coverage html```. Komento muodostaa raportin kerättyjen tietojen perusteella
- Projektin juurihakemistoon pitäisi ilmestyä hakemisto htmlcov. Voit tarkastella HTML-muotoista testikattavuusraporttia avamaalla selaimessa hakemiston htmlcov tiedoston index.html
  - Klikkaamalla raportista yksittäisen tiedoston nimeä näet, mitkä koodin suorituksen haarat on vielä testaamatta
- Lisää projektin .gitignore-tiedostoon tiedosto .coverage ja hakemisto htmlcov
- Kun luokan ```Varasto``` (tiedoston src/varasto.py) testien haarautumakattavuus (branch coverage) on 100%, pushaa tekemäsi muutokset GitHubiin

</details>
