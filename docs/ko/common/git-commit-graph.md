---
layout: page
title: common/git-commit-graph (한국어)
description: "Git commit-graph 파일을 작성하고 검증합니다."
content_hash: 4b96f4ed265a951a286bbd90c9755d08ddf1531d
last_modified_at: 2024-08-23
related_topics:
  - title: English version
    url: /en/common/git-commit-graph.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/git-commit-graph.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/git-commit-graph.html
    icon: bi bi-globe
  - title: українська version
    url: /uk/common/git-commit-graph.html
    icon: bi bi-globe
tldri18n_status: 2
---
# git commit-graph

Git commit-graph 파일을 작성하고 검증합니다.
더 많은 정보: <https://git-scm.com/docs/git-commit-graph>.

- 저장소의 로컬 `.git` 디렉토리에 있는 모든 커밋들에 대한 commit-graph 파일 작성:

`git commit-graph write`

- 모든 브랜치와 태그에서 접근 가능한 커밋들을 포함하는 commit-graph 파일 작성:

`git show-ref --hash | git commit-graph write --stdin-commits`

- 현재 commit-graph 파일의 모든 커밋과 현재 `HEAD`에서 접근 가능한 커밋들을 포함하는 업데이트된 commit-graph 파일 작성:

`git rev-parse `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">HEAD</span>` | git commit-graph write --stdin-commits --append`
