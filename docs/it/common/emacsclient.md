---
layout: page
title: common/emacsclient (italiano)
description: "Apri file in un server emacs esistente."
content_hash: cb00c1d8dee840fcdf75501a4813d070e049bd41
last_modified_at: 2024-10-03
related_topics:
  - title: Deutsch version
    url: /de/common/emacsclient.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/emacsclient.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># emacsclient

Apri file in un server emacs esistente.
Maggiori informazioni: <https://www.gnu.org/software/emacs/manual/html_node/emacs/emacsclient-Options.html>.

- Apri un file in un server Emacs esistente (utilizzando la GUI se disponibile):

`emacsclient `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_file</span>

- Apri un file in modalità console (senza finestra X):

`emacsclient -nw `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_file</span>

- Apri un file in un frame Emacs esistente e ritorna immediatamente:

`emacsclient -n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_file</span>
