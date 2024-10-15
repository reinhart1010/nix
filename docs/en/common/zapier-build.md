---
layout: page
title: common/zapier-build (English)
description: "Build a pushable `zip` of a Zapier integration."
content_hash: 5e9902d0febff2f50cb8b2cd42e5902dc50056a2
last_modified_at: 2024-10-15
tldri18n_status: 2
---
# zapier build

Build a pushable `zip` of a Zapier integration.
More information: <https://github.com/zapier/zapier-platform/blob/main/packages/cli/docs/cli.md#build>.

- Create a build:

`zapier build`

- Disable smart file inclusion (will only include files required by `index.js`):

`zapier build --disable-dependency-detection`

- Show extra debugging output:

`zapier build `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-d|--debug</span>
