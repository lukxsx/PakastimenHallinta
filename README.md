# Pakastimen ja jääkaapin sisällön hallintasovellus
 Sovelluksella voidaan pitää kirjaa pakastimen ja jääkaapin sisällöistä. Pakastimeen ja jääkaappiin voi unohtua ruokaa pitkäksikin aikaa. Tämä sovellus pitää kirjaa kaappeihin asetetuista elintarvikkeista.

Sovellukseen voidaan lisätä kaappeja (esim. pakastin, jääkaappi yms). Sovellukseen voidaan lisätä eri elintarviketyyppejä, ja niitä voidaan sitten lisätä eri kaappeihin. Ruokia lisättäessä niille valitaan päiväys, joka kertoo milloin ne on laitettu kaappiin. Ohjelmassa voidaan sen jälkeen näyttää listauksia kaappien sisällöistä ja näyttää esimerkiksi vanhentuneet ruoat. 
## Heroku
[Sovellus Herokussa](https://pakastimenhallinta.herokuapp.com/)

Tunnukset: _testi_, salasana: _salasana_

_Huomasin vasta palautuksen jälkeen, että toinen yhteenvetokyselyistä ei jostain syystä toimi PostgreSQL:llä (jokin alikyselyihin liittyvä juttu) ja aiheuttaa virheen Herokussa käytettäessä. Se toimii tällä hetkellä vain paikallisesti SQLitellä. Yritän selvittää asiaa._

## Dokumentaatio

* [Asennusohje](documentation/asennusohje.md)
* [Käyttöohje](documentation/kayttoohje.md)
* [Käyttötapaukset](documentation/kayttotapaukset.md)
* [Tietokannan kuvaus](documentation/tietokanta.md)
