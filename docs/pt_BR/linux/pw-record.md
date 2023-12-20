---
layout: page
title: linux/pw-record (português (Brasil))
description: "Grava arquivos de áudio através do pipewire."
content_hash: 53c2f7c23e74da7027a458c3ba2e524f252e3042
last_modified_at: 2023-12-20
related_topics:
  - title: English version
    url: /en/linux/pw-record.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/linux/pw-record.html
    icon: bi bi-globe
tldri18n_status: 2
---
# pw-record

Grava arquivos de áudio através do pipewire.
Atalho para pw-cat --record.
Mais informações: <https://fedoraproject.org/wiki/QA:Testcase_PipeWire_PipeWire_CLI>.

- Faz uma gravação usando o alvo padrão:

`pw-record `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/arquivo.wav</span>

- Faz uma gravação com um volume diferente:

`pw-record --volume=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">0.1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/arquivo.wav</span>

- Faz uma gravação usando uma taxa de amostragem diferente:

`pw-record --rate=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">6000</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/arquivo.wav</span>
