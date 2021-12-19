---
layout: page
title: linux/spectre-meltdown-checker (English)
description: "Spectre and Meltdown mitigation detection tool."
content_hash: 2d479c5583da4b062ee3344247cf9017457844f6
---
# spectre-meltdown-checker

Spectre and Meltdown mitigation detection tool.
More information: <https://manned.org/spectre-meltdown-checker>.

- Check the currently running kernel for Spectre or Meltdown:

`sudo spectre-meltdown-checker`

- Check the currently running kernel and show an explanation of the actions to take to mitigate a vulnerability:

`sudo spectre-meltdown-checker --explain`

- Check for specific variants (defaults to all):

`sudo spectre-meltdown-checker --variant `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1|2|3|3a|4|l1tf|msbds|mfbds|mlpds|mdsum|taa|mcespc|srbds</span>

- Display output using a specific output format:

`sudo spectre-meltdown-checker --batch `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">text|json|nrpe|prometheus|short</span>

- Don't use the `/sys` interface even if present:

`sudo spectre-meltdown-checker --no-sysfs`

- Check a non-running kernel:

`sudo spectre-meltdown-checker --kernel `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/kernel_file</span>
