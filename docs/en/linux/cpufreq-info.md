---
layout: page
title: linux/cpufreq-info (English)
description: "Show CPU frequency information."
content_hash: 886f16994b73f9610972118077836a3439103815
last_modified_at: 2024-02-25
tldri18n_status: 2
---
# cpufreq-info

Show CPU frequency information.
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
