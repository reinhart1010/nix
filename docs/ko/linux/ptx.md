---
layout: page
title: linux/ptx (한국어)
description: "텍스트 파일에서 단어의 순열 색인을 생성합니다."
content_hash: 408613cd1f8f414c2310bbaa3fe3e8d0b6b3f589
last_modified_at: 2025-03-02
related_topics:
  - title: English version
    url: /en/linux/ptx.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/linux/ptx.html
    icon: bi bi-globe
tldri18n_status: 2
---
# ptx

텍스트 파일에서 단어의 순열 색인을 생성합니다.
더 많은 정보: <https://www.gnu.org/software/coreutils/manual/html_node/ptx-invocation.html>.

- 각 줄의 첫 번째 필드가 색인 참조인 순열 색인 생성:

`ptx --references `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- 자동 생성된 색인 참조가 포함된 순열 색인 생성:

`ptx --auto-reference `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- 고정된 너비로 순열 색인 생성:

`ptx --width=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">열_너비</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- 필터링된 단어 목록으로 순열 색인 생성:

`ptx --only-file=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/필터</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- SYSV 스타일의 동작으로 순열 색인 생성:

`ptx --traditional `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>
