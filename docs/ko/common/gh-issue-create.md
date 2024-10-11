---
layout: page
title: common/gh-issue-create (한국어)
description: "저장소에 GitHub 이슈 생성."
content_hash: 279a6c19688d54a85b3765ea601a87ac442b8cab
last_modified_at: 2024-10-11
related_topics:
  - title: English version
    url: /en/common/gh-issue-create.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/gh-issue-create.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># gh issue create

저장소에 GitHub 이슈 생성.
더 많은 정보: <https://cli.github.com/manual/gh_issue_create>.

- 현재 저장소에 대해 대화식으로 새 이슈 생성:

`gh issue create`

- `bug` 레이블을 사용하여 대화식으로 새 이슈 생성:

`gh issue create --label "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">bug</span>`"`

- 지정된 사용자에게 할당하여 대화식으로 새 이슈 생성:

`gh issue create --assignee `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">user1,user2,...</span>

- 제목과 본문을 지정하고 현재 사용자에게 할당하여 새 이슈 생성:

`gh issue create --title "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">제목</span>`" --body "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">본문</span>`" --assignee "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">@me</span>`"`

- 파일에서 본문 텍스트를 읽어와 대화식으로 새 이슈 생성:

`gh issue create --body-file `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- 기본 웹 브라우저에서 새 이슈 생성:

`gh issue create --web`

- 도움말 표시:

`gh issue create --help`
