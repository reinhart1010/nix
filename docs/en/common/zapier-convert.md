---
layout: page
title: common/zapier-convert (English)
description: "Convert a Visual Builder integration to a CLI integration."
content_hash: b26f21b18dc48cd7912bd2d50fe62fe57beee895
last_modified_at: 2024-10-17
tldri18n_status: 2
---
# zapier convert

Convert a Visual Builder integration to a CLI integration.
More information: <https://github.com/zapier/zapier-platform/blob/main/packages/cli/docs/cli.md#convert>.

- Convert a visual builder integration:

`zapier convert `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">integration_id</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>

- Convert a visual builder integration with a specific version:

`zapier convert `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">integration_id</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-v|--version</span>`=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">version</span>

- Show extra debugging output:

`zapier convert --debug`
