---
layout: page
title: common/tslint (English)
description: "A pluggable linting utility for TypeScript."
content_hash: d9603fe4d5e100587140629c20576946e2b8b9e9
last_modified_at: 2024-01-25
tldri18n_status: 2
---
# tslint

A pluggable linting utility for TypeScript.
More information: <https://palantir.github.io/tslint>.

- Create TSLint config:

`tslint --init`

- Lint on a given set of files:

`tslint `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file1.js path/to/file2.js ...</span>

- Fix lint issues:

`tslint --fix`

- Lint with the configuration file in the project root:

`tslint --project `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/project_root</span>
