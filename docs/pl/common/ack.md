---
layout: page
title: common/ack (polski)
description: "Narzędzie wyszukiwania, podobne do `grep`, zoptymalizowane dla programistów."
content_hash: 37d570d2111fad53ab118bd742f78f4f56e3aa71
last_modified_at: 2024-09-03
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

Narzędzie wyszukiwania, podobne do `grep`, zoptymalizowane dla programistów.
Zobacz też: `rg`, który jest znacznie szybszy.
Więcej informacji: <https://beyondgrep.com/documentation>.

- Szukaj rekurencyjnie plików zawierających ciąg znaków lub wyrażenie regularne w bieżącym katalogu:

`ack "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">wzorzec_wyszukiwania</span>`"`

- Szukaj na podstawie wzorca bez uwzględniania wielkości liter:

`ack --ignore-case "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">wzorzec_wyszukiwania</span>`"`

- Szukaj linii zawierających wzorzec, wyświetlając tylk[o] pasujący tekst bez pozostałej zawartości linii:

`ack -o "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">wzorzec_wyszukiwania</span>`"`

- Ogranicz wyszukiwanie do plików wyłącznie określonego typu:

`ack --type `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruby</span>` "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">wzorzec_wyszukiwania</span>`"`

- Wyszukaj z pominięciem plików określonego typu:

`ack --type no`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruby</span>` "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">wzorzec_wyszukiwania</span>`"`

- Policz całkowitą liczbę znalezionych dopasowań:

`ack --count --no-filename "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">wzorzec_wyszukiwania</span>`"`

- Pokaż nazwy plików i liczbę dopasowań w każdym z nich:

`ack --count --files-with-matches "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">wzorzec_wyszukiwania</span>`"`

- Wypisz wszystkie możliwe wartości które mogą być użyte dla `--type`:

`ack --help-types`
