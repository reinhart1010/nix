---
layout: page
title: common/csslint (polski)
description: "Linter dla kodu CSS."
content_hash: ef15a2e8b46f452f39d6d9aa9f1f8e491c9b82d2
last_modified_at: 2023-11-12
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

Linter dla kodu CSS.
Więcej informacji: <https://github.com/CSSLint/csslint/wiki/Command-line-interface>.

- Lintowanie pojedynczego pliku CSS:

`csslint `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">plik.css</span>

- Lintowanie wiele plików CSS:

`csslint `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">plik1.css</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">plik2.css</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">plik3.css</span>

- Wymień wszystkie możliwe reguły stylu:

`csslint --list-rules`

- Określ pewne reguły jako błędy (które powodują niezerowy kod wyjścia):

`csslint --errors=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">bledy,universal-selector,imports</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">plik.css</span>

- Określ pewne reguły jako ostrzeżenia:

`csslint --warnings=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">box-sizing,selector-max,floats</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">plik.css</span>

- Określ pewne reguły, które będą całkowicie ignorowane:

`csslint --ignore=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ids,rules-count,shorthand</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">plik.css</span>
