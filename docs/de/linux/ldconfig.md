---
layout: page
title: linux/ldconfig (Deutsch)
description: "Symbolische Verknüpfungen und Zwischenspeicher für Abhängigkeiten von gemeinsam genutzten Bibliotheken konfigurieren."
content_hash: 3ef2a842168d28fca6a9a1bbae997445f4b9c351
related_topics:
  - title: English version
    url: /en/linux/ldconfig.html
    icon: bi bi-globe
---
# ldconfig

Symbolische Verknüpfungen und Zwischenspeicher für Abhängigkeiten von gemeinsam genutzten Bibliotheken konfigurieren.
Weitere Informationen: <https://manned.org/ldconfig>.

- Aktualisiere symbolische Verknüpfungen und erstelle den Zwischenspeicher neu (wird normalerweise ausgeführt, wenn eine neue Bibliothek installiert wird):

`sudo ldconfig`

- Aktualisiere die symbolischen Verknüpfungen für ein bestimmtes Verzeichnis:

`sudo ldconfig -n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/verzeichnis</span>

- Gib die Bibliotheken im Zwischenspeicher aus und prüfe ob eine bestimmte Bibliothek vorhanden ist:

`ldconfig -p | grep `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">bibliotheksname</span>
