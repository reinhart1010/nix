---
layout: page
title: common/git-mktree (한국어)
description: "`ls-tree` 형식의 텍스트를 사용하여 트리 객체를 생성합니다."
content_hash: 1b08da263334c5787cc71490ae26679b3972ff03
last_modified_at: 2024-10-08
related_topics:
  - title: English version
    url: /en/common/git-mktree.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/git-mktree.html
    icon: bi bi-globe
tldri18n_status: 2
---
# git mktree

`ls-tree` 형식의 텍스트를 사용하여 트리 객체를 생성합니다.
더 많은 정보: <https://git-scm.com/docs/git-mktree>.

- 트리 객체를 생성하고 각 트리 항목의 해시가 기존 객체를 식별하는지 확인:

`git mktree`

- 누락된 객체 허용:

`git mktree --missing`

- 트리 객체의 NUL([z]ero character)로 종료된 출력을 읽기 (`ls-tree -z`):

`git mktree -z`

- 여러 트리 객체 생성 허용:

`git mktree --batch`

- `stdin`에서 정렬하여 트리 생성 (비재귀 `git ls-tree` 출력 형식 필요):

`git mktree < `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/tree.txt</span>
