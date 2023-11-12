---
layout: page
title: linux/lastlog (Deutsch)
description: "Zeigt den letzten Login aller Benutzer oder eines bestimmten Benutzers an."
content_hash: 6d915fe117ea0802132e3943d0e7d75edd16bac9
last_modified_at: 2023-11-12
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

`lastlog --before `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">7</span>

- Zeige Datensätze jünger als 3 Tage an:

`lastlog --time `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">3</span>
