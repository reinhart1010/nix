---
layout: page
title: common/pnmmontage (English)
description: "Create a montage from multiple PNM images."
content_hash: e8f036b8d0664e73a53519c68ba95471ac34b7c5
last_modified_at: 2024-02-10
tldri18n_status: 2
---
# pnmmontage

Create a montage from multiple PNM images.
More information: <https://netpbm.sourceforge.net/doc/pnmmontage.html>.

- Produce a packing of the specified images:

`pnmmontage `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/image1.pnm path/to/image2.pnm ...</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output.pnm</span>

- Specify the quality of the packing (Note: larger values produce smaller packings but take longer to compute.):

`pnmmontage -`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">0..9</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/image1.pnm path/to/image2.pnm ...</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output.pnm</span>

- Produce a packing that is not larger than `p` percent of the optimal packing:

`pnmmontage -quality `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">p</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/image1.pnm path/to/image2.pnm ...</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output.pnm</span>

- Write the positions of the input files within the packed image to a machine-readable file:

`pnmmontage -data `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/datafile</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/image1.pnm path/to/image2.pnm ...</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output.pnm</span>
