---
layout: page
title: common/yarn (English)
description: "JavaScript and Node.js package manager alternative."
content_hash: e985a5f5a820494392274fe3b376bca2f9f5f5ae
last_modified_at: 2023-11-12
related_topics:
  - title: Deutsch version
    url: /de/common/yarn.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/yarn.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/yarn.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/yarn.html
    icon: bi bi-globe
tldri18n_status: 2
---
# yarn

JavaScript and Node.js package manager alternative.
More information: <https://yarnpkg.com>.

- Install a module globally:

`yarn global add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">module_name</span>

- Install all dependencies referenced in the `package.json` file (the `install` is optional):

`yarn install`

- Install a module and save it as a dependency to the `package.json` file (add `--dev` to save as a dev dependency):

`yarn add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">module_name</span>`@`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">version</span>

- Uninstall a module and remove it from the `package.json` file:

`yarn remove `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">module_name</span>

- Interactively create a `package.json` file:

`yarn init`

- Identify whether a module is a dependency and list other modules that depend upon it:

`yarn why `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">module_name</span>
