---
layout: page
title: common/pamshadedrelief (English)
description: "Generate a shaded relief from an elevation map."
content_hash: c7af35172767deda3b85f030aa825e5995262e83
last_modified_at: 2024-03-04
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/pamshadedrelief.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># pamshadedrelief

Generate a shaded relief from an elevation map.
See also: `pamcrater`, `ppmrelief`.
More information: <https://netpbm.sourceforge.net/doc/pamshadedrelief.html>.

- Generate a shaded relief image with the input image interpreted as an elevation map:

`pamshadedrelief < `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input.pam</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output.pam</span>

- Gamma adjust the image by the specified factor:

`pamshadedrelief -gamma `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">factor</span>` < `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input.pam</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output.pam</span>
