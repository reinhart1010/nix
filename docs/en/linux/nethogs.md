---
layout: page
title: linux/nethogs (English)
description: "Monitor bandwidth usage per process."
content_hash: ed7f3725aeccc17afadcf58a4d647b3961dc8b2e
last_modified_at: 2023-06-28
---
# nethogs

Monitor bandwidth usage per process.
More information: <https://github.com/raboof/nethogs>.

- Start NetHogs as root (default device is `eth0`):

`sudo nethogs`

- Monitor bandwidth on specific device:

`sudo nethogs `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">device</span>

- Monitor bandwidth on multiple devices:

`sudo nethogs `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">device1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">device2</span>

- Specify refresh rate:

`sudo nethogs -t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">seconds</span>
