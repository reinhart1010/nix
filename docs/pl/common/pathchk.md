---
layout: page
title: common/pathchk (polski)
description: "Sprawdź poprawność oraz przenośność jednej lub większej ilości ścieżek."
content_hash: a153c15ac71b9aee9273720d5ae8dafc4f75d420
last_modified_at: 2025-03-02
related_topics:
  - title: English version
    url: /en/common/pathchk.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/pathchk.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/pathchk.html
    icon: bi bi-globe
tldri18n_status: 2
---
# pathchk

Sprawdź poprawność oraz przenośność jednej lub większej ilości ścieżek.
Więcej informacji: <https://www.gnu.org/software/coreutils/manual/html_node/pathchk-invocation.html>.

- Sprawdź ścieżki pod kątem poprawności w obecnym systemie:

`pathchk `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ścieżka1 ścieżka2 …</span>

- Sprawdź ścieżki pod kątem poprawności w szerszym zakresie systemów zgodnych z POSIX:

`pathchk -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ścieżka1 ścieżka2 …</span>

- Sprawdź ścieżki pod kątem poprawności we wszystkich systemach zgodnych z POSIX:

`pathchk --portability `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ścieżka1 ścieżka2 …</span>

- Sprawdź tylko pod kątem pustych ścieżek lub wiodących myślników (-):

`pathchk -P `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ścieżka1 ścieżka2 …</span>
