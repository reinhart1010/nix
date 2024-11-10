---
layout: page
title: linux/kernel-install (한국어)
description: "커널 및 initrd 이미지를 `/boot`에 추가 및 제거."
content_hash: 0c12b96cbb1ee64484ee876fc477364517e0a179
last_modified_at: 2024-11-10
related_topics:
  - title: English version
    url: /en/linux/kernel-install.html
    icon: bi bi-globe
tldri18n_status: 2
---
# kernel-install

커널 및 initrd 이미지를 `/boot`에 추가 및 제거.
더 많은 정보: <https://manned.org/kernel-install.8>.

- 커널 및 initramfs 이미지를 부트로더 파티션에 추가:

`sudo kernel-install add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">커널-버전</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">커널-이미지</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/initrd-파일 ...</span>

- 부트로더 파티션에서 커널 제거:

`sudo kernel-install remove `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">커널-버전</span>

- 구성되거나 자동으로 감지된 다양한 경로와 매개변수 표시:

`sudo kernel-install inspect `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">커널-이미지</span>
