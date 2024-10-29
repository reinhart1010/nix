---
layout: page
title: linux/grub-install (한국어)
description: "GRUB을 장치에 설치."
content_hash: e182d4b5cc59b1b434d21b8257f702c4b65db877
last_modified_at: 2024-10-29
related_topics:
  - title: English version
    url: /en/linux/grub-install.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/grub-install.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/grub-install.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># grub-install

GRUB을 장치에 설치.
더 많은 정보: <https://www.gnu.org/software/grub/manual/grub/html_node/Installing-GRUB-using-grub_002dinstall.html>.

- BIOS 시스템에 GRUB 설치:

`grub-install --target=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">i386-pc</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/장치</span>

- UEFI 시스템에 GRUB 설치:

`grub-install --target=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">x86_64-efi</span>` --efi-directory=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/efi_폴더</span>` --bootloader-id=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">GRUB</span>

- 특정 모듈을 사전 로드하여 GRUB 설치:

`grub-install --target=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">x86_64-efi</span>` --efi-directory=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/efi_폴더</span>` --modules="`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">part_gpt part_msdos</span>`"`
