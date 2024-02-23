---
layout: page
title: common/fitstopnm (English)
description: "Convert a Flexible Image Transport System (FITS) file to a PNM image."
content_hash: 18805247bb5f39ba3e1a6f5f8c98b3d8a3c15902
last_modified_at: 2024-02-23
tldri18n_status: 2
---
# fitstopnm

Convert a Flexible Image Transport System (FITS) file to a PNM image.
See also: `pamtofits`.
More information: <https://netpbm.sourceforge.net/doc/fitstopnm.html>.

- Convert a FITS file to a PNM image:

`fitstopnm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.fits</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output.pnm</span>

- Convert the image on the specified position of the third axis in the FITS file:

`fitstopnm -image `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">z_position</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.fits</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output.pnm</span>
