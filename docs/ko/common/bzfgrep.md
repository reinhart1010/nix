---
layout: page
title: common/bzfgrep (한국어)
description: "`fgrep`을 사용하여 `bzip2`로 압축된 파일에서 새로운 줄로 구분된 고정 문자열을 찾음."
content_hash: 3b8c89599e4a89ae1c4995726fbca517302eb4f4
last_modified_at: 2024-09-28
related_topics:
  - title: English version
    url: /en/common/bzfgrep.html
    icon: bi bi-globe
tldri18n_status: 2
---
# bzfgrep

`fgrep`을 사용하여 `bzip2`로 압축된 파일에서 새로운 줄로 구분된 고정 문자열을 찾음.
더 많은 정보: <https://manned.org/bzfgrep>.

- 압축 파일에서 새로운 줄로 구분된 검색 문자열 목록과 일치하는 줄을 검색 (대소문자 구분):

`bzfgrep "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">검색_문자열</span>`" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- 압축 파일에서 새로운 줄로 구분된 검색 문자열 목록과 일치하는 줄을 검색 (대소문자 구분하지 않음):

`bzfgrep --ignore-case "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">검색_문자열</span>`" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- 압축 파일에서 새로운 줄로 구분된 검색 문자열 목록과 일치하지 않는 줄을 검색 :

`bzfgrep --invert-match "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">검색_문자열</span>`" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- 각 일치 항목의 파일 이름과 줄 번호를 인쇄:

`bzfgrep --with-filename --line-number "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">검색_문자열</span>`" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- 패턴과 일치하는 줄을 검색하여, 일치하는 텍스트만 인쇄:

`bzfgrep --only-matching "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">검색_문자열</span>`" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- 주어진 문자열 목록에 대해 bzip2로 압축된 tar 아카이브에서 파일을 반복적으로 검색:

`bzfgrep --recursive "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">검색_문자열</span>`" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>
