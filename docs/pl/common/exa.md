---
layout: page
title: common/exa (polski)
description: "Nowoczesny odpowiednik `ls` (wyświetla zawartość katalogu)."
content_hash: 602afede9822f0825e4d06d32ed9ba29fd00d0db
last_modified_at: 2023-11-12
related_topics:
  - title: Deutsch version
    url: /de/common/exa.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/exa.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/exa.html
    icon: bi bi-globe
tldri18n_status: 2
---
# exa

Nowoczesny odpowiednik `ls` (wyświetla zawartość katalogu).
Więcej informacji: <https://the.exa.website>.

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
