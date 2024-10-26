---
layout: page
title: common/cpan (한국어)
description: "CPAN 사이트에서 perl 모듈을 쿼리, 다운로드 및 빌드하기."
content_hash: 1874486c3016d9d6ad248dcb85326555e94f37c0
last_modified_at: 2024-10-26
related_topics:
  - title: English version
    url: /en/common/cpan.html
    icon: bi bi-globe
tldri18n_status: 2
---
# cpan

CPAN 사이트에서 perl 모듈을 쿼리, 다운로드 및 빌드하기.
더 많은 정보: <https://manned.org/cpan>.

- 모듈을 설치(`-i`는 선택 사항):

`cpan `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-i</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">모듈_이름</span>

- 모듈을 강제 설치(`-i`는 선택 사항이 아님):

`cpan -fi `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">모듈_이름</span>

- 설치된 모든 모듈을 업그레이드:

`cpan -u`

- 모듈을 다시 컴파일:

`cpan -r`
