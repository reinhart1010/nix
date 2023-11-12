---
layout: page
title: common/npm-query (English)
description: "Print an array of dependency objects using CSS-like selectors."
content_hash: 232cacdd305a397a23ddd4c117c9af0ce453b7cc
last_modified_at: 2023-11-12
related_topics:
  - title: 한국어 version
    url: /ko/common/npm-query.html
    icon: bi bi-globe
tldri18n_status: 2
---
# npm query

Print an array of dependency objects using CSS-like selectors.
More information: <https://docs.npmjs.com/cli/v8/commands/npm-query>.

- Print direct dependencies:

`npm query ':root > *'`

- Print all direct production/development dependencies:

`npm query ':root > .`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">prod|dev</span>`'`

- Print dependencies with a specific name:

`npm query '#`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package</span>`'`

- Print dependencies with a specific name and within a semantic versioning range:

`npm query #`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package</span>`@`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">semantic_version</span>

- Print dependencies which have no dependencies:

`npm query ':empty'`

- Find all dependencies with postinstall scripts and uninstall them:

`npm query ":attr(scripts, [postinstall])" | jq 'map(.name) | join("\n")' -r | xargs -I {} npm uninstall {}`

- Find all Git dependencies and print which application requires them:

`npm query ":type(git)" | jq 'map(.name)' | xargs -I {} npm why {}`
