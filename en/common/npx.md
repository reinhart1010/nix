---
layout: page
title: common/npx (English)
description: "Execute binaries from `npm` packages."
content_hash: aaa05244b9c827289f7eb49a60b46d3be87b4db4
related_topics:
  - title: Deutsch version
    url: /de/common/npx.html
    icon: bi bi-globe
---
# npx

Execute binaries from `npm` packages.
More information: <https://github.com/npm/npx>.

- Execute the binary from a given npm module:

`npx `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">module_name</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command_arguments</span>

- In case a package has multiple binaries, specify the package name along with the binary:

`npx --package `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package_name</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">module_name</span>

- Run a command if existis in the current path or in `node_modules/.bin`:

`npx --no-install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command_arguments</span>

- Execute the binary from a given npm module suppressing any output from `npx` itself:

`npx --quiet `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">module_name</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command_arguments</span>

- Display help:

`npx --help`
