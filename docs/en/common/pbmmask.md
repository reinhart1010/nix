---
layout: page
title: common/pbmmask (English)
description: "Create a mask bitmap from a regular bitmap."
content_hash: 197dcc8282bb01b429e9479c6f18dc6511598a7c
last_modified_at: 2024-02-13
tldri18n_status: 2
---
# pbmmask

Create a mask bitmap from a regular bitmap.
See also: `pambackground`.
More information: <https://netpbm.sourceforge.net/doc/pbmmask.html>.

- Create a mask bitmap separating background from foreground:

`pbmmask `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/image.pbm</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output.pbm</span>

- Expand the generated mask by one pixel:

`pbmmask -expand `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/image.pbm</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output.pbm</span>
