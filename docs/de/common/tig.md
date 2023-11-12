---
layout: page
title: common/tig (Deutsch)
description: "Eine interaktive Kommandozeilenoberfläche für Git."
content_hash: e5afb72e0c62a60b0dfbf81bcc5d294ec6b120a3
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/tig.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/common/tig.html
    icon: bi bi-globe
tldri18n_status: 2
---
# tig

Eine interaktive Kommandozeilenoberfläche für Git.
Weitere Informationen: <https://github.com/jonas/tig>.

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
