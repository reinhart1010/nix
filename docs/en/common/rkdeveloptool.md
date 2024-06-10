---
layout: page
title: common/rkdeveloptool (English)
description: "Flash, dump, and manage boot firmware for Rockchip-based computer devices."
content_hash: 02cf9ad171b98f08f2ab167ecbcd85e702acd9a5
last_modified_at: 2024-06-10
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/rkdeveloptool.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># rkdeveloptool

Flash, dump, and manage boot firmware for Rockchip-based computer devices.
You will need to turn on the device into Maskrom/Bootrom mode before connecting it through USB.
Some subcommands may require to run as root.
More information: <https://github.com/rockchip-linux/rkdeveloptool>.

- [l]ist all connected Rockchip-based flash [d]evices:

`rkdeveloptool ld`

- Initialize the device by forcing it to [d]ownload and install the [b]ootloader from the specified file:

`rkdeveloptool db `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/bootloader.bin</span>

- [u]pdate the boot[l]oader software with a new one:

`rkdeveloptool ul `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/bootloader.bin</span>

- Write an image to a GPT-formatted flash partition, specifying the initial storage sector (usually `0x0` alias `0`):

`rkdeveloptool wl `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">initial_sector</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/image.img</span>

- Write to the flash partition by its user-friendly name:

`rkdeveloptool wlx `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">partition_name</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/image.img</span>

- [r]eset/reboot the [d]evice, exit from the Maskrom/Bootrom mode to boot into the selected flash partition:

`rkdeveloptool rd`
