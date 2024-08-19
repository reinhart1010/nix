---
layout: page
title: common/git-ls-tree (한국어)
description: "트리 객체의 파일과 디렉토리 목록을 보여줍니다."
content_hash: eaf3a073452e6dad07b32d11f3017be4eeff3149
last_modified_at: 2024-08-19
related_topics:
  - title: English version
    url: /en/common/git-ls-tree.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/git-ls-tree.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/git-ls-tree.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/git-ls-tree.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/git-ls-tree.html
    icon: bi bi-globe
tldri18n_status: 2
---
# git ls-tree

트리 객체의 파일과 디렉토리 목록을 보여줍니다.
더 많은 정보: <https://git-scm.com/docs/git-ls-tree>.

- 특정 브랜치의 파일과 디렉토리 목록 보기:

`git ls-tree `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">브랜치_이름</span>

- 특정 커밋의 파일과 디렉토리 목록을 하위 디렉토리까지 재귀적으로 보기:

`git ls-tree -r `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">커밋_해시</span>

- 특정 커밋의 파일 이름만 보기:

`git ls-tree --name-only `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">커밋_해시</span>

- 현재 브랜치의 최신 상태 파일과 디렉토리 목록을 트리 구조로 출력하기 (참고: `tree --fromfile`은 Windows에서 지원되지 않음):

`git ls-tree -r --name-only HEAD | tree --fromfile`
