---
layout: page
title: common/tig (Deutsch)
description: "Eine interaktive Kommandozeilenoberfläche für Git."
content_hash: eb6efa974d54fb14f44e32a023d9b1aa276014fd
last_modified_at: 2024-05-06
related_topics:
  - title: English version
    url: /en/common/tig.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/common/tig.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># tig

Eine interaktive Kommandozeilenoberfläche für Git.
Weitere Informationen: <https://jonas.github.io/tig/doc/manual.html>.

- Zeige die Commits des aktuellen Branches:

`tig`

- Zeige die Commits eines bestimmten Branches:

`tig `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">branch</span>

- Zeige die Commits von bestimmten Dateien oder Verzeichnissen:

`tig `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad1 pfad2 ...</span>

- Zeige die Unterschiede zwischen zwei Referenzen (wie z.B. Branches oder Tags):

`tig `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">base_ref</span>`..`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">compared_ref</span>

- Zeige die Commits von allen Branches und Stashes:

`tig --all`

- Zeige alle gespeicherten Stashes:

`tig stash`
