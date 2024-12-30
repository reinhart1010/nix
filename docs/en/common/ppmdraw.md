---
layout: page
title: common/ppmdraw (English)
description: "Draw lines, text and more on a PPM image by executing a script."
content_hash: c18224b54cca771f17faa692f95515ecde8c8e36
last_modified_at: 2024-12-30
tldri18n_status: 2
---
# ppmdraw

Draw lines, text and more on a PPM image by executing a script.
Documentation on the utilized scripting language can be found by following the link below.
More information: <https://netpbm.sourceforge.net/doc/ppmdraw.html>.

- Draw on the specified PPM image by executing the supplied script:

`ppmdraw -script '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">setpos 50 50; text_here "hello!"; </span>`' `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/image.pnm</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output.pnm</span>

- Draw on the specified PPM image by executing the script in the specified file:

`ppmdraw -scriptfile `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/script</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/image.pnm</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output.pnm</span>
