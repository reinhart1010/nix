---
layout: page
title: common/pdftk (polski)
description: "Zestaw narzędzi PDF."
content_hash: be7ec62cdca5357bc61d39f66cc61366a1a42111
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/pdftk.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/pdftk.html
    icon: bi bi-globe
tldri18n_status: 2
---
# pdftk

Zestaw narzędzi PDF.
Więcej informacji: <https://www.pdflabs.com/tools/pdftk-the-pdf-toolkit>.

- Wyodrębnij strony 1-3, 5 i 6-10 z pliku PDF oraz zapisz je jako inny plik PDF:

`pdftk `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">plik_wejściowy.pdf</span>` cat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1-3 5 6-10</span>` output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">plik_wyjściowy.pdf</span>

- Połącz listę plików PDF i zapisz połączony plik jako:

`pdftk `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">plik1.pdf plik2.pdf ...</span>` cat output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">plik_wyjściowy.pdf</span>

- Podziel każdą stronę pliku PDF do osobnych plików, o nazwie nadanej według zdefiniowanego wzoru:

`pdftk `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">plik_wejściowy.pdf</span>` burst output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">plik_wyjściowy_%d.pdf</span>

- Obróć wszystkie strony o 180 stopni zgodnie ze wskazówkami zegara:

`pdftk `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">plik_wejściowy.pdf</span>` cat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1-endsouth</span>` output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">plik_wyjściowy.pdf</span>

- Obóć trzecią stronę o 90 stopni zgodnie ze wskazówkami zegara oraz pozostaw pozostałe strony bez zmian:

`pdftk `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">plik_wejściowy.pdf</span>` cat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1-2 3east 4-end</span>` output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">plik_wyjściowy.pdf</span>
