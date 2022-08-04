---
layout: page
title: linux/ddrescue (English)
description: "Data recovery tool that reads data from damaged block devices."
content_hash: ae2431f19d36d82c0e8873927c34d715253f73f2
---
# ddrescue

Data recovery tool that reads data from damaged block devices.
More information: <https://www.gnu.org/software/ddrescue/>.

- Take an image of a device, creating a log file:

`sudo ddrescue `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sdb</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/image.dd</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/log.txt</span>

- Clone Disk A to Disk B, creating a log file:

`sudo ddrescue --force --no-scrape `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sdX</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sdY</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/log.txt</span>
