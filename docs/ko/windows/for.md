---
layout: page
title: windows/for (한국어)
description: "조건에 따라 명령을 여러 번 실행."
content_hash: 06c6c059694fa5caf77691a734efc0c49b7d0de6
last_modified_at: 2024-11-06
related_topics:
  - title: English version
    url: /en/windows/for.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/windows/for.html
    icon: bi bi-globe
tldri18n_status: 2
---
# for

조건에 따라 명령을 여러 번 실행.
더 많은 정보: <https://learn.microsoft.com/windows-server/administration/windows-commands/for>.

- 지정된 집합에 대해 명령 실행:

`for %`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">변수</span>` in (`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">항목_a 항목_b 항목_c</span>`) do (`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">echo 루프가 실행됩니다</span>`)`

- 주어진 숫자 범위를 반복:

`for /l %`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">변수</span>` in (`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">시작</span>`, `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">단계</span>`, `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">끝</span>`) do (`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">echo 루프가 실행됩니다</span>`)`

- 주어진 파일 목록을 반복:

`for %`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">변수</span>` in (`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로\대상\파일1.ext 경로\대상\파일2.ext ...</span>`) do (`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">echo 루프가 실행됩니다</span>`)`

- 주어진 디렉토리 목록을 반복:

`for /d %`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">변수</span>` in (`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로\대상\폴더1.ext 경로\대상\폴더2.ext ...</span>`) do (`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">echo 루프가 실행됩니다</span>`)`

- 모든 디렉토리에서 지정된 명령 수행:

`for /d %`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">변수</span>` in (*) do (if exist %`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">변수</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">echo 루프가 실행됩니다</span>`)`
