---
layout: page
title: linux/cpufreq-info (English)
description: "A tool to show CPU frequency information."
content_hash: fa046eaa1bf7f4a2103d43c453956091e569deb1
---
# cpufreq-info

A tool to show CPU frequency information.
More information: <https://manned.org/cpufreq-info>.

- Show CPU frequency information for all CPUs:

`cpufreq-info`

- Show CPU frequency information for the specified CPU:

`cpufreq-info -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">cpu_number</span>

- Show the allowed minimum and maximum CPU frequency:

`cpufreq-info -l`

- Show the current minimum and maximum CPU frequency and policy in table format:

`cpufreq-info -o`

- Show available CPU frequency policies:

`cpufreq-info -g`

- Show current CPU work frequency in a human-readable format, according to the cpufreq kernel module:

`cpufreq-info -f -m`

- Show current CPU work frequency in a human-readable format, by reading it from hardware (only available to root):

`sudo cpufreq-info -w -m`
