---
layout: page
title: common/pbmtext (English)
description: "Render text as a PBM image."
content_hash: 268afe22f16b90b187a43cbbc309e6511e2f50bb
last_modified_at: 2024-02-13
tldri18n_status: 2
---
# pbmtext

Render text as a PBM image.
See also: `pbmtextps`.
More information: <https://netpbm.sourceforge.net/doc/pbmtext.html>.

- Render a single line of text as a PBM image:

`pbmtext "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Hello World!</span>`" > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output.pbm</span>

- Render multiple lines of text as a PBM image:

`echo "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Hello\nWorld!</span>`" | pbmtext > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output.pbm</span>

- Render text using a custom font supplied as a PBM file:

`pbmtext -font `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/font.pbm</span>` "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Hello World!</span>`" > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output.pbm</span>

- Specify the number of pixels between characters and lines:

`echo "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Hello\nWorld!</span>`" | pbmtext -space `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">3</span>` -lspace `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">10</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output.pbm</span>
