---
layout: page
title: linux/mkhomedir_helper (한국어)
description: "사용자 생성 후 사용자의 홈 디렉토리를 만듭니다."
content_hash: 66928506cfff47a12978ca39c74c9d05a91a3399
last_modified_at: 2024-11-10
related_topics:
  - title: English version
    url: /en/linux/mkhomedir_helper.html
    icon: bi bi-globe
tldri18n_status: 2
---
# mkhomedir_helper

사용자 생성 후 사용자의 홈 디렉토리를 만듭니다.
더 많은 정보: <https://manned.org/mkhomedir_helper>.

- umask 022로 `/etc/skel`을 기반으로 사용자 홈 디렉토리 생성:

`sudo mkhomedir_helper `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">사용자명</span>

- 소유자에게 모든 권한(0)을, 그룹에게 읽기 권한(3)을 부여한 umask 037로 `/etc/skel`을 기반으로 사용자 홈 디렉토리 생성:

`sudo mkhomedir_helper `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">사용자명</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">037</span>

- 사용자 지정 스켈레톤을 기반으로 사용자 홈 디렉토리 생성:

`sudo mkhomedir_helper `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">사용자명</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">umask</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/스켈레톤_폴더</span>
