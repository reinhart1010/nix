---
layout: page
title: windows/bcdboot (English)
description: "A system utility to configure or repair boot files."
content_hash: e7e2a8ae418438b36fa77fc576b4e7abb89db1db
last_modified_at: 2023-10-18
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># bcdboot

A system utility to configure or repair boot files.
More information: <https://learn.microsoft.com/en-us/windows-hardware/manufacture/desktop/bcdboot-command-line-options-techref-di>.

- Initialize the system partition by using BCD files from the source Windows folder:

`bcdboot `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">C:\Windows</span>

- Enable verbose mode:

`bcdboot `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">C:\Windows</span>` /v`

- Specify the volume letter of the system partition:

`bcdboot `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">C:\Windows</span>` /s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">S:</span>

- Specify a locale:

`bcdboot `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">C:\Windows</span>` /l `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">en-us</span>

- Specify a firmware type while copying the boot files to a specified volume:

`bcdboot `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">C:\Windows</span>` /s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">S:</span>` /f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">UEFI|BIOS|ALL</span>
