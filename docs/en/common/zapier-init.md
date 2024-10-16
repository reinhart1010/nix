---
layout: page
title: common/zapier-init (English)
description: "Initialize a new Zapier integration."
content_hash: 00f9c7b39116c2c06c300add1df9eabfe84b55f0
last_modified_at: 2024-10-16
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/zapier-init.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># zapier init

Initialize a new Zapier integration.
More information: <https://github.com/zapier/zapier-platform/blob/main/packages/cli/docs/cli.md#init>.

- Initialize a new Zapier integration:

`zapier init `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>

- Initialize a new Zapier integration with a specific template:

`zapier init `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-t|--template</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">basic-auth|callback|custom-auth|digest-auth|dynamic-dropdown|files|minimal|oauth1-trello|oauth2|search-or-create|session-auth|typescript</span>

- Show extra debugging output:

`zapier init `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-d|--debug</span>
