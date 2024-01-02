---
layout: page
title: common/awk (polski)
description: "Wszechstronny język programowania do pracy na plikach."
content_hash: aeabfee1ad4e95995acfb5bb55a2fb895d3ab27b
last_modified_at: 2024-01-02
related_topics:
  - title: English version
    url: /en/common/awk.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/awk.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/awk.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/awk.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/awk.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/awk.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/awk.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/awk.html
    icon: bi bi-globe
tldri18n_status: 2
---
# awk

Wszechstronny język programowania do pracy na plikach.
Więcej informacji: <https://github.com/onetrueawk/awk>.

- Wydrukuj piątą kolumnę (aka. pole) w pliku oddzielonym spacjami:

`awk '{print $5}' `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nazwapliku</span>

- Wydrukuj drugą kolumnę wierszy zawierających "something" w pliku oddzielonym spacjami:

`awk '/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">coś</span>`/ {print $2}' `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nazwapliku</span>

- Wydrukuj ostatnią kolumnę każdego wiersza w pliku, używając przecinka (zamiast spacji) jako separatora pola:

`awk -F ',' '{print $NF}' `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nazwapliku</span>

- Zsumuj wartości w pierwszej kolumnie pliku i wydrukuj sumę:

`awk '{s+=$1} END {print s}' `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nazwapliku</span>

- Drukuj co trzeci wiersz, zaczynając od pierwszego wiersza:

`awk 'NR%3==1' `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nazwapliku</span>

- Wydrukuj różne wartości w zależności od warunków:

`awk '{if ($1 == "foo") print "Dokładne dopasowanie foo"; else if ($1 ~ "bar") print "Częściowe dopasowanie bar"; else print "Baz"}' `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nazwapliku</span>

- Wydrukuj wszystkie linie gdzie wartość 10-tej kolumny jest równa podanej wartości:

`awk '($10 == `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">wartość</span>`)'`

- Wydrukuj wszystkie linie, w których wartość 10-tej kolumny jest pomiędzy podanymi wartościami:

`awk '($10 >= `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">wartość_minimalna</span>` && $10 <= `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">wartość_maksymalna</span>`)'`
