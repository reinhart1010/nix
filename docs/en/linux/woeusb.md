---
layout: page
title: linux/woeusb (English)
description: "Windows media creation tool."
content_hash: 90699d30ab2fe6fdf2000b87f3c0c4254654e607
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# woeusb

Windows media creation tool.
More information: <https://github.com/WoeUSB/WoeUSB>.

- Format a USB then create a bootable Windows installation drive:

`woeusb --device `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/windows.iso</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sdX</span>

- Copy Windows files to an existing partition of a USB storage device and make it bootable, without erasing the current data:

`woeusb --partition `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/windows.iso</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sdXN</span>
