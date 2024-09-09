---
layout: page
title: common/autojump (한국어)
description: "가장 자주 방문하는 디렉토리 사이를 빠르게 이동."
content_hash: b666000b4ce32f8e3779db8b85e09c68a550dc1a
last_modified_at: 2024-09-09
related_topics:
  - title: English version
    url: /en/common/autojump.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/autojump.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/autojump.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/autojump.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/autojump.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/autojump.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># autojump

가장 자주 방문하는 디렉토리 사이를 빠르게 이동.
j 또는 jc와 같은 별칭은 타이핑을 줄이기 위해 제공.
더 많은 정보: <https://github.com/wting/autojump>.

- 주어진 패턴이 포함된 디렉토리로 이동:

`j `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">패턴</span>

- 주어진 패턴이 포함된 현재 디렉토리의 하위 디렉토리(자식)로 이동:

`jc `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">패턴</span>

- 운영체제 파일 관리자에서 주어진 패턴이 포함된 디렉토리 열기:

`jo `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">패턴</span>

- 자동 점프 데이터베이스에서 존재하지 않는 디렉토리 제거:

`j --purge`

- 자동 점프 데이터베이스의 항목을 표시:

`j -s`
