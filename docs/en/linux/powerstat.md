---
layout: page
title: linux/powerstat (English)
description: "Measures the power consumption of a computer that has a battery power source or supports the RAPL interface."
content_hash: 381085aeb9f3466529c502987a6521703417d3db
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># powerstat

Measures the power consumption of a computer that has a battery power source or supports the RAPL interface.
More information: <https://manned.org/powerstat>.

- Measure power with the default of 10 samples with an interval of 10 seconds:

`powerstat`

- Measure power with custom number of samples and interval duration:

`powerstat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">interval</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">number_of_samples</span>

- Measure power using Intel's RAPL interface:

`powerstat -R `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">interval</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">number_of_samples</span>

- Show a histogram of the power measurements:

`powerstat -H `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">interval</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">number_of_samples</span>

- Enable all statistics gathering options:

`powerstat -a `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">interval</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">number_of_samples</span>
