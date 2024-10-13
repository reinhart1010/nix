---
layout: page
title: common/cppclean (italiano)
description: "Trova codice inutilizzato in progetti C++."
content_hash: c087a795bb6eb8f4f5beb174702664de1b9e3248
last_modified_at: 2024-10-13
related_topics:
  - title: English version
    url: /en/common/cppclean.html
    icon: bi bi-globe
  - title: فارسی version
    url: /fa/common/cppclean.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/cppclean.html
    icon: bi bi-globe
tldri18n_status: 2
---
# cppclean

Trova codice inutilizzato in progetti C++.
Maggiori informazioni: <https://github.com/myint/cppclean>.

- Esegui nella directory di un progetto:

`cppclean `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/della/directory_progetto</span>

- Esegui su di un progetto dove gli header sono nella directory "inc1" ed "inc2":

`cppclean `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/della/directory_progetto</span>` --include-path `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">inc1</span>` --include-path `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">inc2</span>

- Esegui su di uno specifico file `main.cpp`:

`cppclean `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">main.cpp</span>

- Esegui della directory corrente, escludendo la directory "build":

`cppclean `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">.</span>` --exclude `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">build</span>
