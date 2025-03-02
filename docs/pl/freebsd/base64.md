---
layout: page
title: freebsd/base64 (polski)
description: "Enkoduj lub dekoduj plik lub `stdin` do/z base64, do `stdout` lub innego pliku."
content_hash: 71df1917381629bfab2ac6e2162a80edcbb39848
last_modified_at: 2025-03-02
related_topics:
  - title: English version
    url: /en/freebsd/base64.html
    icon: bi bi-globe
  - title: हिन्दी version
    url: /hi/freebsd/base64.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/freebsd/base64.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/freebsd/base64.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/freebsd/base64.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/freebsd/base64.html
    icon: bi bi-globe
tldri18n_status: 2
---
# base64

Enkoduj lub dekoduj plik lub `stdin` do/z base64, do `stdout` lub innego pliku.
Więcej informacji: <https://man.freebsd.org/cgi/man.cgi?query=base64>.

- Enkoduj plik do `stdout`:

`base64 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-i|--input</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ścieżka/do/pliku</span>

- Enkoduj plik do określonego pliku wyjściowego:

`base64 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-i|--input</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ścieżka/do/pliku_wejściowego</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-o|--output</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ścieżka/do/pliku_wyjściowego</span>

- Zawijaj zakodowane wyjście na określonej szerokości (`0` wyłącza zawijanie):

`base64 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-b|--break</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">0|76|...</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ścieżka/do/pliku</span>

- Dekoduj plik do `stdout`:

`base64 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-d|--decode</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-i|--input</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ścieżka/do/pliku</span>

- Enkoduj z `stdin` do `stdout`:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">komenda</span>` | base64`

- Dekoduj z `stdin` do `stdout`:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">komenda</span>` | base64 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-d|--decode</span>
