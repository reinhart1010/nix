---
layout: page
title: osx/yaa (polski)
description: "Twórz i manipuluj archiwami YAA."
content_hash: a6c3cfa8d51c16ca90556511b0bd96e0616307b1
last_modified_at: 2024-05-07
related_topics:
  - title: English version
    url: /en/osx/yaa.html
    icon: bi bi-globe
  - title: español version
    url: /es/osx/yaa.html
    icon: bi bi-globe
tldri18n_status: 2
---
# yaa

Twórz i manipuluj archiwami YAA.
Więcej informacji: <https://keith.github.io/xcode-man-pages/yaa.1.html>.

- Utwórz archiwum z katalogu:

`yaa archive -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ścieżka/do/katalogu</span>` -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ścieżka/do/pliku_wyjścia.yaa</span>

- Utwórz archiwum z pliku:

`yaa archive -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ścieżka/do/pliku</span>` -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ścieżka/do/pliku_wyjścia.yaa</span>

- Wypakuj archiwum do obecnego folderu:

`yaa extract -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ścieżka/do/pliku_archiwum.yaa</span>

- Wyświetl zawartość archiwum:

`yaa list -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ścieżka/do/pliku_archiwum.yaa</span>

- Utwórz archiwum z określonym algorytmem kompresji:

`yaa archive -a `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">algorytm</span>` -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ścieżka/do/folderu</span>` -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ścieżka/do/pliku_wyjścia.yaa</span>

- Utwórz archiwum o rozmiarze bloku 8 MB:

`yaa archive -b `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">8m</span>` -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ścieżka/do/folderu</span>` -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ścieżka/do/pliku_wyjścia.yaa</span>
