---
layout: page
title: common/alacritty (Deutsch)
description: "Plattformübergreifender, GPU-beschleunigter Terminalemulator."
content_hash: 66c3c64d30d07921506ab199c93b30b735c08cea
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/alacritty.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/alacritty.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/alacritty.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/alacritty.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/alacritty.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/alacritty.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/alacritty.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/alacritty.html
    icon: bi bi-globe
  - title: português (Portugal) version
    url: /pt_PT/common/alacritty.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/alacritty.html
    icon: bi bi-globe
tldri18n_status: 2
---
# alacritty

Plattformübergreifender, GPU-beschleunigter Terminalemulator.
Weitere Informationen: <https://github.com/alacritty/alacritty>.

- Öffne ein neues Alacritty-Fenster:

`alacritty`

- Starte Alacritty in einem bestimmten Arbeitsverzeichnis:

`alacritty --working-directory `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/verzeichnis</span>

- Führe einen Befehl in einem neuen Alacritty-Fenster aus:

`alacritty -e `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">befehl</span>

- Gib eine alternative Konfigurations-Datei an (ist standardmäßig `$XDG_CONFIG_HOME/alacritty/alacritty.yml`):

`alacritty --config-file `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/konfiguration.yml</span>

- Starte mit aktiviertem Live-Konfigurations-Neuladen (kann auch standardmäßig in `alacritty.yml` eingestellt werden):

`alacritty --live-config-reload --config-file `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/konfiguration.yml</span>
