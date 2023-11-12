---
layout: page
title: common/bat (italiano)
description: "Stampa e concatena file."
content_hash: 5ec9880edd746bb5b5738ebc4fee33a4eea2bf63
last_modified_at: 2023-11-12
related_topics:
  - title: Deutsch version
    url: /de/common/bat.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/bat.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/bat.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/bat.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/bat.html
    icon: bi bi-globe
  - title: 日本語 version
    url: /ja/common/bat.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/bat.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/common/bat.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/bat.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/bat.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/bat.html
    icon: bi bi-globe
tldri18n_status: 2
---
# bat

Stampa e concatena file.
Un clone di `cat` con syntax highlighting e integrazione Git.
Maggiori informazioni: <https://github.com/sharkdp/bat>.

- Stampa i contenuti di un file su standard output:

`bat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file</span>

- Concatena diversi file in un unico file:

`bat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file2</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file_finale</span>

- Aggiungi il contenuto di diversi file alla fine di un file:

`bat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file2</span>` >> `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file_finale</span>

- Numera tutte le linee stampate:

`bat -n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file</span>

- Evidenzia la sintassi di un file JSON:

`bat --language json `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file.json</span>

- Mostra tutti i linguaggi supportati:

`bat --list-languages`
