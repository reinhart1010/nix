---
layout: page
title: osx/dd (English)
description: "Convert and copy a file."
content_hash: 47607cf9048ca4e4268058255f410bd7685d093d
last_modified_at: 2024-06-10
related_topics:
  - title: español version
    url: /es/osx/dd.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/osx/dd.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/osx/dd.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/osx/dd.html
    icon: bi bi-globe
tldri18n_status: 2
---
# dd

Convert and copy a file.
More information: <https://keith.github.io/xcode-man-pages/dd.1.html>.

- Make a bootable USB drive from an isohybrid file (such like `archlinux-xxx.iso`) and show the progress:

`dd if=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.iso</span>` of=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/usb_drive</span>` status=progress`

- Clone a drive to another drive with 4 MB block, ignore error and show the progress:

`dd bs=4m conv=noerror if=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/source_drive</span>` of=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/dest_drive</span>` status=progress`

- Generate a file with a specific number of random bytes by using kernel random driver:

`dd bs=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">100</span>` count=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1</span>` if=/dev/urandom of=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/random_file</span>

- Benchmark the write performance of a disk:

`dd bs=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1024</span>` count=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1000000</span>` if=/dev/zero of=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/1GB_file</span>

- Create a system backup, save it into an IMG file (can be restored later by swapping `if` and `of`), and show the progress:

`dd if=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/drive_device</span>` of=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.img</span>` status=progress`

- Check the progress of an ongoing `dd` operation (run this command from another shell):

`kill -USR1 $(pgrep ^dd)`
