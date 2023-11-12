---
layout: page
title: common/emacsclient (italiano)
description: "Apri file in un server emacs esistente."
content_hash: 9fe7e7bd7f382f5256936b05f0c87f3b5da51580
last_modified_at: 2023-11-12
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
Maggiori informazioni: <https://www.emacswiki.org/emacs/EmacsClient>.

- Apri un file in un server Emacs esistente (utilizzando la GUI se disponibile):

`emacsclient `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_file</span>

- Apri un file in modalità console (senza finestra X):

`emacsclient -nw `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_file</span>

- Apri un file in un frame Emacs esistente e ritorna immediatamente:

`emacsclient -n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_file</span>
