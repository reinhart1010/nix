---
layout: page
title: common/dirs (한국어)
description: "디렉토리 스택을 표시하거나 조작한다."
content_hash: 25ed1f3ce0f2eedd936f71da6c2341c6c16b6b93
related_topics:
  - title: Deutsch version
    url: /de/common/dirs.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/dirs.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/dirs.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/dirs.html
    icon: bi bi-globe
---
# dirs

디렉토리 스택을 표시하거나 조작한다.
디렉토리 스택은 `pushd`과 `popd` 명령어로 조작할 수 있는 최근 방문한 디렉토리의 목록이다.
더 많은 정보: <https://www.gnu.org/software/bash/manual/bash.html#Directory-Stack-Builtins>.

- 각각의 엔트리 사이에서 공백으로 디렉토리 스택을 표시하기:

`dirs`

- 하나의 엔트리에 하나의 라인으로 디렉토리 스택 표시하기:

`dirs -p`

- 0부터 시작하는 디렉토리 스택에 n번째 항만 표시하기:

`dirs +`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">N</span>

- 디렉토리 스택 초기화하기:

`dirs -c`
