---
layout: page
title: linux/ledctl (English)
description: "Intel(R) Enclosure LED Control Application."
content_hash: 11fbe1e5205ad1147c44f9781a2b1cb94200a846
---
# ledctl

Intel(R) Enclosure LED Control Application.
More information: <https://manned.org/ledctl>.

- Turn on the "Locate" LED for specified device(s):

`sudo ledctl locate=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sda,/dev/sdb,...</span>

- Turn off the "Locate" LED for specified device(s):

`sudo ledctl locate_off=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sda,/dev/sdb,...</span>

- Turn off the "Status" LED and "Failure" LED for specified device(s):

`sudo ledctl off=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sda,/dev/sdb,...</span>

- Turn off the "Status" LED, "Failure" LED and "Locate" LED for specified device(s):

`sudo ledctl normal=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sda,/dev/sdb,...</span>
