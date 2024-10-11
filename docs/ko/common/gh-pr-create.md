---
layout: page
title: common/gh-pr-create (한국어)
description: "GitHub 풀 리퀘스트 관리."
content_hash: 1109908a9b3ee6b1efea1cd0321e0f2501747141
last_modified_at: 2024-10-11
related_topics:
  - title: English version
    url: /en/common/gh-pr-create.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/gh-pr-create.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># gh pr create

GitHub 풀 리퀘스트 관리.
더 많은 정보: <https://cli.github.com/manual/gh_pr_create>.

- 대화형으로 풀 리퀘스트 생성:

`gh pr create`

- 현재 브랜치의 커밋 메시지에서 제목과 설명을 결정하여 풀 리퀘스트 생성:

`gh pr create --fill`

- 드래프트 풀 리퀘스트 생성:

`gh pr create --draft`

- 베이스 브랜치, 제목 및 설명을 지정하여 풀 리퀘스트 생성:

`gh pr create --base `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">베이스_브랜치</span>` --title "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">제목</span>`" --body "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">본문</span>`"`

- 기본 웹 브라우저에서 풀 리퀘스트 열기 시작:

`gh pr create --web`
