---
layout: page
title: common/git-stash (한국어)
description: "로컬 Git 변경사항을 임시 영역에 저장합니다."
content_hash: f4c6ecc81bf7d4e1b6ed8942f0ef565f397b854c
last_modified_at: 2024-08-20
related_topics:
  - title: English version
    url: /en/common/git-stash.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/git-stash.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/git-stash.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/git-stash.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/git-stash.html
    icon: bi bi-globe
tldri18n_status: 2
---
# git stash

로컬 Git 변경사항을 임시 영역에 저장합니다.
더 자세한 정보: <https://git-scm.com/docs/git-stash>.

- 새롭게 생성한 (Git에서 관리하지 않는) 파일을 제외하고 현재 변경사항을 메시지와 함께 임시 저장:

`git stash push --message `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">optional_stash_message</span>

- 새롭게 생성한 (Git에서 관리하지 않는) 파일을 포함하여 현재 변경사항을 임시 저장:

`git stash --include-untracked`

- 변경된 파일들의 특정 부분만 선택하여 임시 저장 (대화형 프롬프트):

`git stash --patch`

- 모든 임시 저장 목록 표시 (임시 저장 이름, 관련 브랜치 및 메시지 표시):

`git stash list`

- 임시 저장(기본값은 `stash@{0}`)과 해당 임시 저장이 생성된 시점의 커밋 사이의 변경 사항을 터미널에 상세히 표시:

`git stash show --patch `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">stash@{0}</span>

- 임시 저장 적용 (기본값은 가장 최근 임시 저장인 stash@{0}):

`git stash apply `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">optional_stash_name_or_commit</span>

- 임시 저장을 적용하고 (기본값은 stash@{0}), 적용 시 충돌이 없으면 임시 저장 목록에서 제거:

`git stash pop `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">optional_stash_name</span>

- 모든 임시 저장 삭제:

`git stash clear`
