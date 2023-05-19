---
layout: page
title: common/eslint (polski)
description: "Podłączane narzędzie lintowania dla JavaScript i JSX."
content_hash: c4c9b6a4d05c90749f0b92abdf90cc731f408c9d
last_modified_at: 2023-05-19
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

Podłączane narzędzie lintowania dla JavaScript i JSX.
Więcej informacji: <https://eslint.org>.

- Stwórz eslint config:

`eslint --init`

- Lint na danym zestawie plików:

`eslint `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ścieżka/do/pliku1.js ścieżka/do/pliku2.js ...</span>

- Napraw lint issues:

`eslint --fix`

- Lint z config:

`eslint -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ścieżka/do/pliku_konfiguracyjnego</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ścieżka/do/źródła</span>
