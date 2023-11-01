---
layout: page
title: common/rar (polski)
description: "Archiwizator RAR. Obsługuje wielotomowe archiwa, które mogą być opcjonalnie samorozpakowujące się."
content_hash: ddc3cb1ec8d29ed5623feeec2cc36dd73f00741a
last_modified_at: 2023-11-01
related_topics:
  - title: English version
    url: /en/common/rar.html
    icon: bi bi-globe
---
# rar

Archiwizator RAR. Obsługuje wielotomowe archiwa, które mogą być opcjonalnie samorozpakowujące się.
Więcej informacji: <https://manned.org/rar>.

- Zarchiwizuj 1 lub więcej plików:

`rar a `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ścieżka/do/nazwa_archiwum.rar</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ścieżka/do/pliku1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ścieżka/do/pliku2</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ścieżka/do/pliku3</span>

- Zarchiwizuj katalog:

`rar a `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ścieżka/do/nazwa_archiwum.rar</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ścieżka/do/katalogu</span>

- Podziel archiwum na części równej wielkości (50M):

`rar a -v`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">50M</span>` -R `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ścieżka/do/nazwa_archiwum.rar</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ścieżka/do/pliku_lub_katalogu</span>

- Chroń hasłem powstające archiwum:

`rar a -p`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">hasło</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ścieżka/do/nazwa_archiwum.rar</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ścieżka/do/pliku_lub_katalogu</span>

- Szyfruj dane pliku i ich nagłówki za pomocą hasła:

`rar a -hp`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">hasło</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ścieżka/do/nazwa_archiwum.rar</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ścieżka/do/pliku_lub_katalogu</span>

- Użyj określonego poziomu kompresji (0-5):

`rar a -m`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">poziom_kompresji</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ścieżka/do/nazwa_archiwum.rar</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ścieżka/do/pliku_lub_katalogu</span>
