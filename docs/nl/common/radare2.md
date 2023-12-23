---
layout: page
title: common/radare2 (Nederlands)
description: "Een set van reverse engineering tools."
content_hash: e9f79deb2f471aba5cdc4a299be41506c4bee89d
last_modified_at: 2023-12-23
related_topics:
  - title: English version
    url: /en/common/radare2.html
    icon: bi bi-globe
tldri18n_status: 2
---
# radare2

Een set van reverse engineering tools.
Meer informatie: <https://www.radare.org/r/docs.html>.

- Open een schrijfbaar bestand zonder het parsen van de bestandsformaat headers:

`radare2 -nw `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/binary</span>

- Debug een programma:

`radare2 -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/binary</span>

- Voer een script uit voordat de interactieve CLI start:

`radare2 -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/script.r2</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/binary</span>

- Toon help tekst voor ieder commando in de interactieve CLI:

`> `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">radare2_commando</span>`?`

- Voer een shell commando uit vanuit de interactieve CLI:

`> !`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">shell_commando</span>

- Dump raw bytes van het huidige block naar een bestand:

`> pr > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand.bin</span>
