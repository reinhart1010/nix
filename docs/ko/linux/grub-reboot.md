---
layout: page
title: linux/grub-reboot (한국어)
description: "다음 부팅에만 적용되는 GRUB의 기본 부팅 항목 설정."
content_hash: 40d8d95bf4a7fed0c15f4d426661c5c8945ad98e
last_modified_at: 2024-10-30
related_topics:
  - title: English version
    url: /en/linux/grub-reboot.html
    icon: bi bi-globe
tldri18n_status: 2
---
# grub-reboot

다음 부팅에만 적용되는 GRUB의 기본 부팅 항목 설정.
더 많은 정보: <https://manned.org/grub-reboot>.

- 다음 부팅을 위해 기본 부팅 항목을 항목 번호, 이름 또는 식별자로 설정:

`sudo grub-reboot `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">항목_번호</span>

- 다음 부팅을 위해 대체 부팅 디렉토리의 항목 번호, 이름 또는 식별자로 기본 부팅 항목 설정:

`sudo grub-reboot --boot-directory `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/경로/대상/부팅_디렉토리</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">항목_번호</span>
