---
layout: page
title: common/xsv (한국어)
description: "Rust로 작성된 CSV 명령줄 도구 모음."
content_hash: c0c785bc962093ff91a810abc1514bb5c5e5e4d8
last_modified_at: 2024-11-06
related_topics:
  - title: English version
    url: /en/common/xsv.html
    icon: bi bi-globe
tldri18n_status: 2
---
# xsv

Rust로 작성된 CSV 명령줄 도구 모음.
더 많은 정보: <https://github.com/BurntSushi/xsv>.

- 파일의 헤더 확인:

`xsv headers `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.csv</span>

- 항목 수 세기:

`xsv count `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.csv</span>

- 항목 형식 개요 보기:

`xsv stats `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.csv</span>` | xsv table`

- 몇몇 열 선택:

`xsv select `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">열1,열2</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.csv</span>

- 10개의 무작위 항목 표시:

`xsv sample `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">10</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.csv</span>

- 한 파일의 열을 다른 파일에 연결:

`xsv join --no-case `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">열1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일1.csv</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">열2</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일2.csv</span>` | xsv table`
