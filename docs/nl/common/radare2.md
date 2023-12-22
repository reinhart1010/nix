---
layout: page
title: common/radare2 (Nederlands)
description: "Een set van reverse engineering tools."
content_hash: e9f79deb2f471aba5cdc4a299be41506c4bee89d
last_modified_at: 2023-12-22
related_topics:
  - title: English version
    url: /en/common/radare2.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/radare2.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># radare2

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
