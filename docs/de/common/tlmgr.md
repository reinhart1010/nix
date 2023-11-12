---
layout: page
title: common/tlmgr (Deutsch)
description: "Verwalte Packages und Konfigurationen einer existierenden TeX Live Installation."
content_hash: 87c05433f2fa91c6ee4df1a53616167b5cbb60d1
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/tlmgr.html
    icon: bi bi-globe
tldri18n_status: 2
---
# tlmgr

Verwalte Packages und Konfigurationen einer existierenden TeX Live Installation.
Manche Unterbefehle wie `tlmgr paper` sind separat dokumentiert.
Weitere Informationen: <https://www.tug.org/texlive/tlmgr.html>.

- Installiere ein Package und seine Abhängigkeiten:

`tlmgr install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package</span>

- Entferne ein Package und seine Abhängigkeiten:

`tlmgr remove `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package</span>

- Zeige Informationen über ein Package an:

`tlmgr info `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package</span>

- Aktualisiere alle Packages:

`tlmgr update --all`

- Zeige mögliche Aktualisierungen an, ohne Änderungen vorzunehmen:

`tlmgr update --list`

- Starte die grafische Oberfläche von tlmgr:

`tlmgr gui`

- Liste alle Tex Live Konfigurationen auf:

`tlmgr conf`
