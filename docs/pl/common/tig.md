---
layout: page
title: common/tig (polski)
description: "Interfejs tekstowy dla Gita."
content_hash: fc81cee4f61a422a9f491f4fecab09c24ea2ae3c
last_modified_at: 2024-05-06
related_topics:
  - title: Deutsch version
    url: /de/common/tig.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/tig.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># tig

Interfejs tekstowy dla Gita.
Więcej informacji: <https://jonas.github.io/tig/doc/manual.html>.

- Pokaż listę commitów w odwrotnej kolejności chronologicznej, zaczynając od najnowszego:

`tig`

- Pokaż historię wybranej gałęzi:

`tig `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">gałąź</span>

- Pokaż historię wybranych plików lub katalogów:

`tig `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ścieżka1 ścieżka2 ...</span>

- Pokaż różnice pomiędzy dwiema referencjami (np. gałęziami lub tagami):

`tig `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">bazowa_ref</span>`..`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">porównywana_ref</span>

- Wyświetl comity ze wszystkich gałęzi i stash:

`tig --all`

- Rozpocznij w widoku stash, wyświetlając wszystkie zmiany w stash:

`tig stash`
