---
layout: page
title: common/test (polski)
description: "Sprawdza typy plików i porównuje wartości."
content_hash: ead6f4aba133de9f2e2d9c69ae4fdb60969f63cd
related_topics:
  - title: English version
    url: /en/common/test.html
    icon: bi bi-globe
  - title: 日本語 version
    url: /ja/common/test.html
    icon: bi bi-globe
---
# test

Sprawdza typy plików i porównuje wartości.
Zwraca 0 gdy porównanie zwróciło wartość poprawną, 1 gdy fałszywą.
Więcej informacji: <https://www.gnu.org/software/coreutils/test>.

- Sprawdź czy podana zmienna jest równa łańcuchowi znaków:

`test "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">$ZMIENNA</span>`" == "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/bin/zsh</span>`"`

- Sprawdź czy zmienna jest pusta:

`test -z "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">$GIT_BRANCH</span>`"`

- Sprawdź czy plik istnieje:

`test -f "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ścieżka/do/pliku</span>`"`

- Sprawdź czy katalog nie istnieje:

`test ! -d "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ścieżka/do/katalogu</span>`"`

- Zapis jeśli porawne-jeśli fałszywe:

`test `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">warunek</span>` && `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">echo "gdy poprawne"</span>` || `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">echo "gdy fałszywe"</span>
