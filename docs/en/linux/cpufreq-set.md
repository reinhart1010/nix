---
layout: page
title: linux/cpufreq-set (English)
description: "A tool to modify CPU frequency settings."
content_hash: 9025784e67e4b94a7974aa21284cfd8e0ad58201
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# cpufreq-set

A tool to modify CPU frequency settings.
The frequency value should range between the output of command `cpufreq-info -l`.
More information: <https://manned.org/cpufreq-set>.

- Set the CPU frequency policy of CPU 1 to "userspace":

`sudo cpufreq-set -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1</span>` -g `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">userspace</span>

- Set the current minimum CPU frequency of CPU 1:

`sudo cpufreq-set -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1</span>` --min `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">min_frequency</span>

- Set the current maximum CPU frequency of CPU 1:

`sudo cpufreq-set -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1</span>` --max `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">max_frequency</span>

- Set the current work frequency of CPU 1:

`sudo cpufreq-set -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1</span>` -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">work_frequency</span>
