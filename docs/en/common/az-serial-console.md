---
layout: page
title: common/az-serial-console (English)
description: "Connect to the serial console of a Virtual Machine."
content_hash: df170285c9ede85f0dbfd3d859e3c562c2a816a6
last_modified_at: 2024-09-16
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/az-serial-console.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># az serial-console

Connect to the serial console of a Virtual Machine.
Part of `azure-cli` (also known as `az`).
More information: <https://learn.microsoft.com/cli/azure/serial-console>.

- Connect to a serial console:

`az serial-console connect --resource-group `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Resource_Group_Name</span>` --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Virtual_Machine_Name</span>

- Terminate the connection:

`<Ctrl>-]`
