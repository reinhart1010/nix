---
layout: page
title: common/tslint (English)
description: "A pluggable linting utility for TypeScript."
content_hash: 7d746c0aca424d6a4d3c3577fa73922f69b6ce18
---
# tslint

A pluggable linting utility for TypeScript.
More information: <https://palantir.github.io/tslint>.

- Create TSLint config:

`tslint --init`

- Lint on a given set of files:

`tslint `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">filename</span>`.js `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">filename1</span>`.js`

- Fix lint issues:

`tslint --fix`

- Lint with the config file in the project root:

`tslint --project `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/project_root</span>
