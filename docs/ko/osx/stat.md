---
layout: page
title: osx/stat (한국어)
description: "파일 상태 표시."
content_hash: 941f4e9afed3c8ca52df9c2cb74ea2d50851a737
last_modified_at: 2024-11-12
related_topics:
  - title: English version
    url: /en/osx/stat.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/osx/stat.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/osx/stat.html
    icon: bi bi-globe
tldri18n_status: 2
---
# stat

파일 상태 표시.
더 많은 정보: <https://keith.github.io/xcode-man-pages/stat.1.html>.

- 파일의 크기, 권한, 생성 및 접근 날짜 등의 속성 표시:

`stat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- 위와 동일하지만 자세히 표시 (Linux의 `stat`와 더 유사하게):

`stat -x `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- 파일의 8진수 권한만 표시:

`stat -f %Mp%Lp `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- 파일의 소유자와 그룹 표시:

`stat -f "%Su %Sg" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- 파일의 크기를 바이트 단위로 표시:

`stat -f "%z %N" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>
