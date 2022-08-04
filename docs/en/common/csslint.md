---
layout: page
title: common/csslint (English)
description: "A linter for CSS code."
content_hash: d1bbcd625f359b0e8de08307a2c6cda36cc55951
related_topics:
  - title: italiano version
    url: /it/common/csslint.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/csslint.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/common/csslint.html
    icon: bi bi-globe
---
# csslint

A linter for CSS code.
More information: <https://github.com/CSSLint/csslint/wiki/Command-line-interface>.

- Lint a single CSS file:

`csslint `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file.css</span>

- Lint multiple CSS files:

`csslint `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file1.css</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file2.css</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file3.css</span>

- List all possible style rules:

`csslint --list-rules`

- Specify certain rules as errors (which result in a non-zero exit code):

`csslint --errors=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">errors,universal-selector,imports</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file.css</span>

- Specify certain rules as warnings:

`csslint --warnings=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">box-sizing,selector-max,floats</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file.css</span>

- Specify certain rules to ignore:

`csslint --ignore=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ids,rules-count,shorthand</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file.css</span>
