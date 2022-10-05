---
layout: page
title: common/smartctl (English)
description: "Monitor disk health including SMART data."
content_hash: 9f459c366379896c3366536d5d712c1461028d41
---
# smartctl

Monitor disk health including SMART data.
More information: <https://www.smartmontools.org>.

- Display SMART health summary:

`sudo smartctl --health `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sdX</span>

- Display device information:

`sudo smartctl --info `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sdX</span>

- Start a short self-test in the background:

`sudo smartctl --test short `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sdX</span>

- Display current/last self-test status and other SMART capabilities:

`sudo smartctl --capabilities `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sdX</span>

- Display exhaustive SMART data:

`sudo smartctl --all `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sdX</span>
