---
layout: page
title: common/npx (English)
description: "Execute binaries from `npm` packages."
content_hash: 06fbe77616fd3185d418584cd7785ea0a2221628
related_topics:
  - title: Deutsch version
    url: /de/common/npx.html
    icon: bi bi-globe
---
# npx

Execute binaries from `npm` packages.
More information: <https://github.com/npm/npx>.

- Execute the binary from a given npm module:

`npx `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">module_name</span>

- In case a package has multiple binaries, specify the package name along with the binary:

`npx -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package_name</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">module_name</span>

- View help contents:

`npx --help`
