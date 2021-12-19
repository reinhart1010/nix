---
layout: page
title: linux/nethogs (English)
description: "Monitor bandwidth usage per process."
content_hash: 8dbbf7ca303e6a6b66c2bddc41ac752b24c0a03b
---
# nethogs

Monitor bandwidth usage per process.
More information: <https://github.com/raboof/nethogs>.

- Start nethogs as root (default device is eth0):

`sudo nethogs`

- Monitor bandwidth on specific device:

`sudo nethogs `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">device</span>

- Monitor bandwidth on multiple devices:

`sudo nethogs `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">device1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">device2</span>

- Specify refresh rate:

`sudo nethogs -t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">seconds</span>
