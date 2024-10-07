---
layout: page
title: common/git-cp (한국어)
description: "기존 파일을 새로운 위치로 복사하면서 기록을 보존."
content_hash: 867bed98174961a925402cc61ecbf25e58861061
last_modified_at: 2024-10-07
related_topics:
  - title: English version
    url: /en/common/git-cp.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/git-cp.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/git-cp.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># git cp

기존 파일을 새로운 위치로 복사하면서 기록을 보존.
`git-extras`의 일부.
더 많은 정보: <https://github.com/tj/git-extras/blob/master/Commands.md#git-cp>.

- Git 저장소에서 기존 파일을 동일한 디렉토리에 복사:

`git cp `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">파일</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">새_파일</span>

- Git 저장소에서 기존 파일을 다른 위치에 복사:

`git cp `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/새_파일</span>
