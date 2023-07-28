---
layout: page
title: linux/usbip (English)
description: "Use USB devices remotely."
content_hash: e58072bdebeaa5894a34b3f3e1554b02ed439013
last_modified_at: 2023-07-28
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># usbip

Use USB devices remotely.
More information: <https://usbip.sourceforge.net>.

- List all local USB devices and their bus ID's:

`usbip list --local`

- Start a `usbip` daemon on the server:

`systemctl start usbipd`

- Bind a USB device to `usbip` on the server:

`sudo usbip bind --busid=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">bus_id</span>

- Load the kernel module required by `usbip` on the client:

`sudo modprobe vhci-hcd`

- Attach to the `usbip` device on the client (bus ID is the same as on the server):

`sudo usbip attach -r `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ip_address</span>` --busid=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">bus_id</span>

- List attached devices:

`usbip port`

- Detach from a device:

`sudo usbip detach --port=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">port</span>

- Unbind a device:

`usbip unbind --busid=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">bus_id</span>
