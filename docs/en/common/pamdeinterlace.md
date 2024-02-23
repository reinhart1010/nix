---
layout: page
title: common/pamdeinterlace (English)
description: "Remove every other row in a Netpbm image."
content_hash: 05646cdd28e6aef83fe08679607b7b8b41575101
last_modified_at: 2024-02-23
tldri18n_status: 2
---
# pamdeinterlace

Remove every other row in a Netpbm image.
See also: `pammixinterlace`.
More information: <https://netpbm.sourceforge.net/doc/pamdeinterlace.html>.

- Produce an image consisting of the input's even-numbered rows:

`pamdeinterlace `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/image.ppm</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output.ppm</span>

- Produce an image consisting of the input's odd-numbered rows:

`pamdeinterlace -takeodd `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/image.ppm</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output.ppm</span>
