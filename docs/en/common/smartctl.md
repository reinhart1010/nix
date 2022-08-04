---
layout: page
title: common/smartctl (English)
description: "View a disk's SMART data and other information."
content_hash: d880e0b140229bcc54d1159a0fa1d1306b345715
---
# smartctl

View a disk's SMART data and other information.
More information: <https://en.wikipedia.org/wiki/S.M.A.R.T.>.

- View SMART health summary:

`sudo smartctl --health `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sdX</span>

- View device information:

`sudo smartctl --info `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sdX</span>

- Begin a short self-test:

`sudo smartctl --test short `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sdX</span>

- View current/last self-test status and other SMART capabilities:

`sudo smartctl --capabilities `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sdX</span>

- View SMART self-test log (if supported):

`sudo smartctl --log selftest `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sdX</span>
