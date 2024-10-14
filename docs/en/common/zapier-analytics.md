---
layout: page
title: common/zapier-analytics (English)
description: "Show the status of the analytics that are collected. It is also used to change what is collected."
content_hash: b929fdbdc6140145cc6c0b3804781179d9046e07
last_modified_at: 2024-10-14
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/zapier-analytics.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># zapier analytics

Show the status of the analytics that are collected. It is also used to change what is collected.
More information: <https://github.com/zapier/zapier-platform/blob/main/packages/cli/docs/cli.md#analytics>.

- Show the status of collected analytics:

`zapier analytics`

- Change how much information is collected:

`zapier analytics `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-m|--mode</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">enabled|anonymous|disabled</span>

- Show extra debugging output:

`zapier analytics `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-m|--mode</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">enabled|anonymous|disabled</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-d|--debug</span>
