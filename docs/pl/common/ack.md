---
layout: page
title: common/ack (polski)
description: "Narzędzie wyszukiwania, takie jak grep, zoptymalizowane dla programistów."
content_hash: c373a0c1666ebad37aa50ad7ff22e3b7bfed9ef2
last_modified_at: 2024-05-05
related_topics:
  - title: বাংলা version
    url: /bn/common/ack.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/ack.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/ack.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/ack.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/ack.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/ack.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/ack.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/ack.html
    icon: bi bi-globe
  - title: norsk version
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
tldri18n_status: 2
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

`ack --type `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruby</span>` "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">wzorzec</span>`"`

- Wyszukaj z pominięciem plików określonego typu:

`ack --type no`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruby</span>` "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">wzorzec</span>`"`

- Policz całkowitą liczbę dopasowań:

`ack --count --no-filename "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">wzorzec</span>`"`

- Pokaż nazwy plików i liczbę dopasowań w każdym z nich:

`ack --count --files-with-matches "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">wzorzec</span>`"`

- Wypisz wszystkie możliwe wartości które mogą być użyte dla `--type`:

`ack --help-types`
