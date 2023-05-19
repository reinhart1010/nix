---
layout: page
title: windows/clip (italiano)
description: "Copia il contenuto di input negli Appunti di Windows."
content_hash: e6f963772c9a6043bf3043c4a7ef4bf0c4e1f7e3
last_modified_at: 2023-05-19
related_topics:
  - title: Deutsch version
    url: /de/windows/clip.html
    icon: bi bi-globe
  - title: English version
    url: /en/windows/clip.html
    icon: bi bi-globe
  - title: 日本語 version
    url: /ja/windows/clip.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/windows/clip.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/windows/clip.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># clip

Copia il contenuto di input negli Appunti di Windows.
Maggiori informazioni: <https://learn.microsoft.com/windows-server/administration/windows-commands/clip>.

- Manda l'output della riga di comando negli Appunti di Windows:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">dir</span>` | clip`

- Copia i contenuti di un file negli appunti di Windows:

`clip < `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso\per\file.ext</span>

- Copia il testo con una nuova riga finale negli appunti di Windows:

`echo `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">testo_generico</span>` | clip`

- Copia il testo senza una nuova riga finale negli appunti di Windows:

`echo | set /p="testo_generico" | clip`
