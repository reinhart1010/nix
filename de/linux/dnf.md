---
layout: page
title: linux/dnf (Deutsch)
description: "Paketmanagement Tool für RHEL, Fedora, und CentOS (ersetzt yum)."
content_hash: 50236a15681cb2b34cf09c3b3f397d7915627112
related_topics:
  - title: English version
    url: /en/linux/dnf.html
    icon: bi bi-globe
  - title: español version
    url: /es/linux/dnf.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/dnf.html
    icon: bi bi-globe
---
# dnf

Paketmanagement Tool für RHEL, Fedora, und CentOS (ersetzt yum).
Weitere Informationen: <https://dnf.readthedocs.io>.

- Aktualisiere alle Pakete auf die neueste Version:

`sudo dnf upgrade`

- Suche nach Paketen:

`dnf search `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">schlüsselwort</span>

- Zeige Daten über ein bestimmtes Paket an:

`dnf info `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">paket</span>

- Installiere ein neues Paket:

`sudo dnf install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">paket</span>

- Installiere ein neues Paket und antworte "ja" auf alle Fragen:

`sudo dnf -y install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">paket</span>

- Entferne ein Paket:

`sudo dnf remove `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">paket</span>

- Liste alle Pakete auf:

`dnf list --installed`

- Zeige welches Paket eine Datei besitzt:

`dnf provides `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/datei</span>
