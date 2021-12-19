---
layout: page
title: linux/chcpu (English)
description: "Enable/disable a system's CPUs."
content_hash: 1daf5a095aecb9a2adb0c061c1c62870da6226fa
---
# chcpu

Enable/disable a system's CPUs.
More information: <https://manned.org/chcpu>.

- Disable CPUs via a list of CPU ID numbers:

`chcpu -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1,3</span>

- Enable a set of CPUs via a range of CPU ID numbers:

`chcpu -e `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1-10</span>
