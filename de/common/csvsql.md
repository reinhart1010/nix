---
layout: page
title: common/csvsql (Deutsch)
description: "Generiere SQL-Anweisungen für eine CSV-Datei oder führe diese Anweisungen direkt in einer Datenbank aus."
content_hash: 195e5fad225df3f4ec2721c77cd289fbd158cefe
related_topics:
  - title: English version
    url: /en/common/csvsql.html
    icon: bi bi-globe
---
# csvsql

Generiere SQL-Anweisungen für eine CSV-Datei oder führe diese Anweisungen direkt in einer Datenbank aus.
Teil von csvkit.
Weitere Informationen: <https://csvkit.readthedocs.io/en/latest/scripts/csvsql.html>.

- Generiere eine `CREATE TABLE`-SQL-Anweisung für eine CSV-Datei:

`csvsql `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/datei.csv</span>

- Importiere eine CSV-Datei in eine SQL-Datenbank:

`csvsql --insert --db "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">mysql://benutzer:passwort@host/datenbank</span>`" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/datei.csv</span>

- Führe eine SQL-Abfrage auf einer CSV-Datei aus:

`csvsql --query "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">select * from 'datei'</span>`" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">datei.csv</span>
