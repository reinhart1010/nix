---
layout: page
title: common/pamshadedrelief (English)
description: "Generate a shaded relief from an elevation map."
content_hash: c7af35172767deda3b85f030aa825e5995262e83
last_modified_at: 2024-03-05
tldri18n_status: 2
---
# pamshadedrelief

Generate a shaded relief from an elevation map.
See also: `pamcrater`, `ppmrelief`.
More information: <https://netpbm.sourceforge.net/doc/pamshadedrelief.html>.

- Generate a shaded relief image with the input image interpreted as an elevation map:

`pamshadedrelief < `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input.pam</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output.pam</span>

- Gamma adjust the image by the specified factor:

`pamshadedrelief -gamma `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">factor</span>` < `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input.pam</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output.pam</span>
