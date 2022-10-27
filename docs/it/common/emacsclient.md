---
layout: page
title: common/emacsclient (italiano)
description: "Apri file in un server emacs esistente."
content_hash: 9fe7e7bd7f382f5256936b05f0c87f3b5da51580
related_topics:
  - title: Deutsch version
    url: /de/common/emacsclient.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/emacsclient.html
    icon: bi bi-globe
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/emacsclient.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># emacsclient

Apri file in un server emacs esistente.
Maggiori informazioni: <https://www.emacswiki.org/emacs/EmacsClient>.

- Apri un file in un server Emacs esistente (utilizzando la GUI se disponibile):

`emacsclient `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_file</span>

- Apri un file in modalità console (senza finestra X):

`emacsclient -nw `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_file</span>

- Apri un file in un frame Emacs esistente e ritorna immediatamente:

`emacsclient -n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_file</span>
