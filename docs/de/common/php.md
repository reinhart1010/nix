---
layout: page
title: common/php (Deutsch)
description: "PHP Befehlszeilenschnittstelle."
content_hash: db09330334c79ba282ea292de35e343ecea4bbf0
last_modified_at: 2023-10-09
related_topics:
  - title: English version
    url: /en/common/php.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/common/php.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># php

PHP Befehlszeilenschnittstelle.
Mehr Informationen: <https://php.net>.

- Analysiere ein PHP-Skript und führe es aus:

`php `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/datei</span>

- Überprüfe die Syntax eines PHP-Skripts:

`php -l `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/datei</span>

- Führen PHP interaktiv aus:

`php -a`

- Führe einen PHP-Befehl aus:

`php -r "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">befehl</span>`"`

- Starte den in PHP integrierten Webserver im aktuellen Verzeichnis:

`php -S `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">host:port</span>

- Zeige eine Liste der installierten PHP-Erweiterungen:

`php -m`

- Zeige Informationen zur aktuellen PHP-Konfiguration an:

`php -i`

- Zeige Informationen zu einer bestimmten Funktion an:

`php --rf `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">funktionsname</span>
