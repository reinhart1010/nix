---
layout: page
title: linux/nmon (English)
description: "A system administrator, tuner, and benchmark tool."
content_hash: 3a6e7d8985206b15a22a269c58124c1cec7222cc
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# nmon

A system administrator, tuner, and benchmark tool.
More information: <https://manned.org/nmon>.

- Start `nmon`:

`nmon`

- Save records to file ("-s 300 -c 288" by default):

`nmon -f`

- Save records to file with a total of 240 measurements, by taking 30 seconds between each measurement:

`nmon -f -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">30</span>` -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">240</span>
