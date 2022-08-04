---
layout: page
title: linux/hdparm (English)
description: "Get and set SATA and IDE hard drive parameters."
content_hash: f8273d2843521f56cd347a97378f90e3231b8896
---
# hdparm

Get and set SATA and IDE hard drive parameters.
More information: <https://manned.org/hdparm>.

- Request the identification info of a given device:

`sudo hdparm -I /dev/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">device</span>

- Get the Advanced Power Management level:

`sudo hdparm -B /dev/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">device</span>

- Set the Advanced Power Management value (values 1-127 permit spin-down, and values 128-254 do not):

`sudo hdparm -B `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1</span>` /dev/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">device</span>

- Display the device's current power mode status:

`sudo hdparm -C /dev/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">device</span>

- Force a drive to immediately enter standby mode (usually causes a drive to spin down):

`sudo hdparm -y /dev/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">device</span>

- Put the drive into idle (low-power) mode, also setting its standby timeout:

`sudo hdparm -S `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">standby_timeout</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">device</span>
