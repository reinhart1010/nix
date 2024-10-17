---
layout: page
title: common/zapier-push (English)
description: "Build and upload a Zapier integration."
content_hash: 71e16ec6ff81f5427ab41fa48686a778e33995f5
last_modified_at: 2024-10-17
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/zapier-push.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># zapier push

Build and upload a Zapier integration.
More information: <https://github.com/zapier/zapier-platform/blob/main/packages/cli/docs/cli.md#push>.

- Push an integration to Zapier:

`zapier push`

- Disable smart file inclusion (will only include files required by `index.js`):

`zapier push --disable-dependency-detection`

- Show extra debugging output:

`zapier push `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-d|--debug</span>
