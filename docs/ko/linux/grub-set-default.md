---
layout: page
title: linux/grub-set-default (한국어)
description: "GRUB의 기본 부트 항목 설정."
content_hash: fe79bebf33d0836683f44f0688b4839a2d162d64
last_modified_at: 2024-10-30
related_topics:
  - title: English version
    url: /en/linux/grub-set-default.html
    icon: bi bi-globe
tldri18n_status: 2
---
# grub-set-default

GRUB의 기본 부트 항목 설정.
더 많은 정보: <https://manned.org/grub-set-default>.

- 기본 부트 항목을 항목 번호, 이름 또는 식별자로 설정:

`sudo grub-set-default `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">항목_번호</span>

- 대체 부트 디렉토리에 대해 기본 부트 항목을 항목 번호, 이름 또는 식별자로 설정:

`sudo grub-set-default --boot-directory `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/경로/대상/부트_디렉토리</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">항목_번호</span>
