---
layout: page
title: common/idevicecrashreport (English)
description: "Retrieve crash reports from an iOS device."
content_hash: 517b1abd4f1b45790e203c0c268f66e6e4b19dcb
last_modified_at: 2024-10-31
tldri18n_status: 2
---
# idevicecrashreport

Retrieve crash reports from an iOS device.
More information: <https://manned.org/idevicecrashreport>.

- Retrieve crash reports and move them to a specified directory:

`idevicecrashreport `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>

- Retrieve crash reports without removing them from the device:

`idevicecrashreport --keep `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>

- Extract crash reports into separate `.crash` files:

`idevicecrashreport --extract `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>
