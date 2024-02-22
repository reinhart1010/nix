---
layout: page
title: common/pamdeinterlace (English)
description: "Remove every other row in a Netpbm image."
content_hash: 05646cdd28e6aef83fe08679607b7b8b41575101
last_modified_at: 2024-02-22
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/pamdeinterlace.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># pamdeinterlace

Remove every other row in a Netpbm image.
See also: `pammixinterlace`.
More information: <https://netpbm.sourceforge.net/doc/pamdeinterlace.html>.

- Produce an image consisting of the input's even-numbered rows:

`pamdeinterlace `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/image.ppm</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output.ppm</span>

- Produce an image consisting of the input's odd-numbered rows:

`pamdeinterlace -takeodd `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/image.ppm</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output.ppm</span>
