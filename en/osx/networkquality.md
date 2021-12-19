---
layout: page
title: osx/networkquality (English)
description: "Measure the network quality by connecting to the internet."
content_hash: 6804ea21c9967437e0ed022d3836e52ca70a562d
---
# networkQuality

Measure the network quality by connecting to the internet.
More information: <https://support.apple.com/HT212313>.

- Test the network quality for the default interface:

`networkQuality`

- Test the upload and download speeds sequentially instead of in parallel:

`networkQuality -s`

- Test a specified network interface:

`networkQuality -I `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">en0</span>

- Test the network quality with verbose output:

`networkQuality -v`
