---
layout: page
title: osx/pbcopy (한국어)
description: "`stdin`에서 데이터를 클립보드로 복사합니다."
content_hash: 8e66d8240e2ca3fb07bd7fd2d2244f1c10effabc
last_modified_at: 2024-11-12
related_topics:
  - title: English version
    url: /en/osx/pbcopy.html
    icon: bi bi-globe
  - title: español version
    url: /es/osx/pbcopy.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/osx/pbcopy.html
    icon: bi bi-globe
  - title: ไทย version
    url: /th/osx/pbcopy.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/osx/pbcopy.html
    icon: bi bi-globe
tldri18n_status: 2
---
# pbcopy

`stdin`에서 데이터를 클립보드로 복사합니다.
키보드에서 Cmd + C를 누르는 것과 비슷합니다.
더 많은 정보: <https://keith.github.io/xcode-man-pages/pbcopy.1.html>.

- 특정 [f]파일의 내용을 클립보드에 복사:

`pbcopy < `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- 특정 명령의 결과를 클립보드에 복사:

`find . -type t -name "*.png" | pbcopy`
