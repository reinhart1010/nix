---
layout: page
title: osx/tail (한국어)
description: "파일의 마지막 부분을 표시합니다."
content_hash: ffdf4bfcc30b2d7aa41ad1fe86ae62623f7fece7
last_modified_at: 2024-11-12
related_topics:
  - title: English version
    url: /en/osx/tail.html
    icon: bi bi-globe
  - title: español version
    url: /es/osx/tail.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/osx/tail.html
    icon: bi bi-globe
tldri18n_status: 2
---
# tail

파일의 마지막 부분을 표시합니다.
같이 보기: `head`.
더 많은 정보: <https://keith.github.io/xcode-man-pages/tail.1.html>.

- 파일에서 마지막 '개수' 줄을 표시:

`tail -n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">8</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- 특정 행 번호부터 파일 출력:

`tail -n +`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">8</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- 주어진 파일의 끝에서부터 특정 개수의 바이트 출력:

`tail -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">8</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- 주어진 파일의 마지막 줄을 출력하고 `Ctrl + C`까지 계속 읽기:

`tail -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- 파일이 접근 불가능해도 `Ctrl + C`까지 계속 읽기:

`tail -F `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- '파일'의 마지막 '개수' 줄을 표시하고 '초'마다 새로 고침:

`tail -n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">8</span>` -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">10</span>` -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>
