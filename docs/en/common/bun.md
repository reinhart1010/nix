---
layout: page
title: common/bun (English)
description: "JavaScript runtime and toolkit."
content_hash: 1240a07a030fcd62fe4394295c579622e0d04934
last_modified_at: 2023-11-12
related_topics:
  - title: français version
    url: /fr/common/bun.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/common/bun.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/bun.html
    icon: bi bi-globe
tldri18n_status: 2
---
# bun

JavaScript runtime and toolkit.
Includes a bundler, a test runner, and a package manager.
More information: <https://bun.sh>.

- Run a JavaScript file or a `package.json` script:

`bun run `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file|script_name</span>

- Run unit tests:

`bun test`

- Download and install all the packages listed as dependencies in `package.json`:

`bun install`

- Add a dependency to `package.json`:

`bun add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">module_name</span>

- Remove a dependency from `package.json`:

`bun remove `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">module_name</span>

- Create a new Bun project in the current directory:

`bun init`

- Start a REPL (interactive shell):

`bun repl`

- Upgrade Bun to the latest version:

`bun upgrade`
