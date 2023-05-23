---
layout: page
title: common/eslint (polski)
description: "Rozszerzalne narzędzie lintowania dla JavaScript i JSX."
content_hash: b7b9762dfa41b5a25b8e94c6cead7f0e5f26d908
last_modified_at: 2023-05-23
related_topics:
  - title: Deutsch version
    url: /de/common/eslint.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/eslint.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/eslint.html
    icon: bi bi-globe
---
# eslint

Rozszerzalne narzędzie lintowania dla JavaScript i JSX.
Więcej informacji: <https://eslint.org>.

- Stwórz plik konfiguracyjny ESlint:

`eslint --init`

- Lintuj jeden lub więcej plików:

`eslint `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ścieżka/do/pliku1.js ścieżka/do/pliku2.js ...</span>

- Napraw wykryte problemy:

`eslint --fix`

- Lintuj używając podanego pliku konfiguracyjnego:

`eslint -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ścieżka/do/pliku_konfiguracyjnego</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ścieżka/do/pliku1.js ścieżka/do/pliku2.js</span>
