# Toteutettavat käyttötapaukset
- [x] Käyttäjän luonti
    * ```INSERT INTO kayttaja (tunnus, hash) VALUES (?, ?)```
- [x] Kirjautuminen
    * Käyttäjä haetaan nimen perusteella ```SELECT kayttaja.id, kayttaja.tunnus, kayttaja.hash FROM kayttaja WHERE 
kayttaja.tunnus = ?```
    * Annetun salasanan hashia verrataan tietokantaan tallennetun käyttäjän hashiin ```SELECT kayttaja.id, kayttaja.tunnus, 
kayttaja.hash FROM kayttaja WHERE kayttaja.id = ?```
- [x] Kaapin lisääminen
    * ```INSERT INTO kaappi (nimi, kayttaja_id) VALUES (?, ?)```
- [x] Kaapin poistaminen
    * Haetaan poistettava kaappi ```SELECT kaappi.id, kaappi.nimi, kaappi.kayttaja_id FROM kaappi WHERE kaappi.id = ?```
    * Tarkistetaan, onko kaapissa elintarvikkeita ```SELECT elintarvike_kaapissa.id, elintarvike_kaapissa.taso, elintarvike_kaapissa.maara, elintarvike_kaapissa.laitettu_kaappiin, elintarvike_kaapissa.elintarvike_id, elintarvike_kaapissa.kaappi_id, elintarvike_kaapissa.kayttaja_id FROM elintarvike_kaapissa WHERE elintarvike_kaapissa.kaappi_id = ?
 LIMIT ? OFFSET ?```
    * Poistetaan kaappi ```DELETE FROM kaappi WHERE kaappi.id = ?```
- [x] Kaapin uudelleennimeäminen
    * Haetaan uudelleennimettävä kaappi ```SELECT kaappi.id AS kaappi_id, kaappi.nimi, kaappi.kayttaja_id FROM kaappi WHERE kaappi.id = ?```
    * Nimetään kaappi uudelleen ```UPDATE kaappi SET nimi=? WHERE kaappi.id = ?```
- [x] Elintarviketyypin lisääminen
    * ```INSERT INTO elintarvike (nimi, sailyvyys, kayttaja_id) VALUES (?, ?, ?)```
- [x] Elintarviketyyppien listaus
    * ```SELECT elintarvike.id, elintarvike.nimi, elintarvike.sailyvyys, elintarvike.kayttaja_id FROM elintarvike WHERE elintarvike.kayttaja_id = ?```
- [x] Elintarviketyypin tietojen päivittäminen (säilyvyys)
    * haetaan päivitettävä elintarvike ```SELECT elintarvike.id, elintarvike.nimi, elintarvike.sailyvyys, elintarvike.kayttaja_id FROM elintarvike
WHERE elintarvike.id = ?```
    * päivitetään säilyvyys ```UPDATE elintarvike SET sailyvyys=? WHERE elintarvike.id = ?```
- [x] Elintarviketyypin poistaminen
    * haetaan poistettava elintarviketyyppi ```SELECT elintarvike.id, elintarvike.nimi, elintarvike.sailyvyys, elintarvike.kayttaja_id FROM elintarvike
WHERE elintarvike.id = ?```
    * Tarkistetaan, voidaanko elintarviketyyppi poistaa ```SELECT elintarvike_kaapissa.id, elintarvike_kaapissa.taso, elintarvike_kaapissa.maara, elintarvike_kaapissa.laitettu_kaappiin, elintarvike_kaapissa.elintarvike_id, elintarvike_kaapissa.kaappi_id, elintarvike_kaapissa.kayttaja_id FROM elintarvike_kaapissa
WHERE elintarvike_kaapissa.elintarvike_id = ?
 LIMIT ? OFFSET ?```
    * poistetaan elintarviketyyppi ```DELETE FROM elintarvike WHERE elintarvike.id = ?```
