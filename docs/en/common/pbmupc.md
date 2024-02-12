---
layout: page
title: common/pbmupc (English)
description: "Generate a PBM image of a Universal Product Code (UPC)."
content_hash: 99443dd2e9bc68d5cd0907f894148069a7924ebb
last_modified_at: 2024-02-12
tldri18n_status: 2
---
# pbmupc

Generate a PBM image of a Universal Product Code (UPC).
More information: <https://netpbm.sourceforge.net/doc/pbmupc.html>.

- Generate a UPC image for the specified product type, manufacturer code, and product code:

`pbmupc `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">product_type</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">manufacturer_code</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">product_code</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output.pbm</span>

- Use an alternative style that does not display the checksum:

`pbmupc -s2 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">product_type</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">manufacturer_code</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">product_code</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output.pbm</span>
