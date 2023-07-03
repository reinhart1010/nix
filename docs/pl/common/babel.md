---
layout: page
title: common/babel (polski)
description: "Transpiler, który konwertuje kod ze składni JavaScript ES6 / ES7 na składnię ES5."
content_hash: 1804ded7288561bca72cb6b685557e839a93cf74
last_modified_at: 2023-07-03
related_topics:
  - title: English version
    url: /en/common/babel.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/babel.html
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
---
# babel

Transpiler, który konwertuje kod ze składni JavaScript ES6 / ES7 na składnię ES5.
Więcej informacji: <https://babeljs.io/>.

- Transpiluj określony plik wejściowy i dane wyjściowe do `stdout`:

`babel `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">siezka/do/pliku</span>

- Transpiluj określony plik wejściowy i wyjście do określonego pliku:

`babel `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">sciezka/do/pliku_wejsciowego</span>` --out-file `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">sciezka/do/pliku_wyjsciowego</span>

- Transpiluj plik wejściowy przy każdej zmianie:

`babel `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">sciezka/do/pliku_wejsciowego</span>` --watch`

- Transpiluj cały katalog plików:

`babel `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">sciezka/do/katalogu_wejsciowego</span>

- Zignoruj określone pliki oddzielone przecinkami w katalogu:

`babel `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">sciezka/do/katalogu_wejsciowego</span>` --ignore `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ignorowane_pliki</span>

- Transpiluj i wypisz jako zminimalizowany JavaScript:

`babel `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">sciezka/do/pliku_wejsciowego</span>` --minified`

- Wybierz zestaw ustawień dla formatowania wyjściowego:

`babel `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">sciezka/do/pliku_wejsciowego</span>` --presets `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">presets</span>

- Wyświetl wszystkie dostępne opcje:

`babel --help`
