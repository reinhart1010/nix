---
layout: page
title: common/pamcrater (English)
description: "Create a PAM image of cratered terrain."
content_hash: eb4258f97ef1e3c73371e260e7856e32170825aa
last_modified_at: 2024-03-05
tldri18n_status: 2
---
# pamcrater

Create a PAM image of cratered terrain.
See also: `pamshadedrelief`, `ppmrelief`.
More information: <https://netpbm.sourceforge.net/doc/pamcrater.html>.

- Create an image of cratered terrain with the specified dimensions:

`pamcrater -height `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">height</span>` -width `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">width</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output.pam</span>

- Create an image containing the specified number of craters:

`pamcrater -number `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">n_craters</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output.pam</span>