- [x] Elintarvikkeen lisääminen kaappiin
    * ```INSERT INTO elintarvike_kaapissa (taso, maara, laitettu_kaappiin, elintarvike_id, kaappi_id, kayttaja_id) VALUES (?, ?, ?, ?, ?, ?)```
- [x] Elintarvikkeiden poistaminen kaapista
    * haetaan poistettava elintarvike ```SELECT elintarvike_kaapissa.id, elintarvike_kaapissa.taso, elintarvike_kaapissa.maara, elintarvike_kaapissa.laitettu_kaappiin, elintarvike_kaapissa.elintarvike_id, elintarvike_kaapissa.kaappi_id, elintarvike_kaapissa.kayttaja_id FROM elintarvike_kaapissa
WHERE elintarvike_kaapissa.id = ?```
    * poistetaan elintarvike kaapista ```DELETE FROM elintarvike_kaapissa WHERE elintarvike_kaapissa.id = ?```
- [x] Kaapissa olevien elintarvikkeiden listaus
    * Haetaan elintarvikkeet kaapissa ```SELECT elintarvike_kaapissa.id, elintarvike_kaapissa.taso, elintarvike_kaapissa.maara, elintarvike_kaapissa.laitettu_kaappiin, elintarvike_kaapissa.elintarvike_id, elintarvike_kaapissa.kaappi_id, elintarvike_kaapissa.kayttaja_id FROM elintarvike_kaapissa
WHERE elintarvike_kaapissa.kayttaja_id = ?```
    * Haetaan elintarviketyypin nimet listausta varten ```SELECT elintarvike.id, elintarvike.nimi, elintarvike.sailyvyys, elintarvike.kayttaja_id FROM elintarvike WHERE elintarvike.id = ?```
    * Haetaan kaappien nimet listausta varten ```SELECT kaappi.id, kaappi.nimi, kaappi.kayttaja_id FROM kaappi WHERE kaappi.id = ?```
- [x] Vanhentuneiden elintarvikkeiden listaus
    * Haetaan elintarvikkeet kaapissa ```SELECT elintarvike_kaapissa.id, elintarvike_kaapissa.taso, elintarvike_kaapissa.maara, elintarvike_kaapissa.laitettu_kaappiin, elintarvike_kaapissa.elintarvike_id, elintarvike_kaapissa.kaappi_id, elintarvike_kaapissa.kayttaja_id FROM elintarvike_kaapissa WHERE elintarvike_kaapissa.kayttaja_id = ?```
    * Haetaan elintarviketyypin nimet listausta varten ```SELECT elintarvike.id, elintarvike.nimi, elintarvike.sailyvyys, elintarvike.kayttaja_id FROM elintarvike WHERE elintarvike.id = ? LIMIT ? OFFSET ?```
    * Haetaan kaappien nimet listausta varten ```SELECT kaappi.id, kaappi.nimi, kaappi.kayttaja_id FROM kaappi WHERE kaappi.id = ?```
- [x] Yhteenvetokysely, elintarvikkeiden määrä kaapissa
    * ```SELECT kaappi.nimi, SUM(elintarvike_kaapissa.maara) FROM elintarvike_kaapissa LEFT JOIN kaappi ON elintarvike_kaapissa.kaappi_id=kaappi.id WHERE kaappi.kayttaja_id = ? GROUP BY kaappi.nimi```
- [x] Yhteenvetokysely, elintarviketyyppien määrä kaapeissa
    * ```SELECT E.nimi, (SELECT SUM(maara) FROM elintarvike_kaapissa WHERE elintarvike_id = E.id AND kayttaja_id = ?) laskuri FROM elintarvike E, elintarvike_kaapissa GROUP BY E.nimi```
- [x] Yhteenvetokysely, tyhjät kaapit
    * ```SELECT COUNT(id) FROM kaappi WHERE id NOT IN (SELECT kaappi_id FROM elintarvike_kaapissa) AND kaappi.kayttaja_id = ?```