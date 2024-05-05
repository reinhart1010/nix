---
layout: page
title: osx/yaa (polski)
description: "Tworzenie archiwów YAA i manipulowanie nimi."
content_hash: a9eaae5a06bb20191461b206a9a0a842c8d07646
last_modified_at: 2024-05-05
related_topics:
  - title: English version
    url: /en/osx/yaa.html
    icon: bi bi-globe
  - title: español version
    url: /es/osx/yaa.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/osx/yaa.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># yaa

Tworzenie archiwów YAA i manipulowanie nimi.
Więcej informacji: <https://keith.github.io/xcode-man-pages/yaa.1.html>.

- Tworzenie archiwum z katalogu:

`yaa archive -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">sciezka/do/katalogu</span>` -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">sciezka/do/pliku_wyjscia.yaa</span>

- Tworzenie archiwum z pliku:

`yaa archive -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">sciezka/do/pliku</span>` -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">sciezka/do/pliku_wyjscia.yaa</span>

- Wypakowanie archiwum do obecnego folderu:

`yaa extract -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">sciezka/do/pliku_archiwum.yaa</span>

- Lista zawartości archiwum:

`yaa list -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">sciezka/do/pliku_archiwum.yaa</span>

- Tworzenie archiwum z określonym algorytmem kompresji:

`yaa archive -a `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">algorytm</span>` -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">sciezka/do/folderu</span>` -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">sciezka/do/pliku_wyjscia.yaa</span>

- Utwórz archiwum o rozmiarze bloku 8 MB:

`yaa archive -b `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">8m</span>` -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">sciezka/do/folderu</span>` -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">sciezka/do/pliku_wyjscia.yaa</span>
