---
layout: page
title: common/perl (한국어)
description: "Perl 5 언어 인터프리터."
content_hash: 9d0b5665768e4c611724073f6e9b01bf4d4cfe67
last_modified_at: 2024-11-08
related_topics:
  - title: English version
    url: /en/common/perl.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/perl.html
    icon: bi bi-globe
tldri18n_status: 2
---
# perl

Perl 5 언어 인터프리터.
더 많은 정보: <https://www.perl.org>.

- `stdin`에서 regex1과 일치하고 대소문자를 구분하지 않는 regex2와 일치하는 행 출력:

`perl -n -e 'print if m/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">regex1</span>`/ and m/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">regex2</span>`/i'`

- 공백을 무시하고 정규식을 사용하여 첫 번째 매치 그룹 출력:

`perl -n -E 'say $1 if m/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">이전</span>` (  `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">정규식_그룹</span>`  ) `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">이후</span>`/x'`

- 백업과 함께 제자리에서 모든 regex 발생을 대체:

`perl -i'.bak' -p -e 's/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">regex</span>`/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">대체</span>`/g' `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일들</span>

- Perl의 인라인 문서 사용, 일부 페이지는 Linux의 매뉴얼 페이지에서도 사용 가능:

`perldoc perlrun ; perldoc module ; perldoc -f splice; perldoc -q perlfaq1`
