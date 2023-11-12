---
layout: page
title: linux/deluser (한국어)
description: "유저 계정 제거 또는 그룹으로부터 사용자 제거."
content_hash: b6ee3a3f47788133172a44b724d8f5c82942b24f
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/linux/deluser.html
    icon: bi bi-globe
  - title: français version
    url: /fr/linux/deluser.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/linux/deluser.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># deluser

유저 계정 제거 또는 그룹으로부터 사용자 제거.
더 많은 정보: <https://manpages.debian.org/latest/adduser/deluser.html>.

- 유저 삭제:

`deluser `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">이름</span>

- 사용자의 홈 디렉토리 및 메일 스풀과 함께 사용자 제거:

`deluser -r `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">이름</span>

- 그룹으로부터 사용자 제거:

`deluser `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">이름</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">그룹</span>
