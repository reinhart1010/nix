---
layout: page
title: linux/isoinfo (English)
description: "Utility programs for dumping and verifying ISO disk images."
content_hash: 0ea88bbfbc43eb9734323c8714ff78f902f3bce5
last_modified_at: 2022-12-04
---
# isoinfo

Utility programs for dumping and verifying ISO disk images.
More information: <https://manned.org/isoinfo>.

- List all the files included in an ISO image:

`isoinfo -f -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/image.iso</span>

- E[x]tract a specific file from an ISO image and send it out `stdout`:

`isoinfo -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/image.iso</span>` -x `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/PATH/TO/FILE/INSIDE/ISO.EXT</span>

- Show header information for an ISO disk image:

`isoinfo -d -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/image.iso</span>
