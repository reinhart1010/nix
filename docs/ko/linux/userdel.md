---
layout: page
title: linux/userdel (한국어)
description: "사용자 계정을 삭제하거나 사용자를 그룹에서 제거합니다."
content_hash: 9cfe722c4bc98e79ef6e26868c6e70073c3f2cca
last_modified_at: 2024-11-10
related_topics:
  - title: català version
    url: /ca/linux/userdel.html
    icon: bi bi-globe
  - title: English version
    url: /en/linux/userdel.html
    icon: bi bi-globe
  - title: español version
    url: /es/linux/userdel.html
    icon: bi bi-globe
  - title: français version
    url: /fr/linux/userdel.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/linux/userdel.html
    icon: bi bi-globe
tldri18n_status: 2
---
# userdel

사용자 계정을 삭제하거나 사용자를 그룹에서 제거합니다.
같이 보기: `users`, `useradd`, `usermod`.
더 많은 정보: <https://manned.org/userdel>.

- 사용자 삭제:

`sudo userdel `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">사용자명</span>

- 다른 루트 디렉토리에서 사용자 삭제:

`sudo userdel `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-R|--root</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/다른/루트</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">사용자명</span>

- 홈 디렉토리 및 메일 스풀과 함께 사용자 삭제:

`sudo userdel `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-r|--remove</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">사용자명</span>
