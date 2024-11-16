---
layout: page
title: common/npm-install (English)
description: "Install Node packages."
content_hash: cc25156cc76d4f25b7be5e78e3dff007aef1ffe2
last_modified_at: 2024-11-16
related_topics:
  - title: 한국어 version
    url: /ko/common/npm-install.html
    icon: bi bi-globe
tldri18n_status: 2
---
# npm install

Install Node packages.
More information: <https://docs.npmjs.com/cli/commands/npm-install>.

- Install dependencies listed in `package.json`:

`npm install`

- Download a specific version of a package and add it to the list of dependencies in `package.json`:

`npm install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package_name</span>`@`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">version</span>

- Download the latest version of a package and add it to the list of dev dependencies in `package.json`:

`npm install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package_name</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-D|--save-dev</span>

- Download the latest version of a package and install it globally:

`npm install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-g|--global</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package_name</span>
