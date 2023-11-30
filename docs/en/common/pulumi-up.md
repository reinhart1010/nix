---
layout: page
title: common/pulumi-up (English)
description: "Create or update the resources in a stack."
content_hash: f53d2011ef9b4bd8cf9c5ea46ea098736ae63123
last_modified_at: 2023-11-30
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/pulumi-up.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># pulumi up

Create or update the resources in a stack.
More information: <https://www.pulumi.com/docs/cli/commands/pulumi_up/>.

- Preview and deploy changes to a program and/or infrastructure:

`pulumi up`

- Automatically approve and perform the update after previewing it:

`pulumi up --yes`

- Preview and deploy changes in a specific stack:

`pulumi up --stack `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">stack</span>
