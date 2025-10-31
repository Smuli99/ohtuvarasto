# Ohjelmistotuotanto, TEKA2500
[![GHA workflow badge](https://github.com/Smuli99/ohtuvarasto/workflows/CI/badge.svg)](https://github.com/Smuli99/ohtuvarasto/actions)

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
