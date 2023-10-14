---
layout: page
title: common/eza (polski)
description: "Nowoczesny odpowiednik `ls`, fork `exa`."
content_hash: ec762a81fe4fccd5663d26a9d56989ee37092fcc
last_modified_at: 2023-10-14
related_topics:
  - title: English version
    url: /en/common/eza.html
    icon: bi bi-globe
---
# eza

Nowoczesny odpowiednik `ls`, fork `exa`.
Więcej informacji: <https://github.com/eza-community/eza>.

- Wyświetl listę plików, po jednym w linii:

`eza --oneline`

- Wyświetl wszystkie pliki, łącznie z ukrytymi:

`eza --all`

- Wyświetl listę wszystkich plików ze szczegółami (uprawnienia, właściciel, wielkość i data zmiany):

`eza --long --all`

- Wyświetl listę plików posortowaną względem wielkości pliku, od największego:

`eza --reverse --sort=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">size</span>

- Wyświetl drzewko plików (trzy poziomy):

`eza --long --tree --level=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">3</span>

- Wyświetl listę plików posortowaną względem daty zmiany, od najstarszego:

`eza --long --sort=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">modified</span>

- Wyświetl listę plików wraz z nagłówkiem, ikoną i statusem Git:

`eza --long --header --icons --git`

- Wyświetl listę plików, ignorując pliki z `.gitignore`:

`eza --git-ignore`
