---
layout: page
title: common/fgrep (한국어)
description: "파일의 고정 문자열과 일치."
content_hash: 04b134787689920d9692c4bc93ceb0fee2692cba
last_modified_at: 2024-10-21
related_topics:
  - title: English version
    url: /en/common/fgrep.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/fgrep.html
    icon: bi bi-globe
tldri18n_status: 2
---
# fgrep

파일의 고정 문자열과 일치.
`grep -F`와 동일.
더 많은 정보: <https://www.gnu.org/software/grep/manual/grep.html>.

- 파일에서 정확한 문자열을 검색:

`fgrep `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">검색_문자열</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- 하나 이상의 파일에서 완전히 일치하는 행만 검색:

`fgrep -x `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">검색_문자열</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일1 경로/대상/파일2 ...</span>

- 파일에서 주어진 문자열과 일치하는 줄 수를 셈:

`fgrep -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">검색_문자열</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- 일치하는 줄과 함께 파일의 줄 번호를 표시:

`fgrep -n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">검색_문자열</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- 검색 문자열을 포함하는 행을 제외한 모든 행을 표시:

`fgrep -v `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">검색_문자열</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- 콘텐츠가 검색 문자열과 한 번 이상 일치하는 파일 이름을 표시:

`fgrep -l `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">검색_문자열</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일1 경로/대상/파일2 ...</span>
