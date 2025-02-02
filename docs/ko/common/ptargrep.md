---
layout: page
title: common/ptargrep (한국어)
description: "tar 아카이브 파일에서 정규 표현식 패턴 찾기."
content_hash: d2fb42906134e6d71981fac373399da1735a3225
last_modified_at: 2024-11-08
related_topics:
  - title: English version
    url: /en/common/ptargrep.html
    icon: bi bi-globe
tldri18n_status: 2
---
# ptargrep

tar 아카이브 파일에서 정규 표현식 패턴 찾기.
더 많은 정보: <https://manned.org/ptargrep>.

- 하나 이상의 tar 아카이브 내에서 패턴 검색:

`ptargrep "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">검색_패턴</span>`" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일1 경로/대상/파일2 ...</span>

- 파일의 기본 이름을 사용하여 현재 디렉토리에 추출:

`ptargrep --basename "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">검색_패턴</span>`" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- tar 아카이브 내에서 대소문자를 구분하지 않고 패턴 검색:

`ptargrep --ignore-case "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">검색_패턴</span>`" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>
