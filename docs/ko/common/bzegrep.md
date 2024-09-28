---
layout: page
title: common/bzegrep (한국어)
description: "`egrep`을 사용하여 `bzip2` 압축 파일에서 확장 정규식 패턴을 찾음."
content_hash: 6a707f1cd7c16bee39c72465abddaae4b0be4007
last_modified_at: 2024-09-28
related_topics:
  - title: English version
    url: /en/common/bzegrep.html
    icon: bi bi-globe
tldri18n_status: 2
---
# bzegrep

`egrep`을 사용하여 `bzip2` 압축 파일에서 확장 정규식 패턴을 찾음.
더 많은 정보: <https://manned.org/bzegrep>.

- 압축 파일에서 확장된 정규식 (`?`, `+`, `{}`, `()` 및 `|` 지원)을 검색 (대소문자 구분):

`bzegrep "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">검색_패턴</span>`" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- 압축 파일에서 확장된 정규식 (`?`, `+`, `{}`, `()` 및 `|` 지원)을 검색 (대소문자 구분하지 않음)::

`bzegrep --ignore-case "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">검색_패턴</span>`" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- 패턴과 일치하지 않는 라인 검색:

`bzegrep --invert-match "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">검색_패턴</span>`" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- 각 일치 항목의 파일 이름과 줄 번호를 인쇄:

`bzegrep --with-filename --line-number "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">검색_패턴</span>`" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- 패턴과 일치하는 줄을 검색하여 일치하는 텍스트만 인쇄:

`bzegrep --only-matching "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">검색_패턴</span>`" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- bzip2으로 압축된 tar 아카이브에서 파일을 반복적으로 검색하여 패턴을 찾음:

`bzegrep --recursive "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">검색_패턴</span>`" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>
