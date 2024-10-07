---
layout: page
title: common/git-squash (한국어)
description: "여러 커밋을 하나의 커밋으로 합치기."
content_hash: eebe7cbb8931e56fece98f5c832f6b52496b2237
last_modified_at: 2024-10-07
related_topics:
  - title: English version
    url: /en/common/git-squash.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/git-squash.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># git squash

여러 커밋을 하나의 커밋으로 합치기.
`git-extras`의 일부.
더 많은 정보: <https://github.com/tj/git-extras/blob/master/Commands.md#git-squash>.

- 특정 브랜치의 모든 커밋을 현재 브랜치에 하나의 커밋으로 합치기:

`git squash `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">source_branch</span>

- 현재 브랜치에서 특정 커밋부터 시작하는 모든 커밋을 합치기:

`git squash `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">commit</span>

- 최근 `n`개의 커밋을 합치고 메시지와 함께 커밋:

`git squash HEAD~`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">n</span>` "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">메시지</span>`"`

- 최근 `n`개의 커밋을 합치고 모든 개별 메시지를 연결하여 커밋:

`git squash --squash-msg HEAD~`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">n</span>
