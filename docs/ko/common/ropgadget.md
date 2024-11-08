---
layout: page
title: common/ropgadget (한국어)
description: "바이너리 파일에서 ROP 가젯을 찾습니다."
content_hash: b1e4b91af3cdefae72f84645af0b36e04b9949b2
last_modified_at: 2024-11-08
related_topics:
  - title: English version
    url: /en/common/ropgadget.html
    icon: bi bi-globe
tldri18n_status: 2
---
# ROPgadget

바이너리 파일에서 ROP 가젯을 찾습니다.
더 많은 정보: <https://github.com/JonathanSalwan/ROPgadget>.

- 바이너리 파일에서 가젯 나열:

`ROPgadget --binary `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/바이너리</span>

- 정규 표현식으로 바이너리 파일의 가젯 필터링:

`ROPgadget --binary `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/바이너리</span>` --re `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">정규표현식</span>

- 지정된 유형을 제외한 바이너리 파일의 가젯 나열:

`ROPgadget --binary `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/바이너리</span>` --`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">norop|nojob|nosys</span>

- 바이너리 파일에서 잘못된 바이트 가젯 제외:

`ROPgadget --binary `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/바이너리</span>` --badbytes `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">바이트_문자열</span>

- 지정된 바이트 수까지의 바이너리 파일 가젯 나열:

`ROPgadget --binary `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/바이너리</span>` --depth `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">바이트_수</span>
