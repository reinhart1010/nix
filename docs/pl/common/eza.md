---
layout: page
title: common/eza (polski)
description: "Nowoczesny odpowiednik `ls`, fork `exa`."
content_hash: 11872df4479414baf1b8cf445add7132c073be7a
last_modified_at: 2023-10-09
related_topics:
  - title: English version
    url: /en/common/eza.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># exa

Nowoczesny odpowiednik `ls`, fork `exa`.
Więcej informacji: <https://github.com/eza-community/eza>.

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
