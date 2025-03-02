---
layout: page
title: linux/mknod (한국어)
description: "블록 또는 문자 장치 특수 파일 생성."
content_hash: 6155b600d54916c0640f971c11352a556215a09e
last_modified_at: 2025-03-02
related_topics:
  - title: English version
    url: /en/linux/mknod.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/linux/mknod.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/mknod.html
    icon: bi bi-globe
tldri18n_status: 2
---
# mknod

블록 또는 문자 장치 특수 파일 생성.
더 많은 정보: <https://www.gnu.org/software/coreutils/manual/html_node/mknod-invocation.html>.

- 블록 장치 생성:

`sudo mknod `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/장치_파일</span>` b `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">주_장치_번호</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">부_장치_번호</span>

- 문자 장치 생성:

`sudo mknod `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/장치_파일</span>` c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">주_장치_번호</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">부_장치_번호</span>

- FIFO(큐) 장치 생성:

`sudo mknod `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/장치_파일</span>` p`

- 기본 SELinux 보안 컨텍스트로 장치 파일 생성:

`sudo mknod -Z `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/장치_파일</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">유형</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">주_장치_번호</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">부_장치_번호</span>
