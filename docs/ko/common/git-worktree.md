---
layout: page
title: common/git-worktree (한국어)
description: "동일한 저장소에 연결된 여러 작업 트리를 관리."
content_hash: 6056a6a9a68332bd2a9e3e9d9ff8f99648103626
last_modified_at: 2024-10-08
related_topics:
  - title: English version
    url: /en/common/git-worktree.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/git-worktree.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/git-worktree.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/git-worktree.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/git-worktree.html
    icon: bi bi-globe
tldri18n_status: 2
---
# git worktree

동일한 저장소에 연결된 여러 작업 트리를 관리.
더 많은 정보: <https://git-scm.com/docs/git-worktree>.

- 지정된 브랜치가 체크아웃된 새 디렉터리 생성:

`git worktree add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/폴더</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">브랜치</span>

- 새로운 브랜치가 체크아웃된 새 디렉터리 생성:

`git worktree add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/폴더</span>` -b `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">새_브랜치</span>

- 이 저장소에 연결된 모든 작업 디렉터리 나열:

`git worktree list`

- 작업 트리 제거 (작업 트리 디렉터리 삭제 후):

`git worktree prune`
