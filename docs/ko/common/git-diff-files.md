---
layout: page
title: common/git-diff-files (한국어)
description: "파일의 sha1 해시와 모드를 사용하여 파일을 비교."
content_hash: 31bd6703d2be2c9463f1acae98deaf311ddf8a88
last_modified_at: 2024-10-07
related_topics:
  - title: English version
    url: /en/common/git-diff-files.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/git-diff-files.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># git diff-files

파일의 sha1 해시와 모드를 사용하여 파일을 비교.
더 많은 정보: <https://git-scm.com/docs/git-diff-files>.

- 변경된 모든 파일 비교:

`git diff-files`

- 지정된 파일만 비교:

`git diff-files `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- 변경된 파일의 이름만 출력:

`git diff-files --name-only`

- 확장 헤더 정보 요약 출력:

`git diff-files --summary`
