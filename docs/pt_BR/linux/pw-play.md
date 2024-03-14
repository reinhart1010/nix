---
layout: page
title: linux/pw-play (português (Brasil))
description: "Grava arquivos de áudio através do PipeWire."
content_hash: 4b509f1cafcc503eb1dd74072d0743c06264cd80
last_modified_at: 2024-03-14
related_topics:
  - title: English version
    url: /en/linux/pw-play.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/linux/pw-play.html
    icon: bi bi-globe
tldri18n_status: 2
---
# pw-play

Grava arquivos de áudio através do PipeWire.
Atalho para pw-cat --playback.
Mais informações: <https://fedoraproject.org/wiki/QA:Testcase_PipeWire_PipeWire_CLI>.

- Toca um som em formato WAV no alvo padrão:

`pw-play `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/arquivo.wav</span>

- Toca um arquivo em formato WAV com um volume específico:

`pw-play --volume=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">0.1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/arquivo.wav</span>
