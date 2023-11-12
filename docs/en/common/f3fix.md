---
layout: page
title: common/f3fix (English)
description: "Edit the partition table of a fake flash drive."
content_hash: bea53b69f2ffd345f3b6b7a28ed6d822c49dfe6c
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# f3fix

Edit the partition table of a fake flash drive.
See also `f3probe`, `f3write`, `f3read`.
More information: <http://oss.digirati.com.br/f3/>.

- Fill a fake flash drive with a single partition that matches its real capacity:

`sudo f3fix `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/device_name</span>

- Mark the partition as bootable:

`sudo f3fix --boot `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/device_name</span>

- Specify the filesystem:

`sudo f3fix --fs-type=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">filesystem_type</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/device_name</span>
