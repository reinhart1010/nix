---
layout: page
title: common/ed (Nederlands)
description: "De originele Unix tekst editor."
content_hash: 4b4836ee54558f53ded05f53ec7875b0be09e10c
last_modified_at: 2024-06-18
related_topics:
  - title: English version
    url: /en/common/ed.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/ed.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/ed.html
    icon: bi bi-globe
  - title: русский version
    url: /ru/common/ed.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/ed.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># ed

De originele Unix tekst editor.
Bekijk ook: `awk`, `sed`.
Meer informatie: <https://www.gnu.org/software/ed/manual/ed_manual.html>.

- Start een interactieve editor sessie met een leeg document:

`ed`

- Start een interactieve editor sessie met een leeg document en een specifieke prompt:

`ed --prompt='> '`

- Start een interactieve editor sessie met gebruiksvriendelijke foutmeldingen:

`ed --verbose`

- Start een interactieve editor sessie met een leeg document en zonder diagnostics, het aantal bytes en de '!' prompt:

`ed --quiet`

- Start een interactieve editor sessie zonder exit status change als het commando faalt:

`ed --loose-exit-status`

- Pas een specifiek bestand aan (dit toont het aantal bytes van het geladen bestand):

`ed `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand</span>

- Vervang een string met een specifieke vervanging voor alle regels:

`,s/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">reguliere_expressie</span>`/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">vervanging</span>`/g`
