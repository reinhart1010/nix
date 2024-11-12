---
layout: page
title: osx/cat (한국어)
description: "파일을 출력하고 연결합니다."
content_hash: 77aadd963d5a710c3c0c8aff2a30c0455f5c7dbb
last_modified_at: 2024-11-12
related_topics:
  - title: English version
    url: /en/osx/cat.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/osx/cat.html
    icon: bi bi-globe
tldri18n_status: 2
---
# cat

파일을 출력하고 연결합니다.
더 많은 정보: <https://keith.github.io/xcode-man-pages/cat.1.html>.

- 파일의 내용을 `stdout`에 출력:

`cat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- 여러 파일을 연결하여 출력 파일로 저장:

`cat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일1 경로/대상/파일2 ...</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력_파일</span>

- 여러 파일을 출력 파일에 추가:

`cat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일1 경로/대상/파일2 ...</span>` >> `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력_파일</span>

- 파일의 내용을 버퍼링 없이 출력 파일로 복사:

`cat -u `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/tty12</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/tty13</span>

- `stdin`을 파일에 기록:

`cat - > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- 모든 출력 줄에 번호 매기기:

`cat -n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- 출력하지 않는 문자와 공백 문자 표시 (`M-` 접두사가 붙은 경우 비-ASCII):

`cat -v -t -e `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>
