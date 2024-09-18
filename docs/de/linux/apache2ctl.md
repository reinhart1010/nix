---
layout: page
title: linux/apache2ctl (Deutsch)
description: "Das CLI Tool um den Apache HTTP Web Server zu administrieren."
content_hash: 84141356fa014cb88442b444f02f9b8cd8340116
last_modified_at: 2024-09-18
related_topics:
  - title: English version
    url: /en/linux/apache2ctl.html
    icon: bi bi-globe
  - title: français version
    url: /fr/linux/apache2ctl.html
    icon: bi bi-globe
  - title: हिन्दी version
    url: /hi/linux/apache2ctl.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/apache2ctl.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/apache2ctl.html
    icon: bi bi-globe
tldri18n_status: 2
---
# apache2ctl

Das CLI Tool um den Apache HTTP Web Server zu administrieren.
Dieser Befehl wird mit Debian-basierten Betriebssystemen geliefert, für RHEL siehe `httpd`.
Weitere Informationen: <https://manned.org/apache2ctl.8>.

- Starte den Apache daemon. Gibt einen Fehler aus, wenn er bereits läuft:

`sudo apache2ctl start`

- Stoppe den Apache Daemon:

`sudo apache2ctl stop`

- Starte den Apache Daemon neu:

`sudo apache2ctl restart`

- Überprüfe die Syntax einer Konfigurationsdatei:

`sudo apache2ctl -t`

- Liste alle geladenen Module auf:

`sudo apache2ctl -M`
