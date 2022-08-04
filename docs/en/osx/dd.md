---
layout: page
title: osx/dd (English)
description: "Convert and copy a file."
content_hash: c30688ad44a6534fb746bb1d021f5c122ac2eec8
related_topics:
  - title: 中文 version
    url: /zh/osx/dd.html
    icon: bi bi-globe
---
# dd

Convert and copy a file.
More information: <https://ss64.com/osx/dd.html>.

- Make a bootable USB drive from an isohybrid file (such like `archlinux-xxx.iso`):

`dd if=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file.iso</span>` of=/dev/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">usb_drive</span>

- Clone a drive to another drive with 4 MB block and ignore error:

`dd if=/dev/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">source_drive</span>` of=/dev/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">dest_drive</span>` bs=4m conv=noerror`

- Generate a file of 100 random bytes by using kernel random driver:

`dd if=/dev/urandom of=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">random_file</span>` bs=100 count=1`

- Benchmark the write performance of a disk:

`dd if=/dev/zero of=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file_1GB</span>` bs=1024 count=1000000`
