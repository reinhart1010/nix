---
layout: page
title: common/bzgrep (한국어)
description: "`grep`을 사용하여 `bzip2`로 압축된 파일에서 패턴을 찾음."
content_hash: c96db67bcd8b229381d5794ed9db265bb80a8191
last_modified_at: 2024-09-28
related_topics:
  - title: English version
    url: /en/common/bzgrep.html
    icon: bi bi-globe
tldri18n_status: 2
---
# bzgrep

`grep`을 사용하여 `bzip2`로 압축된 파일에서 패턴을 찾음.
더 많은 정보: <https://manned.org/bzgrep>.

- 압축 파일 내에서 패턴 검색:

`bzgrep "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">검색_패턴</span>`" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- 대소문자를 구분하지 않는 모드에서 확장 정규표현식 (`?`, `+`, `{}`, `()` 및 `|` 지원)을 사용:

`bzgrep --extended-regexp --ignore-case "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">검색_패턴</span>`" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- 각 일치하는 전후 및 전후 3줄의 컨텍스트를 출력:

`bzgrep --`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">context|before-context|after-context</span>`=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">3</span>` "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">검색_패턴</span>`" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- 각 일치 항목의 파일 이름과 줄 번호를 출력:

`bzgrep --with-filename --line-number "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">검색_패턴</span>`" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- 패턴과 일치하는 줄을 검색하여 일치하는 텍스트만 출력:

`bzgrep --only-matching "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">검색_패턴</span>`" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- bzip2로 압축된 tar 아카이브에서 파일을 반복적으로 검색하여 패턴을 찾음:

`bzgrep --recursive "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">검색_패턴</span>`" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/tar/파일</span>

- 패턴과 일치하지 않는 줄을 `stdin`으로 검색:

`cat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/path/to/bz/compressed/file</span>` | bzgrep --invert-match "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">검색_패턴</span>`"`
