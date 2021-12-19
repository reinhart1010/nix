---
layout: page
title: common/cradle-sql (한국어)
description: "Cradle SQL 데이터베이스 관리."
content_hash: fcbfe809c53791045720790b670aff57ceb2f835
related_topics:
  - title: Deutsch version
    url: /de/common/cradle-sql.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/cradle-sql.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/cradle-sql.html
    icon: bi bi-globe
---
# cradle sql

Cradle SQL 데이터베이스 관리.
더 많은 정보: <https://cradlephp.github.io/docs/3.B.-Reference-Command-Line-Tools.html#sql>.

- 데이터베이스 스키마 재구축:

`cradle sql build`

- 특정 패키지에 대한 데이터베이스 스키마 재구축:

`cradle sql build `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">패키지_명</span>

- 전체 데이터베이스 비우기:

`cradle sql flush`

- 특정 패키지에 대한 데이터베이스 테이블 비우기:

`cradle sql flush `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">패키지_명</span>

- 모든 패키지에 대한 테이블 채우기:

`cradle sql populate`

- 특정 패키지에 대한 테이블 채우기:

`cradle sql populate `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">패키지_명</span>
