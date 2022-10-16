---
layout: page
title: windows/xcopy (polski)
description: "Kopiuje pliki i katalogi, w tym podkatalogi."
content_hash: af0395c61dc00c750968f579d6eb07ea8e59960c
related_topics:
  - title: Deutsch version
    url: /de/windows/xcopy.html
    icon: bi bi-globe
  - title: English version
    url: /en/windows/xcopy.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/windows/xcopy.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/windows/xcopy.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># xcopy

Kopiuje pliki i katalogi, w tym podkatalogi.
Więcej informacji: <https://learn.microsoft.com/windows-server/administration/windows-commands/xcopy>.

- Skopiuj plik(i) do określonego miejsca docelowego:

`xcopy `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ścieżka/do/pliku_lub_katalogu</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ścieżka/do/miejsca_przeznaczenia</span>

- Wyświetl listę plików, które zostaną skopiowane przed skopiowaniem:

`xcopy `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ścieżka/do/pliku_lub_katalogu</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ścieżka/do/miejsca_przeznaczenia</span>` /p`

- Skopiuj tylko strukturę katalogów, z wyłączeniem plików:

`xcopy `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ścieżka/do/pliku_lub_katalogu</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ścieżka/do/miejsca_przeznaczenia</span>` /t`

- Dołącz puste katalogi podczas kopiowania:

`xcopy `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ścieżka/do/pliku_lub_katalogu</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ścieżka/do/miejsca_przeznaczenia</span>` /e`

- Zachowaj źródłową listę ACL w miejscu docelowym:

`xcopy `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ścieżka/do/pliku_lub_katalogu</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ścieżka/do/miejsca_przeznaczenia</span>` /o`

- Zezwól na wznawianie po utracie połączenia sieciowego:

`xcopy `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ścieżka/do/pliku_lub_katalogu</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ścieżka/do/miejsca_przeznaczenia</span>` /z`

- Wyłącz monit, gdy plik istnieje w miejscu docelowym:

`xcopy `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ścieżka/do/pliku_lub_katalogu</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ścieżka/do/miejsca_przeznaczenia</span>` /y`

- Wyświetl szczegółowe informacje dotyczące polecenia:

`xcopy /?`
