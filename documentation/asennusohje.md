# Asennusohje

## Paikallinen testiympäristö
Vaatimukset: Python 3 ja pip

Luo uusi Pythonin virtuaaliympäristö
```
python -m venv venv
```
Aktivoi virtuaaliympäristö
```
source venv/bin/activate
```
Asenna riippuvuudet
```
pip install -r requirements.txt
```
Sovellus voidaan käynnistää paikalliseen Flaskin testipalvelimeen komennolla
```
python run.py
```

## Heroku
Vaatii Herokun CLI-työkalun ja tunnukset.
```
heroku create <haluttu nimi>
```
Liitetään git-repositioon Heroku
```
git remote add heroku <herokusta saatu git-osoite>
```
Asetetaan Herokun HEROKU-ympäristömuuttujan arvoksi 1, että sovellus tietää
että käytetään nyt Herokua.
```
heroku config:set HEROKU=1
```
Luodaan sovellukselle PostgreSQL-tietokanta Herokuun
```
heroku addons:add heroku-postgresql:hobby-dev
```
Pushataan Herokuun
```
git push heroku master
```
