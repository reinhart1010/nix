---
layout: page
title: osx/kmutil (English)
description: "Utility for managing kernel extensions (kexts) and kext collections on disk."
content_hash: 64aadae07ef6542e0760a9987860fc348f481e0e
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# kmutil

Utility for managing kernel extensions (kexts) and kext collections on disk.
More information: <https://keith.github.io/xcode-man-pages/kmutil.8.html>.

- Find kexts available on the operating system:

`kmutil find`

- Display logging information about the Kernel Management sub-system:

`kmutil log`

- Inspect and display a kext collection's contents according to the options provided:

`kmutil inspect `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">options</span>

- Check the consistency of kext collections against each other:

`kmutil check`

- Dump kernelmanagerd state for debugging:

`sudo kmutil dumpstate`

- Load one or more extensions based on the bundle specified at this path in the results:

`kmutil load --bundle-path `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/extension.kext</span>
