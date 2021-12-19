---
layout: page
title: common/fls (English)
description: "List files and directories in an image file or device."
content_hash: d6d2ba94fe51e7613bf7b8c639dd44216e0a773d
---
# fls

List files and directories in an image file or device.
More information: <https://wiki.sleuthkit.org/index.php?title=Fls>.

- Build a recursive fls list over a device, output paths will start with C:

`fls -r -m `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">C:</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/loop1p1</span>

- Analyse a single partition, providing the sector offset at which the filesystem starts in the image:

`fls -r -m `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">C:</span>` -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">sector</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/image_file</span>

- Analyse a single partition, providing the timezone of the original system:

`fls -r -m `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">C:</span>` -z `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">timezone</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/loop1p1</span>
