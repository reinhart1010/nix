---
layout: page
title: linux/cpufreq-aperf (English)
description: "Calculate the average CPU frequency over a time period."
content_hash: 7fe79c9e31ee8a9eb6caa1b07a218449b0c2e95c
---
# cpufreq-aperf

Calculate the average CPU frequency over a time period.
Requires root privileges.
More information: <https://manned.org/cpufreq-aperf>.

- Start calculating, defaulting to all CPU cores and 1 second refresh interval:

`sudo cpufreq-aperf`

- Start calculating for CPU 1 only:

`sudo cpufreq-aperf -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1</span>

- Start calculating with a 3 second refresh interval for all CPU cores:

`sudo cpufreq-aperf -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">3</span>

- Calculate only once:

`sudo cpufreq-aperf -o`
