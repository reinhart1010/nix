---
layout: page
title: common/rar (polski)
description: "Archiwizator RAR. Obsługuje wielotomowe archiwa, które mogą być opcjonalnie samorozpakowujące się."
content_hash: ae3a98285b2f6435e7a214eae3a74b678c3f5c8f
related_topics:
  - title: English version
    url: /en/common/rar.html
    icon: bi bi-globe
---
# rar

Archiwizator RAR. Obsługuje wielotomowe archiwa, które mogą być opcjonalnie samorozpakowujące się.
Więcej informacji: <https://manned.org/rar>.

- Zarchiwizuj 1 lub więcej plików:

`rar a `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">sciezka/do/nazwa_archiwum.rar</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">sciezka/do/plik1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">sciezka/do/plik2</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">sciezka/do/plik3</span>

- Zarchiwizuj katalog:

`rar a `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">sciezka/do/nazwa_archiwum.rar</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">sciezka/do/katalog</span>

- Podziel archiwum na części równej wielkości (50M):

`rar a -v`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">50M</span>` -R `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">sciezka/do/nazwa_archiwum.rar</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">sciezka/do/plik_lub_katalog</span>

- Chroń hasło wynikowego archiwum:

`rar a -p`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">haslo</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">sciezka/do/nazwa_archiwum.rar</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">sciezka/do/plik_lub_katalog</span>

- Szyfruj dane pliku i nagłówki za pomocą hasła:

`rar a -hp`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">haslo</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">sciezka/do/nazwa_archiwum.rar</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">sciezka/do/plik_lub_katalog</span>

- Użyj określonego poziomu kompresji (0-5):

`rar a -m`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">poziom_kompresji</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">sciezka/do/nazwa_archiwum.rar</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">sciezka/do/plik_lub_katalog</span>
