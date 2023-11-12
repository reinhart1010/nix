---
layout: page
title: osx/csshx (português (Brasil))
description: "Ferramenta de Cluster SSH para macOS."
content_hash: c315e16c42b0f4b467f83c77d2c2f9cf1d63a9fc
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/osx/csshx.html
    icon: bi bi-globe
  - title: español version
    url: /es/osx/csshx.html
    icon: bi bi-globe
tldri18n_status: 2
---
# csshX

Ferramenta de Cluster SSH para macOS.
Mais informações: <https://github.com/brockgr/csshx>.

- Conecta a vários hosts:

`csshX `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nomedohost1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nomedohost2</span>

- Conecta a vários hosts com uma determinada chave SSH:

`csshX `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">user@nomedohost1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">user@nomedohost2</span>` --ssh_args "-i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/ssh_key.pem</span>`"`

- Conecta a um cluster predefinido em `/etc/clusters`:

`csshX cluster1`
