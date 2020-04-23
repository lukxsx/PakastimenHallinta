# Toteutettavat käyttötapaukset
- [x] Käyttäjän luonti
* ```INSERT INTO kayttaja (tunnus, salasana) VALUES ('tunnus', 'salasana')```
- [x] Kirjautuminen
* ```SELECT kayttaja.id, kayttaja.tunnus, kayttaja.salasana FROM kayttaja WHERE kayttaja.tunnus = ? AND kayttaja.salasana = ? LIMIT ? OFFSET ?```
- [x] Kaapin lisääminen
* ```INSERT INTO kaappi (nimi) VALUES (?)```
- [x] Elintarviketyypin lisääminen
* ```INSERT INTO elintarvike (nimi, sailyvyys) VALUES (?, ?)```
- [x] Elintarviketyyppien listaus
* ```SELECT elintarvike.id, elintarvike.nimi, elintarvike.sailyvyys FROM elintarvike```
- [x] Elintarviketyypin tietojen päivittäminen (säilyvyys)
* ```UPDATE elintarvike SET sailyvyys=? WHERE elintarvike.id = ?```
- [x] Elintarvikkeen lisääminen kaappiin
* ```INSERT INTO elintarvike_kaapissa (taso, maara, laitettu_kaappiin, elintarvike_id, kaappi_id) VALUES (?, ?, ?, ?, ?)```
- [ ] Elintarvikkeiden poistaminen kaapista
- [x] Kaapissa olevien elintarvikkeiden listaus
* ```SELECT elintarvike_kaapissa.id, elintarvike_kaapissa.taso, elintarvike_kaapissa.maara, elintarvike_kaapissa.laitettu_kaappiin, elintarvike_kaapissa.elintarvike_id, elintarvike_kaapissa.kaappi_id FROM elintarvike_kaapissa```
* ```SELECT elintarvike.id, elintarvike.nimi, elintarvike.sailyvyys FROM elintarvike WHERE elintarvike.id = ?```
* ```SELECT kaappi.id, kaappi.nimi FROM kaappi WHERE kaappi.id = ?```
- [x] Vanhentuneiden elintarvikkeiden listaus
* ```SELECT elintarvike_kaapissa.id, elintarvike_kaapissa.taso, elintarvike_kaapissa.maara, elintarvike_kaapissa.laitettu_kaappiin, elintarvike_kaapissa.elintarvike_id, elintarvike_kaapissa.kaappi_id FROM elintarvike_kaapissa```
* ```SELECT elintarvike.id AS elintarvike_id, elintarvike.nimi AS elintarvike_nimi, elintarvike.sailyvyys AS elintarvike_sailyvyys FROM elintarvike WHERE elintarvike.id = ? LIMIT ? OFFSET ?```
* ```SELECT kaappi.id AS kaappi_id, kaappi.nimi AS kaappi_nimi FROM kaappi WHERE kaappi.id = ?```
