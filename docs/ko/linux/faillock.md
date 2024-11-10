---
layout: page
title: linux/faillock (한국어)
description: "인증 실패 기록 파일을 표시하고 수정합니다."
content_hash: 0a0986c86daa5e2191c2813b471a44a359d9b806
last_modified_at: 2024-11-10
related_topics:
  - title: English version
    url: /en/linux/faillock.html
    icon: bi bi-globe
tldri18n_status: 2
---
# faillock

인증 실패 기록 파일을 표시하고 수정합니다.
더 많은 정보: <https://manned.org/faillock>.

- 현재 사용자의 로그인 실패 목록 표시:

`faillock`

- 현재 사용자의 실패 기록 초기화:

`faillock --reset`

- 모든 사용자의 로그인 실패 목록 표시:

`sudo faillock`

- 특정 사용자의 로그인 실패 목록 표시:

`sudo faillock --user `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">사용자</span>

- 특정 사용자의 실패 기록 초기화:

`sudo faillock --user `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">사용자</span>` --reset`
