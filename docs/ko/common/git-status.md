---
layout: page
title: common/git-status (한국어)
description: "Git 저장소의 파일 변경 사항을 표시합니다."
content_hash: b4092890c3c0bcc25839ed5cbbd69cd102d91618
last_modified_at: 2024-10-08
related_topics:
  - title: Deutsch version
    url: /de/common/git-status.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/git-status.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/git-status.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/git-status.html
    icon: bi bi-globe
  - title: हिन्दी version
    url: /hi/common/git-status.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/git-status.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/git-status.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/git-status.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/git-status.html
    icon: bi bi-globe
  - title: українська version
    url: /uk/common/git-status.html
    icon: bi bi-globe
tldri18n_status: 2
---
# git status

Git 저장소의 파일 변경 사항을 표시합니다.
현재 체크아웃된 커밋과 비교하여 변경된, 추가된 및 삭제된 파일을 나열합니다.
더 많은 정보: <https://git-scm.com/docs/git-status>.

- 커밋할 파일로 아직 추가되지 않은 변경된 파일 보기:

`git status`

- [s]hort 형식으로 출력:

`git status --short`

- 스테이징 영역과 작업 디렉토리의 변경 사항에 대한 [v]erbose 정보 표시:

`git status --verbose --verbose`

- [b]ranch 및 추적 정보 표시:

`git status --branch`

- [s]hort 형식으로 출력하면서 [b]ranch 정보 표시:

`git status --short --branch`

- 현재 숨겨둔 엔트리의 수 표시:

`git status --show-stash`

- 출력에 추적되지 않는 파일을 표시하지 않기:

`git status --untracked-files=no`
