---
layout: page
title: common/npx (English)
description: "Execute binaries from `npm` packages."
content_hash: cc790a6daaf2a0626d161f2c53adc308e6514979
related_topics:
  - title: Deutsch version
    url: /de/common/npx.html
    icon: bi bi-globe
---
# npx

Execute binaries from `npm` packages.
More information: <https://www.npmjs.com/package/npx>.

- Execute the binary from a given npm module:

`npx `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">module_name</span>

- In case a package has multiple binaries, specify the package name along with the binary:

`npx -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package_name</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">module_name</span>

- View help contents:

`npx --help`
