---
layout: page
title: osx/shuf (한국어)
description: "무작위 순열 생성."
content_hash: 3696df4428a313188df143c6f9d9a2e5ed3a3c82
last_modified_at: 2024-11-12
related_topics:
  - title: English version
    url: /en/osx/shuf.html
    icon: bi bi-globe
  - title: español version
    url: /es/osx/shuf.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/osx/shuf.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/osx/shuf.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/osx/shuf.html
    icon: bi bi-globe
tldri18n_status: 2
---
# shuf

무작위 순열 생성.
더 많은 정보: <https://keith.github.io/xcode-man-pages/shuf.1.html>.

- 파일의 줄 순서를 무작위로 변환하여 결과 출력:

`shuf `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- 결과의 처음 5개 항목만 출력:

`shuf --head-count=5 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- 출력을 다른 파일에 쓰기:

`shuf `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/입력_파일</span>` --output=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력_파일</span>

- 1에서 10까지의 범위에서 무작위 숫자 생성:

`shuf --input-range=1-10`
