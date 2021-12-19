---
layout: page
title: common/pathchk (polski)
description: "Sprawdź poprawność oraz przenośność jednej lub większej ilości ścieżek."
content_hash: 6147172f8833d6f79c9584efedc7c7f5bf146acf
related_topics:
  - title: English version
    url: /en/common/pathchk.html
    icon: bi bi-globe
---
# pathchk

Sprawdź poprawność oraz przenośność jednej lub większej ilości ścieżek.
Więcej informacji: <https://www.gnu.org/software/coreutils/pathchk>.

- Sprawdź ścieżki pod kątem poprawności w obecnym systemie:

`pathchk `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ścieżka1 ścieżka2 …</span>

- Sprawdź ścieżki pod kątem poprawności w szerszym zakresie systemów zgodnych z POSIX:

`pathchk -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ścieżka1 ścieżka2 …</span>

- Sprawdź ścieżki pod kątem poprawności we wszystkich systemach zgodnych z POSIX:

`pathchk --portability `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ścieżka1 ścieżka2 …</span>

- Sprawdź tylko pod kątem pustych ścieżek lub wiodących myślników (-):

`pathchk -P `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ścieżka1 ścieżka2 …</span>
