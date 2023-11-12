---
layout: page
title: windows/choco-new (polski)
description: "Generowanie nowych specyfikacji pakietów Chocolatey."
content_hash: 0029f46dcade8b4cff6852b0ca4ac320b04baf25
last_modified_at: 2023-11-12
related_topics:
  - title: Deutsch version
    url: /de/windows/choco-new.html
    icon: bi bi-globe
  - title: English version
    url: /en/windows/choco-new.html
    icon: bi bi-globe
  - title: français version
    url: /fr/windows/choco-new.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/windows/choco-new.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/windows/choco-new.html
    icon: bi bi-globe
tldri18n_status: 2
---
# choco new

Generowanie nowych specyfikacji pakietów Chocolatey.
Więcej informacji: <https://chocolatey.org/docs/commands-new>.

- Utwórz nowy szkielet pakietu:

`choco new `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nazwa_pakietu</span>

- Utwórz nowy pakiet podając konkretną wersję:

`choco new `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nazwa_pakietu</span>` --version `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">wersja</span>

- Utwórz nowy pakiet podając podając nazwę opiekuna:

`choco new `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nazwa_pakietu</span>` --maintainer `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nazwa_opiekuna</span>

- Utwórz nowy pakiet w podanym katalogu wyjściowym:

`choco new `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nazwa_pakietu</span>` --output-directory `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ścieżka/do/katalogu/wyjściowego</span>

- Utwórz nowy pakiet podając specyficzne adresy URL instalatoró dla wersji 32-bit i 64-bit:

`choco new `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nazwa_pakietu</span>` url="`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">adres_url</span>`" url64="`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">adres_url</span>`"`
