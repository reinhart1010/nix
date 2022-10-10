---
layout: page
title: windows/color (svenska)
description: "Används för att ändra bakgrunds och textfärgen i kommandotolken."
content_hash: 3bff840445a1616f154e141feff73a4e2cc9e223
related_topics:
  - title: català version
    url: /ca/windows/color.html
    icon: bi bi-globe
  - title: Deutsch version
    url: /de/windows/color.html
    icon: bi bi-globe
  - title: English version
    url: /en/windows/color.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/windows/color.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># color

Används för att ändra bakgrunds och textfärgen i kommandotolken.
Mer information: <https://learn.microsoft.com/windows-server/administration/windows-commands/color>.

- Återställer färgerna till orginal (svart bakgrund, vit text):

`color`

- För att se detaljerad information och de olika färgalternativen:

`color /?`

- Ställ in vilken färg bakgrunden och texten ska ha med hjälp av hexadecimala tal (`1-9,a-f`):

`color `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">tal_textfärg</span><span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">tal_bakgrundsfärg</span>
