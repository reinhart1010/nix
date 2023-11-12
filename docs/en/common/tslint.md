---
layout: page
title: common/tslint (English)
description: "A pluggable linting utility for TypeScript."
content_hash: 7cca15b7e9ad4b9154b17bc59a382825ee54a8e0
last_modified_at: 2023-11-12
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

- Lint with the config file in the project root:

`tslint --project `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/project_root</span>
