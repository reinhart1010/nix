---
layout: page
title: windows/bcdboot (English)
description: "Configure or repair boot files."
content_hash: e21205690d264a66bb69b0f227ccf9edffc15565
last_modified_at: 2023-10-25
---
# bcdboot

Configure or repair boot files.
More information: <https://learn.microsoft.com/windows-hardware/manufacture/desktop/bcdboot-command-line-options-techref-di>.

- Initialize the system partition by using BCD files from the source Windows folder:

`bcdboot `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">C:\Windows</span>

- Enable [v]erbose mode:

`bcdboot `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">C:\Windows</span>` /v`

- Specify the volume letter of the [s]ystem partition:

`bcdboot `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">C:\Windows</span>` /s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">S:</span>

- Specify a [l]ocale:

`bcdboot `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">C:\Windows</span>` /l `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">en-us</span>

- Specify a [f]irmware type while copying the boot files to a specified volume:

`bcdboot `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">C:\Windows</span>` /s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">S:</span>` /f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">UEFI|BIOS|ALL</span>
