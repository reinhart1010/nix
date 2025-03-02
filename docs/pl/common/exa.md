---
layout: page
title: common/exa (polski)
description: "Nowoczesny odpowiednik `ls` (wyświetla zawartość katalogu)."
content_hash: 6844a4020207a067860a1020a7670e637063e68f
last_modified_at: 2025-03-02
related_topics:
  - title: Deutsch version
    url: /de/common/exa.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/exa.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/exa.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/exa.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/exa.html
    icon: bi bi-globe
tldri18n_status: 2
---
# exa

Nowoczesny odpowiednik `ls` (wyświetla zawartość katalogu).
Więcej informacji: <https://github.com/ogham/exa>.

- Wyświetl listę plików, po jednym w linii:

`exa --oneline`

- Wyświetl wszystkie pliki, łącznie z ukrytymi:

`exa --all`

- Wyświetl listę wszystkich plików ze szczegółami (uprawnienia, właściciel, wielkość i data zmiany):

`exa --long --all`

- Wyświetl listę plików posortowaną względem wielkości pliku, od największego:

`exa --reverse --sort=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">size</span>

- Wyświetl drzewko plików (trzy poziomy):

`exa --long --tree --level=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">3</span>

- Wyświetl listę plików posortowaną względem daty zmiany, od najstarszego:

`exa --long --sort=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">modified</span>

- Wyświetl listę plików wraz z nagłówkiem, ikoną i statusem Git:

`exa --long --header --icons --git`

- Wyświetl listę plików, ignorując pliki z `.gitignore`:

`exa --git-ignore`
