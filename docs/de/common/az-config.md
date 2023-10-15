---
layout: page
title: common/az-config (Deutsch)
description: "Verwalten der Azure CLI-Konfiguration."
content_hash: 735120d2cb3f3f2854339550e5b78f78a19ff271
last_modified_at: 2023-10-15
related_topics:
  - title: English version
    url: /en/common/az-config.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/az-config.html
    icon: bi bi-globe
---
# az config

Verwalten der Azure CLI-Konfiguration.
Teil von `azure-cli` (auch bekannt als `az`).
Weitere Informationen: <https://learn.microsoft.com/cli/azure/config>.

- Rufe alle Konfigurationen ab:

`az config get`

- Rufe alle Konfigurationen in einer Sektion ab:

`az config get `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">sektionsname</span>

- Setze eine Konfiguration:

`az config set `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">konfigurationsname</span>`=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">wert</span>

- Hebe eine Konfiguration auf:

`az config unset `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">konfigurationsname</span>
