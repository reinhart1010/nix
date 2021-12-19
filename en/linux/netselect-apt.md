---
layout: page
title: linux/netselect-apt (English)
description: "Create a `sources.list` file for a Debian mirror with the lowest latency."
content_hash: 120605f94446425571673a3106ea1b9fc6c3ed06
---
# netselect-apt

Create a `sources.list` file for a Debian mirror with the lowest latency.
More information: <https://manpages.debian.org/buster/netselect-apt/netselect-apt.1.html>.

- Create `sources.list` using the lowest latency server:

`sudo netselect-apt`

- Specify Debian branch, stable is used by default:

`sudo netselect-apt `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">testing</span>

- Include non-free section:

`sudo netselect-apt --non-free`

- Specify a country for the mirror list lookup:

`sudo netselect-apt -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">India</span>
