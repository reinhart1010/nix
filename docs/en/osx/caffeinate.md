---
layout: page
title: osx/caffeinate (English)
description: "Prevent macOS from sleeping."
content_hash: b166d2199cbe0dbb409324b27cc0f81e31d83107
last_modified_at: 2023-09-23
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
---
# caffeinate

Prevent macOS from sleeping.
More information: <https://ss64.com/osx/caffeinate.html>.

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
