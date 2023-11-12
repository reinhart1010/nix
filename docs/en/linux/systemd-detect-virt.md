---
layout: page
title: linux/systemd-detect-virt (English)
description: "Detect execution in a virtualized environment."
content_hash: e585ff3c1fe99f79ac66bd9166be06542e4decb6
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# systemd-detect-virt

Detect execution in a virtualized environment.
More information: <https://www.freedesktop.org/software/systemd/man/systemd-detect-virt.html>.

- List detectable virtualization technologies:

`systemd-detect-virt --list`

- Detect virtualization, print the result and return a zero status code when running in a VM or a container, and a non-zero code otherwise:

`systemd-detect-virt`

- Silently check without printing anything:

`systemd-detect-virt --quiet`

- Only detect container virtualization:

`systemd-detect-virt --container`

- Only detect hardware virtualization:

`systemd-detect-virt --vm`
