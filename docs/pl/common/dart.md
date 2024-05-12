---
layout: page
title: common/dart (polski)
description: "Zarządzaj projektami Dart."
content_hash: a50efb22340df31805c70f552631aec5018c170a
last_modified_at: 2024-05-12
related_topics:
  - title: Deutsch version
    url: /de/common/dart.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/dart.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/dart.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/dart.html
    icon: bi bi-globe
tldri18n_status: 2
---
# dart

Zarządzaj projektami Dart.
Więcej informacji: <https://dart.dev/tools/dart-tool>.

- Zainicjuj nowy projekt Dart w katalogu o tej samej nazwie:

`dart create `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nazwa_projektu</span>

- Uruchom plik Dart:

`dart run `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ścieżka/do/pliku.dart</span>

- Pobierz zależności dla obecnego projektu:

`dart pub get`

- Uruchom testy jednostkowe dla obecnego projektu:

`dart test`

- Aktualizuj przestarzałe zależności projektu w celu obsługi null-safety:

`dart pub upgrade --null-safety`

- Skompiluj plik Dart do natywnego pliku binarnego:

`dart compile exe `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ścieżka/do/pliku.dart</span>

- Zastosuj automatyczne poprawki dla obecnego projektu:

`dart fix --apply`
