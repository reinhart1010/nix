---
layout: page
title: common/git-var (한국어)
description: "Git 논리 변수의 값을 출력."
content_hash: 8b3ec5966385c194a0bbdf101f3a6f807b8ab7a8
last_modified_at: 2024-10-07
related_topics:
  - title: English version
    url: /en/common/git-var.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/git-var.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/git-var.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># git var

Git 논리 변수의 값을 출력.
`git var`보다 `git config`를 사용하는 것이 좋습니다.
더 많은 정보: <https://git-scm.com/docs/git-var>.

- Git 논리 변수의 값을 출력:

`git var `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">GIT_AUTHOR_IDENT|GIT_COMMITTER_IDENT|GIT_EDITOR|GIT_PAGER</span>

- 모든 Git 논리 변수를 [l]리스트:

`git var -l`
