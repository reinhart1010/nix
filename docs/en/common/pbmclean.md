---
layout: page
title: common/pbmclean (English)
description: "Clean up a PBM image by erasing isolated black and white pixels."
content_hash: d3113fd3eef5ff48834ab90698243e79228310d5
last_modified_at: 2024-02-13
tldri18n_status: 2
---
# pbmclean

Clean up a PBM image by erasing isolated black and white pixels.
More information: <https://netpbm.sourceforge.net/doc/pbmclean.html>.

- Clean up a PBM image by erasing isolated black and white pixels:

`pbmclean `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/image.pbm</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output.pbm</span>

- Clean up only black/white pixels:

`pbmclean -`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">black|white</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/image.pbm</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output.pbm</span>

- Specify the minimum number of neighbouring pixels of the same color in order for a pixel not to be considered isolated:

`pbmclean -minneighbours `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">3</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/image.pbm</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output.pbm</span>
