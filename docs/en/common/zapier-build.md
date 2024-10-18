---
layout: page
title: common/zapier-build (English)
description: "Build a pushable `zip` of a Zapier integration."
content_hash: 11ac40fb9079e13b20c9f567bdd537039fd8882e
last_modified_at: 2024-10-18
tldri18n_status: 2
---
# zapier build

Build a pushable `zip` of a Zapier integration.
More information: <https://platform.zapier.com/reference/cli#build>.

- Create a build:

`zapier build`

- Disable smart file inclusion (will only include files required by `index.js`):

`zapier build --disable-dependency-detection`

- Show extra debugging output:

`zapier build `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-d|--debug</span>
