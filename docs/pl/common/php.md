---
layout: page
title: common/php (polski)
description: "Interfejs wiersza poleceń PHP."
content_hash: 76827059390c812fe817f2ad38283d21d035effe
related_topics:
  - title: English version
    url: /en/common/php.html
    icon: bi bi-globe
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/php.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># php

Interfejs wiersza poleceń PHP.
Więcej informacji: <https://php.net>.

- Parsuj i uruchom skrypt php:

`php `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">plik</span>

- Sprawdź składnię skryptu PHP (np. lint):

`php -l `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">plik</span>

- Uruchom PHP interaktywnie:

`php -a`

- Uruchom kod PHP (uwagi: nie używaj znaczników <? ?> ; unikaj podwójnych cudzysłowów z odwrotnym ukośnikiem):

`php -r "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">kod</span>`"`

- uruchom wbudowany serwer PHP w bieżącym katalogu:

`php -S `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">host:port</span>

- Uzyskaj listę zainstalowanych rozszerzeń PHP:

`php -m`

- Wyświetl informacje o bieżącej konfiguracji PHP:

`php -i`
