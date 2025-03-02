---
layout: page
title: linux/pw-record (português (Brasil))
description: "Grava arquivos de áudio através do PipeWire."
content_hash: 43bc3ff12fefda332e5ad9dccbe78c1d8399c6bf
last_modified_at: 2025-03-02
related_topics:
  - title: English version
    url: /en/linux/pw-record.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/linux/pw-record.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/linux/pw-record.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/linux/pw-record.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># pw-record

Grava arquivos de áudio através do PipeWire.
Atalho para pw-cat --record.
Mais informações: <https://fedoraproject.org/wiki/QA:Testcase_PipeWire_PipeWire_CLI>.

- Faz uma gravação usando o alvo padrão:

`pw-record `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/arquivo.wav</span>

- Faz uma gravação com um volume diferente:

`pw-record --volume=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">0.1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/arquivo.wav</span>

- Faz uma gravação usando uma taxa de amostragem diferente:

`pw-record --rate=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">6000</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/arquivo.wav</span>
