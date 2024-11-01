---
layout: page
title: common/hashid (한국어)
description: "데이터 및 비밀번호 해시를 식별하는 Python3 프로그램."
content_hash: 9c0ffcfaf699a50809ee06b646be3352b467803f
last_modified_at: 2024-11-01
related_topics:
  - title: English version
    url: /en/common/hashid.html
    icon: bi bi-globe
tldri18n_status: 2
---
# hashid

데이터 및 비밀번호 해시를 식별하는 Python3 프로그램.
더 많은 정보: <https://github.com/psypanda/hashID>.

- `stdin`에서 해시를 식별 (입력, 복사 및 붙여넣기 또는 해시를 프로그램에 파이프 사용):

`hashid`

- 하나 이상의 해시를 식별:

`hashid `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">해시1 해시2 ...</span>

- 파일의 해시를 식별 (한 줄에 하나의 해시):

`hashid `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/해시.txt</span>

- 가능한 모든 해시 유형 표시 (salt된 해시를 포함):

`hashid --extended `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">해시</span>

- `hashcat`의 모드 번호와 `john`의 해시 유형 형식 문자열을 표시:

`hashid --mode --john `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">해시</span>

- `stdout`으로 출력하는 대신 파일에 출력을 저장:

`hashid --outfile `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력파일.txt</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">해시</span>
