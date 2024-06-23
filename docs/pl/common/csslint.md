---
layout: page
title: common/csslint (polski)
description: "Lintuj kod CSS."
content_hash: 810e9ea5e517e11d0af5985e22787f6c4dc95c79
last_modified_at: 2024-06-23
related_topics:
  - title: English version
    url: /en/common/csslint.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/csslint.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/csslint.html
    icon: bi bi-globe
tldri18n_status: 2
---
# csslint

Lintuj kod CSS.
Więcej informacji: <https://github.com/CSSLint/csslint/wiki/Command-line-interface>.

- Lintuj pojedyńczy plik CSS:

`csslint `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">plik.css</span>

- Lintuj wiele plików CSS:

`csslint `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">plik1.css plik2.css ...</span>

- Wymień wszystkie możliwe reguły stylu:

`csslint --list-rules`

- Określ pewne reguły jako błędy (które powodują niezerowy kod wyjścia):

`csslint --errors=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">errors,universal-selector,imports</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">plik.css</span>

- Określ pewne reguły jako ostrzeżenia:

`csslint --warnings=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">box-sizing,selector-max,floats</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">plik.css</span>

- Ignoruj określone reguły:

`csslint --ignore=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ids,rules-count,shorthand</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">plik.css</span>
