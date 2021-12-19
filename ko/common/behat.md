---
layout: page
title: common/behat (한국어)
description: "Behaviour-Driven 개발을 위한 PHP 프레임워크."
content_hash: 3f6f2f7de9e6cc9ddd49d6aeb607ba208d8b5069
related_topics:
  - title: English version
    url: /en/common/behat.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/behat.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/behat.html
    icon: bi bi-globe
---
# behat

Behaviour-Driven 개발을 위한 PHP 프레임워크.
더 많은 정보: <https://behat.org>.

- 새로운 Behat 프로젝트 초기화:

`behat --init`

- 모든 테스트 실행:

`behat`

- 지정된 suite에서 모든 테스트 실행:

`behat --suite=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">suite_명</span>

- 특정 출력 formatter로 테스트 실행:

`behat --format `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">좋은|진행</span>

- 테스트 실행 및 파일로 결과 출력:

`behat --out `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">파일/의/경로</span>

- 테스트 suite에 정의 목록 표시:

`behat --definitions`
