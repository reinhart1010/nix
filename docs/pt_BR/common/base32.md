---
layout: page
title: common/base32 (português (Brasil))
description: "Codifica ou decodifica um arquivo ou a entrada padrão (stdin) de/para Base32, para a saída padrão (stdout)."
content_hash: d04c97d7b28eb958eef21185f642be2af251334c
related_topics:
  - title: English version
    url: /en/common/base32.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/base32.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/base32.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/base32.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/common/base32.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/base32.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/base32.html
    icon: bi bi-globe
---
# base32

Codifica ou decodifica um arquivo ou a entrada padrão (stdin) de/para Base32, para a saída padrão (stdout).
Mais informações: <https://www.gnu.org/software/coreutils/base32>.

- Codifica um arquivo:

`base32 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_do_arquivo</span>

- Decodifica um arquivo:

`base32 --decode `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_do_arquivo</span>

- Codifica a partir de stdin:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">algum_comando</span>` | base32`

- Decodifica a partir de stdin:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">algum_comando</span>` | base32 --decode`
