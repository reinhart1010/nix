---
layout: page
title: common/git-diff-files (한국어)
description: "파일의 sha1 해시와 모드를 사용하여 파일을 비교."
content_hash: 31bd6703d2be2c9463f1acae98deaf311ddf8a88
last_modified_at: 2024-10-08
related_topics:
  - title: English version
    url: /en/common/git-diff-files.html
    icon: bi bi-globe
tldri18n_status: 2
---
# git diff-files

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
