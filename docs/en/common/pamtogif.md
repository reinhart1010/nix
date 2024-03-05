---
layout: page
title: common/pamtogif (English)
description: "Convert a Netpbm image into an unanimated GIF image."
content_hash: 03f004bdc6071e88a9e8cdfb625f62d038ccacb6
last_modified_at: 2024-03-05
tldri18n_status: 2
---
# pamtogif

Convert a Netpbm image into an unanimated GIF image.
See also: `giftopnm`, `gifsicle`.
More information: <https://netpbm.sourceforge.net/doc/pamtogif.html>.

- Convert a Netpbm image into an unanimated GIF image:

`pamtogif `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/image.pam</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output.gif</span>

- Mark the specified color as transparent in the output GIF file:

`pamtogif -transparent `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">color</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/image.pam</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output.gif</span>

- Include the specified text as a comment in the output GIF file:

`pamtogif -comment "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Hello World!</span>`" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/image.pam</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output.gif</span>
