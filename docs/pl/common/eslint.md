---
layout: page
title: common/eslint (polski)
description: "Podłączane narzędzie lintowania dla JavaScript i JSX."
content_hash: 5b5339a96bb77ff58ea9673eb96ae1bae047d834
related_topics:
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

`eslint `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nazwapliku</span>`.js `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nazwapliku1</span>`.js`

- Napraw lint issues:

`eslint --fix`

- Lint z config:

`eslint -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">sciezka/do/pliku_config</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">app/src</span>
