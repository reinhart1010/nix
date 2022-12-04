---
layout: page
title: linux/ttyplot (English)
description: "A realtime plotting utility for the command line with data input from `stdin`."
content_hash: 76fc3ccb0d46672c5205113b144f6f9f2e1b84a5
last_modified_at: 2022-12-04
---
# ttyplot

A realtime plotting utility for the command line with data input from `stdin`.
More information: <https://github.com/tenox7/ttyplot>.

- Plot the values `1`, `2` and `3` (`cat` prevents ttyplot to exit):

`{ echo `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1 2 3</span>`; cat } | ttyplot`

- Set a specific title and unit:

`{ echo `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1 2 3</span>`; cat } | ttyplot -t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">title</span>` -u `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">unit</span>

- Use a while loop to continuously plot random values:

`{ while `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">true</span>`; do echo `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">$RANDOM</span>`; sleep `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1</span>`; done } | ttyplot`

- Parse the output from `ping` and visualize it:

`ping `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">8.8.8.8</span>` | sed -u '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">s/^.*time=//g; s/ ms//g</span>`' | ttyplot -t "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ping to 8.8.8.8</span>`" -u `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ms</span>
