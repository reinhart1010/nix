---
layout: page
title: common/atoum (한국어)
description: "PHP를 위한 단순하고 현대적이며 직관적인 단위 테스트 프레임워크."
content_hash: 82cae96673f9718917a21aa24b215165940683ed
last_modified_at: 2024-10-12
related_topics:
  - title: English version
    url: /en/common/atoum.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/atoum.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/atoum.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/atoum.html
    icon: bi bi-globe
tldri18n_status: 2
---
# atoum

PHP를 위한 단순하고 현대적이며 직관적인 단위 테스트 프레임워크.
더 많은 정보: <https://atoum.org>.

- 설정 파일 초기화:

`atoum --init`

- 모든 테스트 실행:

`atoum`

- 특정 설정 파일을 사용한 테스트 실행:

`atoum -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/파일명</span>

- 특정 테스트파일 실행:

`atoum -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/파일명</span>

- 특정 테스트 디렉토리 실행:

`atoum -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/디렉토리명</span>

- 특정 namespace 아래 있는 모든 테스트 실행:

`atoum -ns `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">namespace</span>

- 특정 태그를 갖고 테스트 실행:

`atoum -t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">태그</span>

- 테스트를 실행하기 전에 사용자 지정 부트스트랩 파일을 로드:

`atoum --bootstrap-file `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/파일명</span>
