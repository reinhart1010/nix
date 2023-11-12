---
layout: page
title: common/asdf (Deutsch)
description: "Verwalte installierte Versionen von verschiedenen Paketen."
content_hash: ba081a598538ed66ecad0f3bc4f8936428330b13
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/asdf.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/asdf.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/asdf.html
    icon: bi bi-globe
  - title: 日本語 version
    url: /ja/common/asdf.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/asdf.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/asdf.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/asdf.html
    icon: bi bi-globe
tldri18n_status: 2
---
# asdf

Verwalte installierte Versionen von verschiedenen Paketen.
Plugins (z.B. asdf-node) werden für spezifische Pakete verwendet.
Weitere Informationen: <https://asdf-vm.com>.

- Liste alle verfügbaren Plugins auf:

`asdf plugin list all`

- Installiere ein neues Plugin:

`asdf plugin add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">name</span>

- Liste alle verfügbaren Versionen für ein Paket auf:

`asdf list all `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">name</span>

- Installiere eine spezifische Version eines Pakets:

`asdf install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">name</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">version</span>

- Lege die globale Version für ein Paket fest:

`asdf global `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">name</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">version</span>

- Lege die lokale Version für ein Paket fest:

`asdf local `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">name</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">version</span>
