---
layout: page
title: common/git-clear (한국어)
description: "현재 브랜치와 `.gitignore`에 포함된 파일들을 포함하여 Git 작업 디렉토리를 새로 클론한 것처럼 초기화합니다."
content_hash: f4cf47f1d11467f9bfc2a8cbae88d67b5b710883
last_modified_at: 2024-10-07
related_topics:
  - title: English version
    url: /en/common/git-clear.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/git-clear.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/git-clear.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># git clear

현재 브랜치와 `.gitignore`에 포함된 파일들을 포함하여 Git 작업 디렉토리를 새로 클론한 것처럼 초기화합니다.
`git-extras`의 일부입니다.
더 많은 정보: <https://github.com/tj/git-extras/blob/master/Commands.md#git-clear>.

- 모든 추적된 파일을 초기화하고 `.gitignore`에 포함된 파일을 포함하여 모든 추적되지 않은 파일 삭제:

`git clear`
