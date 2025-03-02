---
layout: page
title: freebsd/look (polski)
description: "Wyświetl linie zaczynające się od przedrostka w posortowanym pliku."
content_hash: 692dc88af7c9a2c7b3d7661dc579b598e1eb95b4
last_modified_at: 2025-03-02
related_topics:
  - title: English version
    url: /en/freebsd/look.html
    icon: bi bi-globe
  - title: español version
    url: /es/freebsd/look.html
    icon: bi bi-globe
  - title: हिन्दी version
    url: /hi/freebsd/look.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/freebsd/look.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/freebsd/look.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/freebsd/look.html
    icon: bi bi-globe
tldri18n_status: 2
---
# look

Wyświetl linie zaczynające się od przedrostka w posortowanym pliku.
Zobacz także: `grep`, `sort`.
Więcej informacji: <https://man.freebsd.org/cgi/man.cgi?look>.

- Wyszukaj linie zaczynające się określonym przedrostkiem w określonym pliku:

`look `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">przedrostek</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ścieżka/do/pliku</span>

- Wyszukuj bez uwzględniania wielkości liter, tylko znaki alfanumeryczne:

`look `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-f|--ignore-case</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-d|--alphanum</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">przedrostek</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ścieżka/do/pliku</span>

- Określ znak kończący ciąg znaków (domyślnie spacja):

`look `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-t|--terminate</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">,</span>

- Wyszukaj w `/usr/share/dict/words` (przyjęte opcje `--ignore-case` i `--alphanum`):

`look `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">przedrostek</span>
