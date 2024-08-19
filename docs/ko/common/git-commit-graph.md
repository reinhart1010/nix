---
layout: page
title: common/git-commit-graph (한국어)
description: "Git commit-graph 파일을 작성하고 검증합니다."
content_hash: 955ca6251e4efc3c4070a0830ab8f53012c3e672
last_modified_at: 2024-08-19
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
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/git-commit-graph.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># git commit-graph

Git commit-graph 파일을 작성하고 검증합니다.
더 자세한 정보: <https://git-scm.com/docs/git-commit-graph>.

- 저장소의 로컬 `.git` 디렉토리에 있는 모든 커밋들에 대한 commit-graph 파일 작성:

`git commit-graph write`

- 모든 브랜치와 태그에서 접근 가능한 커밋들을 포함하는 commit-graph 파일 작성:

`git show-ref --hash | git commit-graph write --stdin-commits`

- 현재 commit-graph 파일의 모든 커밋과 현재 `HEAD`에서 접근 가능한 커밋들을 포함하는 업데이트된 commit-graph 파일 작성:

`git rev-parse `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">HEAD</span>` | git commit-graph write --stdin-commits --append`
