---
layout: page
title: common/csslint (italiano)
description: "Un linter per codice CSS."
content_hash: 6a1e7d5681c1149be58a4820f37f63a607ea1089
related_topics:
  - title: English version
    url: /en/common/csslint.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/csslint.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/common/csslint.html
    icon: bi bi-globe
---
# csslint

Un linter per codice CSS.
Maggiori informazioni: <https://github.com/CSSLint/csslint/wiki/Command-line-interface>.

- Esegui il linting di un singolo file CSS:

`csslint `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file.css</span>

- Esegui il linting di file CSS multipli:

`csslint `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file1.css</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file2.css</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file3.css</span>

- Elenca tutte le possibili regole di stile:

`csslint --list-rules`

- Specifica certe regole come errori (che risulteranno in un codice d'uscita diverso da zero):

`csslint --errors=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">errors,universal-selector,imports</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file.css</span>

- Specifica certe regole come warning:

`csslint --warnings=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">box-sizing,selector-max,floats</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file.css</span>

- Specifica certe regole da essere completamente ignorate:

`csslint --ignore=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ids,rules-count,shorthand</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file.css</span>
