---
layout: page
title: linux/cpupower (English)
description: "Tools regarding CPU power and tuning options."
content_hash: 3f9e560c1b7653455f712bb19418506c72b45043
last_modified_at: 2023-11-15
tldri18n_status: 2
---
# cpupower

Tools regarding CPU power and tuning options.
More information: <https://manned.org/cpupower>.

- List CPUs:

`sudo cpupower --cpu `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">all</span>` info`

- Print information about all cores:

`sudo cpupower --cpu `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">all</span>` info`

- Set all CPUs to a power-saving frequency governor:

`sudo cpupower --cpu `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">all</span>` frequency-set --governor `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">powersave</span>

- Print CPU 0's available frequency [g]overnors:

`sudo cpupower --cpu `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">0</span>` frequency-info g | grep "analyzing\|governors"`

- Print CPU 4's frequency from the hardware, in a human-readable format:

`sudo cpupower --cpu `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">4</span>` frequency-info --hwfreq --human`
