---
layout: page
title: common/dirname (italiano)
description: "Determina la directory genitore di un determinato file o percorso."
content_hash: 19fc3d66ef797a3a972edeedeb0cf41e967e2345
last_modified_at: 2025-03-02
related_topics:
  - title: English version
    url: /en/common/dirname.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/dirname.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/dirname.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/dirname.html
    icon: bi bi-globe
tldri18n_status: 2
---
# dirname

Determina la directory genitore di un determinato file o percorso.
Maggiori informazioni: <https://www.gnu.org/software/coreutils/manual/html_node/dirname-invocation.html>.

- Calcola la directory genitore di un dato percorso:

`dirname `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/del/file_o_directory</span>

- Calcola la directory genitore di più percorsi:

`dirname `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/del/file_or_directory1 percorso/del/file_or_directory2 ...</span>

- Delimita l'output utilizzando caratteri NUL invece di una nuova linea (utile in combinazione con `xargs`):

`dirname --zero `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/del/file_or_directory1 percorso/del/file_or_directory2 ...</span>
