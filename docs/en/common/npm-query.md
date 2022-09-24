---
layout: page
title: common/npm-query (English)
description: "Print an array of dependency objects using CSS-like selectors."
content_hash: 747b857227c25cf99b5f21e61408b4c6f4199d11
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># npm query

Print an array of dependency objects using CSS-like selectors.
More information: <https://docs.npmjs.com/cli/v8/commands/npm-query>.

- Print direct dependencies:

`npm query ':root > *'`

- Print all direct production/development dependencies:

`npm query ':root > .`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">prod|dev</span>`'`

- Print dependencies with a specific name:

`npm query '#`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package_name</span>`'`

- Print dependencies with a specific name and within a semantic versioning range:

`npm query #`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package_name</span>`@`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">semantic_version</span>

- Print dependencies which have no dependencies:

`npm query ':empty'`

- Find all dependencies with postinstall scripts and uninstall them:

`npm query ":attr(scripts, [postinstall])" | jq 'map(.name) | join("\n")' -r | xargs -I {} npm uninstall {}`

- Find all Git dependencies and print which application requires them:

`npm query ":type(git)" | jq 'map(.name)' | xargs -I {} npm why {}`
