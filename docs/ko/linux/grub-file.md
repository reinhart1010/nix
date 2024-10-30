---
layout: page
title: linux/grub-file (한국어)
description: "파일이 부팅 가능한 이미지 유형인지 확인."
content_hash: 27d4872ef4603b1f1f0baa70d6859df430dec9ae
last_modified_at: 2024-10-30
related_topics:
  - title: English version
    url: /en/linux/grub-file.html
    icon: bi bi-globe
tldri18n_status: 2
---
# grub-file

파일이 부팅 가능한 이미지 유형인지 확인.
더 많은 정보: <https://manned.org/grub-file>.

- 파일이 ARM EFI 이미지인지 확인:

`grub-file --is-arm-efi `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- 파일이 i386 EFI 이미지인지 확인:

`grub-file --is-i386-efi `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- 파일이 x86_64 EFI 이미지인지 확인:

`grub-file --is-x86_64-efi `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- 파일이 ARM 이미지(Linux 커널)인지 확인:

`grub-file --is-arm-linux `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- 파일이 x86 이미지(Linux 커널)인지 확인:

`grub-file --is-x86-linux `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- 파일이 x86_64 XNU 이미지(macOS 커널)인지 확인:

`grub-file --is-x86_64-xnu `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>
