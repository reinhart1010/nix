---
layout: page
title: common/az-config (Deutsch)
description: "Verwalten der Azure CLI-Konfiguration."
content_hash: 8b6894c7c676f12b6a3a7ddc30a82caf32e9d4ac
related_topics:
  - title: English version
    url: /en/common/az-config.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># az config

Verwalten der Azure CLI-Konfiguration.
Teil von `azure-cli`.
Weitere Informationen: <https://learn.microsoft.com/cli/azure/config>.

- Rufe alle Konfigurationen ab:

`az config get`

- Rufe alle Konfigurationen in einer Sektion ab:

`az config get `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">sektionsname</span>

- Setze eine Konfiguration:

`az config set `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">konfigurationsname</span>`=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">wert</span>

- Hebe eine Konfiguration auf:

`az config unset `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">konfigurationsname</span>
