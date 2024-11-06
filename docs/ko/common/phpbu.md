---
layout: page
title: common/phpbu (한국어)
description: "PHP 백업 유틸리티 프레임워크."
content_hash: 0e3e6d62fc87dd2dff942f410fbc45df19be4de6
last_modified_at: 2024-11-06
related_topics:
  - title: Deutsch version
    url: /de/common/phpbu.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/phpbu.html
    icon: bi bi-globe
tldri18n_status: 2
---
# phpbu

PHP 백업 유틸리티 프레임워크.
더 많은 정보: <https://phpbu.de>.

- 기본 `phpbu.xml` 구성 파일을 사용하여 백업 실행:

`phpbu`

- 특정 구성 파일을 사용하여 백업 실행:

`phpbu --configuration=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/구성_파일.xml</span>

- 지정된 백업만 실행:

`phpbu --limit=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">백업_작업_이름</span>

- 수행될 작업을 시뮬레이션:

`phpbu --simulate`
