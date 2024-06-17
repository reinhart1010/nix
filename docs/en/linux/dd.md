---
layout: page
title: linux/dd (English)
description: "Convert and copy a file."
content_hash: 042cff69be2edeed57bf307bb4d2f239fba71707
last_modified_at: 2024-06-17
related_topics:
  - title: فارسی version
    url: /fa/linux/dd.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/linux/dd.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/linux/dd.html
    icon: bi bi-globe
tldri18n_status: 2
---
# dd

Convert and copy a file.
More information: <https://www.gnu.org/software/coreutils/dd>.

- Make a bootable USB drive from an isohybrid file (such as `archlinux-xxx.iso`) and show the progress:

`dd if=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.iso</span>` of=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/usb_drive</span>` status=progress`

- Clone a drive to another drive with 4 MiB block size and flush writes before the command terminates:

`dd bs=4M conv=fsync if=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/source_drive</span>` of=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/dest_drive</span>

- Generate a file with a specific number of random bytes by using kernel random driver:

`dd bs=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">100</span>` count=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1</span>` if=/dev/urandom of=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/random_file</span>

- Benchmark the write performance of a disk:

`dd bs=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1M</span>` count=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1024</span>` if=/dev/zero of=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file_1GB</span>

- Create a system backup, save it into an IMG file (can be restored later by swapping `if` and `of`), and show the progress:

`dd if=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/drive_device</span>` of=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.img</span>` status=progress`

- Check the progress of an ongoing `dd` operation (run this command from another shell):

`kill -USR1 $(pgrep -x dd)`
