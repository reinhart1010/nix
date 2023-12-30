---
layout: page
title: linux/lastlog (Deutsch)
description: "Zeigt den letzten Login aller Benutzer oder eines bestimmten Benutzers an."
content_hash: 6b9b947da1d7f9d7f54251f776048267284a6ad5
last_modified_at: 2023-12-30
related_topics:
  - title: English version
    url: /en/linux/lastlog.html
    icon: bi bi-globe
tldri18n_status: 2
---
# lastlog

Zeigt den letzten Login aller Benutzer oder eines bestimmten Benutzers an.
Weitere Informationen: <https://manned.org/lastlog>.

- Zeige den letzten Login aller Benutzer an:

`lastlog`

- Zeige den lastlog Datensatz des angegebenen Benutzers an:

`lastlog --user `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">benutzername</span>

- Zeige Datensätze älter als 7 Tage an:

`lastlog --before 7`

- Zeige Datensätze jünger als 3 Tage an:

`lastlog --time 3`
