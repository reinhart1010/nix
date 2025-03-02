---
layout: page
title: common/alacritty (Nederlands)
description: "Cross-platform, GPU-versnelde terminalemulator."
content_hash: d57148006399a9f5684b5fafc64424ffa52505a3
last_modified_at: 2025-03-02
related_topics:
  - title: Deutsch version
    url: /de/common/alacritty.html
    icon: bi bi-globe
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

Cross-platform, GPU-versnelde terminalemulator.
Meer informatie: <https://github.com/alacritty/alacritty>.

- Open een nieuw Alacritty-venster:

`alacritty`

- Start de Alacritty daemon (zonder een venster te maken):

`alacritty --daemon`

- Maak een nieuw venster met behulp van het reeds lopende Alacritty proces:

`alacritty msg create-window`

- Uitvoeren in een specifieke map:

`alacritty --working-directory `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/map</span>

- Vo[e]r een commando uit in een nieuw Alacritty-venster:

`alacritty -e `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">commando</span>

- Geef een alternatief configuratiebestand op (standaard ingesteld op `$XDG_CONFIG_HOME/alacritty/alacritty.toml`):

`alacritty --config-file `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/config.toml</span>

- Uitvoeren met live config reload ingeschakeld (kan ook standaard worden ingeschakeld in `alacritty.toml`):

`alacritty --live-config-reload --config-file `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/config.toml</span>
