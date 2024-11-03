---
layout: page
title: common/pio-account (한국어)
description: "명령줄에서 PlatformIO 계정을 관리."
content_hash: 98ff5ce9d405fe543f519a7cc5c281527f64b2b4
last_modified_at: 2024-11-03
related_topics:
  - title: English version
    url: /en/common/pio-account.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/pio-account.html
    icon: bi bi-globe
tldri18n_status: 2
---
# pio account

명령줄에서 PlatformIO 계정을 관리.
더 많은 정보: <https://docs.platformio.org/en/latest/core/userguide/account/>.

- 새 PlatformIO 계정 등록:

`pio account register --username `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">사용자이름</span>` --email `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">이메일</span>` --password `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">비밀번호</span>` --firstname `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">이름</span>` --lastname `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">성</span>

- PlatformIO 계정 및 관련 데이터 영구 삭제:

`pio account destroy`

- PlatformIO 계정에 로그인:

`pio account login --username `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">사용자이름</span>` --password `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">비밀번호</span>

- PlatformIO 계정에서 로그아웃:

`pio account logout`

- PlatformIO 프로필 업데이트:

`pio account update --username `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">사용자이름</span>` --email `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">이메일</span>` --firstname `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">이름</span>` --lastname `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">성</span>` --current-password `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">비밀번호</span>

- PlatformIO 계정에 대한 자세한 정보 표시:

`pio account show`

- 사용자 이름이나 이메일을 사용하여 비밀번호 재설정:

`pio account forgot --username `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">사용자이름_또는_이메일</span>
