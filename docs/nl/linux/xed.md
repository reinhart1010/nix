---
layout: page
title: linux/xed (Nederlands)
description: "Bewerk bestanden in de Cinnamon-desktopomgeving."
content_hash: c7c795212ec6c15369b516a6de527a36086955f3
last_modified_at: 2024-08-14
related_topics:
  - title: English version
    url: /en/linux/xed.html
    icon: bi bi-globe
tldri18n_status: 2
---
# xed

Bewerk bestanden in de Cinnamon-desktopomgeving.
Meer informatie: <https://github.com/linuxmint/xed>.

- Start de editor:

`xed`

- Open specifieke bestanden:

`xed `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand1 pad/naar/bestand2 ...</span>

- Open bestanden met een specifieke codering:

`xed --encoding `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">WINDOWS-1252</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand1 pad/naar/bestand2 ...</span>

- Toon alle ondersteunde coderingen:

`xed --list-encodings`

- Open een bestand en ga naar een specifieke regel:

`xed +`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">10</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand</span>
