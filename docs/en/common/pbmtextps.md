---
layout: page
title: common/pbmtextps (English)
description: "Render text as a PBM image using PostScript."
content_hash: cc528e9457ff5eca8e8aca9702a339c9dbe22133
last_modified_at: 2024-11-02
tldri18n_status: 2
---
# pbmtextps

Render text as a PBM image using PostScript.
See also: `pbmtext`.
More information: <https://netpbm.sourceforge.net/doc/pbmtextps.html>.

- Render a single line of text as a PBM image:

`pbmtextps "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Hello World!</span>`" > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output.pbm</span>

- Specify the font and font size:

`pbmtextps -font `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Times-Roman</span>` -fontsize `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">30</span>` "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Hello World!</span>`" > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output.pbm</span>

- Specify the desired left and top margins:

`pbmtextps -leftmargin `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">70</span>` -topmargin `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">162</span>` "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Hello World!</span>`" > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output.pbm</span>

- Do not output the rendered text as a PBM image, but a PostScript program that would create this image:

`pbmtextps -dump-ps "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Hello World!</span>`" > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output.ps</span>
