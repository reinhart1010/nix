---
layout: page
title: common/xzgrep (한국어)
description: "정규식을 사용하여 `xz`, `lzma`, `gzip`, `bzip2`, `lzop`, 또는 `zstd`로 압축된 파일을 검색합니다."
content_hash: 74c6f94a845d5026e073dc83eba74f06846a7c02
last_modified_at: 2024-11-06
related_topics:
  - title: English version
    url: /en/common/xzgrep.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/xzgrep.html
    icon: bi bi-globe
tldri18n_status: 2
---
# xzgrep

정규식을 사용하여 `xz`, `lzma`, `gzip`, `bzip2`, `lzop`, 또는 `zstd`로 압축된 파일을 검색합니다.
같이 보기: `grep`.
더 많은 정보: <https://manned.org/xzgrep>.

- 파일 내 패턴 검색:

`xzgrep "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">검색_패턴</span>`" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- 정확한 문자열 검색 (정규식 사용 안 함):

`xzgrep --fixed-strings "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">정확한_문자열</span>`" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- 모든 파일에서 패턴을 검색하고 일치하는 줄 번호 표시:

`xzgrep --line-number "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">검색_패턴</span>`" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- 확장 정규식(지원: `?`, `+`, `{}`, `()` 및 `|`)과 대소문자 구분 없는 모드 사용:

`xzgrep --extended-regexp --ignore-case "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">검색_패턴</span>`" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- 각 일치 항목 주변, 이전 또는 이후에 3줄의 컨텍스트 출력:

`xzgrep --`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">context|before-context|after-context</span>`=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">3</span>` "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">검색_패턴</span>`" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- 각 일치 항목에 대해 파일 이름과 줄 번호를 색상 출력으로 표시:

`xzgrep --with-filename --line-number --color=always "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">검색_패턴</span>`" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- 패턴과 일치하는 줄을 검색하고 일치하는 텍스트만 출력:

`xzgrep --only-matching "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">검색_패턴</span>`" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>
