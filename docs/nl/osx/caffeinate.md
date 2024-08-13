---
layout: page
title: osx/caffeinate (Nederlands)
description: "Voorkom dat macOS in slaapstand gaat."
content_hash: 25ec7fcb9670e6afde02a265d7f45c7a12d04848
last_modified_at: 2024-08-13
related_topics:
  - title: Deutsch version
    url: /de/osx/caffeinate.html
    icon: bi bi-globe
  - title: English version
    url: /en/osx/caffeinate.html
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
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/osx/caffeinate.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># caffeinate

Voorkom dat macOS in slaapstand gaat.
Meer informatie: <https://keith.github.io/xcode-man-pages/caffeinate.8.html>.

- Voorkom slaapstand voor 1 uur (3600 seconden):

`caffeinate -u -t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">3600</span>

- Voorkom slaapstand totdat een commando is voltooid:

`caffeinate -s "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">commando</span>`"`

- Voorkom slaapstand totdat een proces met de opgegeven PID is voltooid:

`caffeinate -w `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pid</span>

- Voorkom slaapstand (gebruik `Ctrl + C` om te stoppen):

`caffeinate -i`

- Voorkom dat de schijf in slaapstand gaat (gebruik `Ctrl + C` om te stoppen):

`caffeinate -m`
