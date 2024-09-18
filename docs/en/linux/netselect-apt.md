---
layout: page
title: linux/netselect-apt (English)
description: "Create a `sources.list` file for a Debian mirror with the lowest latency."
content_hash: f6a6a7c1738ddcad7d2bd15fbcf2d54238fc36c0
last_modified_at: 2024-09-18
tldri18n_status: 2
---
# netselect-apt

Create a `sources.list` file for a Debian mirror with the lowest latency.
More information: <https://manned.org/netselect-apt>.

- Create `sources.list` using the lowest latency server:

`sudo netselect-apt`

- Specify Debian branch, stable is used by default:

`sudo netselect-apt `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">testing</span>

- Include non-free section:

`sudo netselect-apt --non-free`

- Specify a country for the mirror list lookup:

`sudo netselect-apt -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">India</span>
