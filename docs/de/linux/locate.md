---
layout: page
title: linux/locate (Deutsch)
description: "Zum schnellen Finden von Dateinamen."
content_hash: 611545733342a962c0f445f9271951240011c140
related_topics:
  - title: English version
    url: /en/linux/locate.html
    icon: bi bi-globe
---
# locate

Zum schnellen Finden von Dateinamen.
Weitere Informationen: <https://manned.org/locate>.

- Suche nach Dateien in der Datenbank. Hinweis: Die Datenbank wird periodisch aktualisiert (für gewöhnlich täglich oder wöchentlich):

`locate `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">muster</span>

- Suche nach Dateien mit dem exakten Dateinamen. (Ein Muster ohne Platzhalterzeichen wird als `*muster*` interpretiert):

`locate */`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">dateiname</span>

- Aktualisiere die Datenbank. Dies ist nötig, falls kürzlich hinzugefügte Dateien gefunden werden sollen:

`sudo updatedb`
