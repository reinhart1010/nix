---
layout: page
title: linux/sar (English)
description: "Monitor performance of various Linux subsystems."
content_hash: 04fa524fcb48c6fac56fb6f70d8f1de69fb97d9d
---
# sar

Monitor performance of various Linux subsystems.

- Report I/O and transfer rate issued to physical devices, one per second (press CTRL+C to quit):

`sar -b `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1</span>

- Report a total of 10 network device statistics, one per 2 seconds:

`sar -n DEV `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">2</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">10</span>

- Report CPU utilization, one per 2 seconds:

`sar -u ALL `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">2</span>

- Report a total of 20 memory utilization statistics, one per second:

`sar -r ALL `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">20</span>

- Report the run queue length and load averages, one per second:

`sar -q `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1</span>

- Report paging statistics, one per 5 seconds:

`sar -B `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">5</span>
