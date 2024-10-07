---
layout: page
title: common/git-authors (한국어)
description: "Git 저장소의 커밋 작성자 목록을 생성."
content_hash: 13678118c7475f638bcde05c3b0aac5f96287eff
last_modified_at: 2024-10-07
related_topics:
  - title: English version
    url: /en/common/git-authors.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/git-authors.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/git-authors.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># git authors

Git 저장소의 커밋 작성자 목록을 생성.
`git-extras`의 일부.
더 많은 정보: <https://github.com/tj/git-extras/blob/master/Commands.md#git-authors>.

- 커밋 작성자 목록을 `AUTHORS` 파일 대신 `stdout`에 출력:

`git authors --list`

- 커밋 작성자 목록을 `AUTHORS` 파일에 추가하고 기본 편집기로 열기:

`git authors`

- 이메일 주소를 제외한 커밋 작성자 목록을 `AUTHORS` 파일에 추가하고 기본 편집기로 열기:

`git authors --no-email`
