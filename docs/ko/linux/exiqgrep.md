---
layout: page
title: linux/exiqgrep (한국어)
description: "Exim 큐 출력에서 `grep`의 기능을 제공하는 Perl 스크립트."
content_hash: ff264ad025ae0bbbf50285d4a78705017ac9cc67
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/linux/exiqgrep.html
    icon: bi bi-globe
tldri18n_status: 2
---
# exiqgrep

Exim 큐 출력에서 `grep`의 기능을 제공하는 Perl 스크립트.
더 많은 정보: <https://www.exim.org/exim-html-current/doc/html/spec_html/ch-exim_utilities.html>.

- 발신자 주소를 대소문자 구분 없이 검색:

`exiqgrep -f '<`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">email@somedomain.com</span>`>'`

- 발신자 주소를 검색하고 메시지 ID만 표시:

`exiqgrep -i -f '<`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">email@somedomain.com</span>`>'`

- 수신자 주소 검색:

`exiqgrep -r '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">email@somedomain.com</span>`'`

- 큐에서 발신자 주소와 일치하는 모든 메시지 제거:

`exiqgrep -i -f '<`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">email@somedomain.com</span>`>' | xargs exim -Mrm`

- 반송된 메시지 테스트:

`exiqgrep -f '^<>$'`

- 반송된 메시지 개수 표시:

`exiqgrep -c -f '^<>$'`
