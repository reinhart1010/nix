---
layout: page
title: common/ack (polski)
description: "Narzędzie wyszukiwania, takie jak grep, zoptymalizowane dla programistów."
content_hash: 4063005f0575a0ea0042073f0569122c529716c1
related_topics:
  - title: English version
    url: /en/common/ack.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/ack.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/ack.html
    icon: bi bi-globe
  - title: norsk bokmål (Norge) version
    url: /no/common/ack.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/ack.html
    icon: bi bi-globe
  - title: русский version
    url: /ru/common/ack.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/common/ack.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/ack.html
    icon: bi bi-globe
---
# ack

Narzędzie wyszukiwania, takie jak grep, zoptymalizowane dla programistów.
Zobacz też: `rg`, który jest znacznie szybszy.
Więcej informacji: <https://beyondgrep.com/documentation>.

- Znajdź pliki zawierające ciąg znaków lub wyrażenie regularne rekurencyjnie w bieżącym katalogu:

`ack "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">wzorzec</span>`"`

- Szukaj na podstawie wzorca bez uwzględniania wielkości liter:

`ack --ignore-case "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">wzorzec</span>`"`

- Szukaj linii zawierających wzorzec, wyświetl wyłącznie pasujący tekst bez pozostałej zawartości linii:

`ack -o "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">wzorzec</span>`"`

- Ogranicz wyszukiwanie do plików wyłącznie określonego typu:

`ack --type=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruby</span>` "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">wzorzec</span>`"`

- Wyszukaj z pominięciem plików określonego typu:

`ack --type=no`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruby</span>` "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">wzorzec</span>`"`

- Policz całkowitą liczbę dopasowań:

`ack --count --no-filename "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">wzorzec</span>`"`

- Pokaż nazwy plików i liczbę dopasowań w każdym z nich:

`ack --count --files-with-matches "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">wzorzec</span>`"`

- Wypisz wszystkie możliwe wartości które mogą być użyte dla `--type`:

`ack --help-types`
