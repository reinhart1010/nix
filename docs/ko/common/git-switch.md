---
layout: page
title: common/git-switch (한국어)
description: "Git 브랜치 간 전환합니다. Git 버전 2.23+가 필요합니다."
content_hash: c552a16002571ee1a33a5f68aa3b9d5b0d560274
last_modified_at: 2024-06-13
related_topics:
  - title: Deutsch version
    url: /de/common/git-switch.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/git-switch.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/git-switch.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/git-switch.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/git-switch.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/git-switch.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/git-switch.html
    icon: bi bi-globe
tldri18n_status: 2
---
# git switch

Git 브랜치 간 전환합니다. Git 버전 2.23+가 필요합니다.
같이 보기: `git checkout`.
더 많은 정보: <https://git-scm.com/docs/git-switch>.

- 기존 브랜치로 전환:

`git switch `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">브랜치_이름</span>

- 새 브랜치를 만들고 전환:

`git switch --create `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">브랜치_이름</span>

- 기존 커밋을 기반으로 새 브랜치를 만들고 전환:

`git switch --create `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">브랜치_이름</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">커밋</span>

- 이전 브랜치로 전환:

`git switch -`

- 브랜치로 전환하고 모든 서브모듈을 일치하도록 업데이트:

`git switch --recurse-submodules `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">브랜치_이름</span>

- 브랜치로 전환하고 현재 브랜치와 미커밋된 변경 사항을 자동으로 병합:

`git switch --merge `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">브랜치_이름</span>
