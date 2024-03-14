---
layout: page
title: linux/pw-cat (português (Brasil))
description: "Toca e grava arquivos de áudio através do PipeWire."
content_hash: 3b763646896ece3dc799a59c2b5088d06cb7352a
last_modified_at: 2024-03-14
related_topics:
  - title: English version
    url: /en/linux/pw-cat.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/linux/pw-cat.html
    icon: bi bi-globe
tldri18n_status: 2
---
# pw-cat

Toca e grava arquivos de áudio através do PipeWire.
Mais informações: <https://fedoraproject.org/wiki/QA:Testcase_PipeWire_PipeWire_CLI>.

- Toca um arquivo WAV no alvo padrão:

`pw-cat --playback `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/arquivo.wav</span>

- Toca um arquivo WAV com uma qualidade de reamostragem específica (4 por padrão):

`pw-cat --quality `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">0..15</span>` --playback `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/arquivo.wav</span>

- Faz uma gravação com o volume em 125%:

`pw-cat --record --volume `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1.25</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/arquivo.wav</span>

- Faz uma gravação com uma taxa de amostragem diferente:

`pw-cat --record --rate `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">6000</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/arquivo.wav</span>
