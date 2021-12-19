---
layout: page
title: common/dirname (italiano)
description: "Determina la directory genitore di un determinato file o percorso."
content_hash: bacd9e9c4f0e4ff843e2d03ab30748746ef48c9c
related_topics:
  - title: English version
    url: /en/common/dirname.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/dirname.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/dirname.html
    icon: bi bi-globe
---
# dirname

Determina la directory genitore di un determinato file o percorso.
Maggiori informazioni: <https://www.gnu.org/software/coreutils/dirname>.

- Calcola la directory genitore di un dato percorso:

`dirname `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/a/file_o_directory</span>

- Calcola la directory genitore di più percorsi:

`dirname `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/a/file_a</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/a/directory_b</span>

- Delimita l'output con caratteri NUL invece di newline (utile in combinazione con `xargs`):

`dirname --zero `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/a/directory_a</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/a/file_b</span>
