---
layout: page
title: common/babel (polski)
description: "Transpiler, który konwertuje kod ze składni JavaScript ES6/ES7 na składnię ES5."
content_hash: af85a6f24a93b8e970002a55a930240da9761573
last_modified_at: 2024-09-13
related_topics:
  - title: English version
    url: /en/common/babel.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/babel.html
    icon: bi bi-globe
  - title: हिन्दी version
    url: /hi/common/babel.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/babel.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/babel.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/babel.html
    icon: bi bi-globe
tldri18n_status: 2
---
# babel

Transpiler, który konwertuje kod ze składni JavaScript ES6/ES7 na składnię ES5.
Więcej informacji: <https://babeljs.io/>.

- Transpiluj określony plik wejściowy i wypisz dane wyjściowe do `stdout`:

`babel `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ścieżka/do/pliku</span>

- Transpiluj określony plik wejściowy i zapisz wyjście do określonego pliku:

`babel `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ścieżka/do/pliku_wejściowego</span>` --out-file `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ścieżka/do/pliku_wyjściowego</span>

- Transpiluj plik wejściowy przy każdej zmianie:

`babel `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ścieżka/do/pliku_wejściowego</span>` --watch`

- Transpiluj cały katalog plików:

`babel `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ścieżka/do/katalogu_wejściowego</span>

- Zignoruj określone pliki oddzielone przecinkami w katalogu:

`babel `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ścieżka/do/katalogu_wejściowego</span>` --ignore `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ignorowany_plik1,ignorowany_plik2,...</span>

- Transpiluj i wypisz jako zminimalizowany JavaScript:

`babel `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ścieżka/do/pliku_wejściowego</span>` --minified`

- Wybierz zestaw ustawień dla formatowania wyjściowego:

`babel `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ścieżka/do/pliku_wejściowego</span>` --presets `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">preset1,preset2,...</span>

- Wyświetl pomoc:

`babel --help`
