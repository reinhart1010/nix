---
layout: page
title: linux/hdparm (English)
description: "Get and set SATA and IDE hard drive parameters."
content_hash: b7c6e2d6c59a055df78cf66f4a2c52933865c31b
last_modified_at: 2024-06-11
tldri18n_status: 2
---
# hdparm

Get and set SATA and IDE hard drive parameters.
More information: <https://manned.org/hdparm>.

- Request the identification info of a given device:

`sudo hdparm -I `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/device</span>

- Get the Advanced Power Management level:

`sudo hdparm -B `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/device</span>

- Set the Advanced Power Management value (values 1-127 permit spin-down, and values 128-254 do not):

`sudo hdparm -B `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/device</span>

- Display the device's current power mode status:

`sudo hdparm -C `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/device</span>

- Force a drive to immediately enter standby mode (usually causes a drive to spin down):

`sudo hdparm -y `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/device</span>

- Put the drive into idle (low-power) mode, also setting its standby timeout:

`sudo hdparm -S `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">standby_timeout</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">device</span>

- Test the read speed of a specific device:

`sudo hdparm -tT `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">device</span>
