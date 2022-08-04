---
layout: page
title: common/pdfimages (polski)
description: "Narzędzie do wyodrębniania obrazów z plików PDF."
content_hash: 6cde8125fb1daec6209456bbbfa5fc0895241aba
related_topics:
  - title: English version
    url: /en/common/pdfimages.html
    icon: bi bi-globe
---
# pdfimages

Narzędzie do wyodrębniania obrazów z plików PDF.
Więcej informacji: <https://manned.org/pdfimages>.

- Wyodrębnij wszystkie obrazy z pliku PDF i zapisz je jako pliki PNG:

`pdfimages -png `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ścieżka/do/pliku.pdf</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">przedrostek_nazwy_pliku</span>

- Wyodrębnij obrazy ze stron 3 do 5:

`pdfimages -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">3</span>` -l `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">5</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ścieżka/do/pliku.pdf</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">przedrostek_nazwy_pliku</span>

- Wyodrębnij obrazy z pliku PDF oraz zawrzyj numer strony w nazwach wyjściowych:

`pdfimages -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ścieżka/do/pliku.pdf</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">przedrostek_nazwy_pliku</span>

- Wyświetl listę informacji o każdym obrazie w pliku PDF:

`pdfimages -list `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ścieżka/do/pliku.pdf</span>
