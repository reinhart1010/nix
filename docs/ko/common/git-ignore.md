---
layout: page
title: common/git-ignore (한국어)
description: "`.gitignore` 파일을 표시/업데이트."
content_hash: 2d69871d255b8e2870298249778e9a355d9b998a
last_modified_at: 2024-10-07
related_topics:
  - title: English version
    url: /en/common/git-ignore.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/git-ignore.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/git-ignore.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># git ignore

`.gitignore` 파일을 표시/업데이트.
`git-extras`의 일부. 같이 보기: `git ignore-io`.
더 많은 정보: <https://github.com/tj/git-extras/blob/master/Commands.md#git-ignore>.

- 모든 전역 및 로컬 `.gitignore` 파일의 내용을 표시:

`git ignore`

- 파일을 비공개로 무시하고, `.git/info/exclude` 파일을 업데이트:

`git ignore `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">파일_패턴</span>` --private`

- 파일을 로컬에서 무시하고, 로컬 `.gitignore` 파일을 업데이트:

`git ignore `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">파일_패턴</span>

- 파일을 전역에서 무시하고, 전역 `.gitignore` 파일을 업데이트:

`git ignore `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">파일_패턴</span>` --global`
