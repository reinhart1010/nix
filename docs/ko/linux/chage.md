---
layout: page
title: linux/chage (한국어)
description: "사용자 계정 및 비밀번호 만료 정보를 변경합니다."
content_hash: cc222a0076f356c2bbcd277010df030146d95ec8
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/linux/chage.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/chage.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/chage.html
    icon: bi bi-globe
tldri18n_status: 2
---
# chage

사용자 계정 및 비밀번호 만료 정보를 변경합니다.
더 많은 정보: <https://manned.org/chage>.

- 사용자의 비밀번호 정보를 나열:

`chage --list `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">사용자명</span>

- 비밀번호 만료를 10일 후로 설정:

`sudo chage --maxdays `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">10</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">사용자명</span>

- 비밀번호 만료 비활성화:

`sudo chage --maxdays `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">사용자명</span>

- 계정 만료 날짜 설정:

`sudo chage --expiredate `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">YYYY-MM-DD</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">사용자명</span>

- 다음 로그인 시 비밀번호 변경을 강제:

`sudo chage --lastday `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">0</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">사용자명</span>
