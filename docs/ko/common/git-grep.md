---
layout: page
title: common/git-grep (한국어)
description: "저장소의 히스토리에서 파일 내의 문자열을 찾습니다."
content_hash: 27e36607ced806f9895bd4232ec95bb85f82d5cf
last_modified_at: 2024-06-13
related_topics:
  - title: English version
    url: /en/common/git-grep.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/git-grep.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/git-grep.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/git-grep.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/git-grep.html
    icon: bi bi-globe
tldri18n_status: 2
---
# git-grep

저장소의 히스토리에서 파일 내의 문자열을 찾습니다.
일반 `grep`과 같은 많은 플래그를 수용합니다.
더 많은 정보: <https://git-scm.com/docs/git-grep>.

- 추적된 파일에서 문자열 검색:

`git grep `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">검색_문자열</span>

- 추적된 파일 중 일치하는 패턴의 파일에서 문자열 검색:

`git grep `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">검색_문자열</span>` -- `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">파일_글로브_패턴</span>

- 서브모듈을 포함하여 추적된 파일에서 문자열 검색:

`git grep --recurse-submodules `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">검색_문자열</span>

- 특정 히스토리 지점에서 문자열 검색:

`git grep `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">검색_문자열</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">HEAD~2</span>

- 모든 브랜치에서 문자열 검색:

`git grep `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">검색_문자열</span>` $(git rev-list --all)`
