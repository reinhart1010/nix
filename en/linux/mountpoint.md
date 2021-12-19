---
layout: page
title: linux/mountpoint (English)
description: "Test if a directory is a filesystem mountpoint."
content_hash: a4572c7ab9bde1b353db96a70d094490cc46cacf
---
# mountpoint

Test if a directory is a filesystem mountpoint.
More information: <https://manned.org/mountpoint>.

- Check if a directory is a mountpoint:

`mountpoint `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>

- Check if a directory is a mountpoint without showing any output:

`mountpoint -q `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>

- Show major/minor numbers of a mountpoint's filesystem:

`mountpoint --fs-devno `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>
