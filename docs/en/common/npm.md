---
layout: page
title: common/npm (English)
description: "JavaScript and Node.js package manager."
content_hash: e841e8f1e3c2ae9988dd05918c3573891e9c0ca4
last_modified_at: 2023-11-12
related_topics:
  - title: Deutsch version
    url: /de/common/npm.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/npm.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/npm.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/npm.html
    icon: bi bi-globe
tldri18n_status: 2
---
# npm

JavaScript and Node.js package manager.
Manage Node.js projects and their module dependencies.
More information: <https://www.npmjs.com>.

- Interactively create a `package.json` file:

`npm init`

- Download all the packages listed as dependencies in `package.json`:

`npm install`

- Download a specific version of a package and add it to the list of dependencies in `package.json`:

`npm install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package_name</span>`@`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">version</span>

- Download the latest version of a package and add it to the list of dev dependencies in `package.json`:

`npm install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package_name</span>` --save-dev`

- Download the latest version of a package and install it globally:

`npm install --global `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package_name</span>

- Uninstall a package and remove it from the list of dependencies in `package.json`:

`npm uninstall `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package_name</span>

- List of locally installed dependencies:

`npm list`

- List top-level globally installed packages:

`npm list --global --depth=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">0</span>
