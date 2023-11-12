---
layout: page
title: common/dd (English)
description: "Convert and copy a file."
content_hash: ddf69d2291353d0143e3f75e5ae8274fb8c39ddd
last_modified_at: 2023-11-12
related_topics:
  - title: Deutsch version
    url: /de/common/dd.html
    icon: bi bi-globe
  - title: فارسی version
    url: /fa/common/dd.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/dd.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/dd.html
    icon: bi bi-globe
tldri18n_status: 2
---
# dd

Convert and copy a file.
More information: <https://www.gnu.org/software/coreutils/dd>.

- Make a bootable USB drive from an isohybrid file (such like `archlinux-xxx.iso`):

`dd if=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.iso</span>` of=/dev/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">usb_drive</span>

- Clone a drive to another drive with 4 MiB block and ignore error:

`dd if=/dev/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">source_drive</span>` of=/dev/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">dest_drive</span>` bs=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">4194304</span>` conv=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">noerror</span>

- Generate a file of 100 random bytes by using kernel random driver:

`dd if=/dev/urandom of=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/random_file</span>` bs=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">100</span>` count=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1</span>

- Benchmark the write performance of a disk:

`dd if=/dev/zero of=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file_1GB</span>` bs=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1024</span>` count=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1000000</span>

- Generate a system backup into an IMG file:

`dd if=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/drive_device</span>` of=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.img</span>

- Restore a drive from an IMG file:

`dd if=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.img</span>` of=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/drive_device</span>
