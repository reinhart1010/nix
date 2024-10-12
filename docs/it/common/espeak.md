---
layout: page
title: common/espeak (italiano)
description: "Usa la sintesi vocale per parlare tramite il dispositivo audio di output predefinito."
content_hash: a7bc1beae6eeab47dcacd972c2006c9d09a94da9
last_modified_at: 2024-10-12
related_topics:
  - title: English version
    url: /en/common/espeak.html
    icon: bi bi-globe
tldri18n_status: 2
---
# espeak

Usa la sintesi vocale per parlare tramite il dispositivo audio di output predefinito.
Maggiori informazioni: <https://espeak.sourceforge.net>.

- Pronuncia una frase ad alta voce:

`espeak "Mi piace andare in bici."`

- Pronuncia il contenuto di un file ad alta voce:

`espeak -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_file</span>

- Salva l'output su un file audio WAV, invece che parlare direttamente:

`espeak -w `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_file.wav</span>` "È GNU più Linux."`

- Usa una voce differente:

`espeak -v `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">voce</span>
