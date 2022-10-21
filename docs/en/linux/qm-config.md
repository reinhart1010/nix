---
layout: page
title: linux/qm-config (English)
description: "Display the virtual machine configuration with pending configuration changes applied."
content_hash: dba70677ab8face07f4b37dbff943bc6291ddafb
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># qm config

Display the virtual machine configuration with pending configuration changes applied.
More information: <https://pve.proxmox.com/pve-docs/qm.1.html>.

- Display the virtual machine configuration:

`qm config `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">vm_id</span>

- Display the current configuration values instead of pending values for the virtual machine:

`qm config --current `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">true</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">vm_id</span>

- Fetch the configuration values from the given snapshot:

`qm config --snapshot `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">snapshot_name</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">vm_id</span>
