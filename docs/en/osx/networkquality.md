---
layout: page
title: osx/networkquality (English)
description: "Measure the network quality by connecting to the internet."
content_hash: ea4db4fffd54dc88df965de04fb3311b8a2093fb
last_modified_at: 2024-11-08
tldri18n_status: 2
---
# networkQuality

Measure the network quality by connecting to the internet.
More information: <https://support.apple.com/101942>.

- Test the network quality for the default interface:

`networkQuality`

- Test the upload and download speeds sequentially instead of in parallel:

`networkQuality -s`

- Test a specified network interface:

`networkQuality -I `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">en0</span>

- Test the network quality with verbose output:

`networkQuality -v`
