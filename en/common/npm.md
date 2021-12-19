---
layout: page
title: common/npm (English)
description: "JavaScript and Node.js package manager."
content_hash: 49e08b2b6a673a4d3f3b621dc0864666e451a1d1
related_topics:
  - title: Deutsch version
    url: /de/common/npm.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/npm.html
    icon: bi bi-globe
---
# npm

JavaScript and Node.js package manager.
Manage Node.js projects and their module dependencies.
More information: <https://www.npmjs.com/>.

- Interactively create a `package.json` file:

`npm init`

- Download all the packages listed as dependencies in package.json:

`npm install`

- Download a specific version of a package and add it to the list of dependencies in `package.json`:

`npm install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">module_name</span>`@`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">version</span>

- Download a package and add it to the list of dev dependencies in `package.json`:

`npm install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">module_name</span>` --save-dev`

- Download a package and install it globally:

`npm install --global `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">module_name</span>

- Uninstall a package and remove it from the list of dependencies in `package.json`:

`npm uninstall `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">module_name</span>

- Print a tree of locally installed dependencies:

`npm list`

- List top-level globally installed modules:

`npm list --global --depth=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">0</span>
