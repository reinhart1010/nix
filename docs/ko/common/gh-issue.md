---
layout: page
title: common/gh-issue (한국어)
description: "GitHub 이슈 관리."
content_hash: 6b6887ad96a0115c9f54b684d7001c2ae2f3cbe9
last_modified_at: 2024-10-11
related_topics:
  - title: English version
    url: /en/common/gh-issue.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/gh-issue.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># gh issue

GitHub 이슈 관리.
더 많은 정보: <https://cli.github.com/manual/gh_issue>.

- 특정 이슈 보기:

`gh issue view `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">이슈_번호</span>

- 기본 웹 브라우저에서 특정 이슈 보기:

`gh issue view `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">이슈_번호</span>` --web`

- 기본 웹 브라우저에서 새 이슈 생성:

`gh issue create --web`

- `bug` 라벨이 있는 최근 10개의 이슈 나열:

`gh issue list --limit `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">10</span>` --label "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">bug</span>`"`

- 특정 사용자가 만든 닫힌 이슈 나열:

`gh issue list --state closed --author `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">사용자_명</span>

- 특정 저장소의 사용자와 관련된 이슈 상태 표시:

`gh issue status --repo `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">소유자</span>`/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">저장소</span>

- 특정 이슈 다시 열기:

`gh issue reopen `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">이슈_번호</span>
