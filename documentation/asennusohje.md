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
Vaatii Herokun CLI-työkalun ja sovelluksen git-reposition
```
heroku create _haluttu nimi tähän_
```
Liitetään git-repositioon Heroku
```
git remote add heroku _herokusta saatu git-osoite_
```
Pushataan Herokuun
```
git push heroku master
```
