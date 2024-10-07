---
layout: page
title: common/git-clear-soft (한국어)
description: "현재 브랜치와 `.gitignore`에 포함된 파일을 제외하고 Git 작업 디렉토리를 새로 클론한 것처럼 초기화."
content_hash: 9fd7cee2300d31834889121d6fc5e2304f10975b
last_modified_at: 2024-10-07
related_topics:
  - title: English version
    url: /en/common/git-clear-soft.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/git-clear-soft.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/git-clear-soft.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># git clear-soft

현재 브랜치와 `.gitignore`에 포함된 파일을 제외하고 Git 작업 디렉토리를 새로 클론한 것처럼 초기화.
`git-extras`의 일부.
더 많은 정보: <https://github.com/tj/git-extras/blob/master/Commands.md#git-clear-soft>.

- 모든 추적된 파일을 초기화하고 모든 추적되지 않은 파일 삭제:

`git clear-soft`
