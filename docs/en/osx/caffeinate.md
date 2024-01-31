---
layout: page
title: osx/caffeinate (English)
description: "Prevent macOS from sleeping."
content_hash: aeb4617b2972d78833162bbb0ae9880e3fcc68b5
last_modified_at: 2024-01-31
related_topics:
  - title: Deutsch version
    url: /de/osx/caffeinate.html
    icon: bi bi-globe
  - title: español version
    url: /es/osx/caffeinate.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/osx/caffeinate.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/osx/caffeinate.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/osx/caffeinate.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/osx/caffeinate.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/osx/caffeinate.html
    icon: bi bi-globe
tldri18n_status: 2
---
# caffeinate

Prevent macOS from sleeping.
More information: <https://keith.github.io/xcode-man-pages/caffeinate.8.html>.

- Prevent from sleeping for 1 hour (3600 seconds):

`caffeinate -u -t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">3600</span>

- Prevent from sleeping until a command completes:

`caffeinate -s "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>`"`

- Prevent from sleeping until a process with the specified PID completes:

`caffeinate -w `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pid</span>

- Prevent from sleeping (use `Ctrl + C` to exit):

`caffeinate -i`

- Prevent disk from sleeping (use `Ctrl + C` to exit):

`caffeinate -m`
