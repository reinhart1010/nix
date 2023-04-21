---
layout: page
title: windows/attrib (italiano)
description: "Mostra o cambia gli attributi di file e cartelle."
content_hash: 0c3c7a820f1392a526e1dca79d103c9c67be2549
last_modified_at: 2023-04-21
related_topics:
  - title: English version
    url: /en/windows/attrib.html
    icon: bi bi-globe
  - title: 日本語 version
    url: /ja/windows/attrib.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/windows/attrib.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/windows/attrib.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># attrib

Mostra o cambia gli attributi di file e cartelle.
Maggiori informazioni: <https://learn.microsoft.com/windows-server/administration/windows-commands/attrib>.

- Mostra tutti gli attributi dei file in una cartella:

`attrib`

- Mostra tutti gli attributi dei file in una cartella specifica:

`attrib `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso\della\cartella</span>

- Mostra tutti gli attributi dei file e delle cartelle nella cartella corrente:

`attrib /d`

- Mostra tutti gli attributi dei file in una cartella e le sue sotto-cartelle:

`attrib /s`

- Aggiungi l'attributo `[r]ead-only` o `[a]rchive` o `[s]ystem` o `[h]idden` o `not content [i]ndexed` a file o cartelle:

`attrib +`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">r|a|s|h|i</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso\del\file_o_cartella1 percorso\del\file_o_cartella2 ...</span>

- Rimuovi un attributo specifico da un file o una cartella:

`attrib -`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">r|a|s|h|i</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso\del\file_o_cartella1 percorso\del\file_o_cartella2 ...</span>
