---
layout: page
title: common/cradle-elastic (한국어)
description: "Cradle 인스턴스의 ElasticSearch 인스턴스 관리."
content_hash: fbe0c1b5a7e08f6508ba110af2ea9395812a300a
related_topics:
  - title: Deutsch version
    url: /de/common/cradle-elastic.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/cradle-elastic.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/cradle-elastic.html
    icon: bi bi-globe
---
# cradle elastic

Cradle 인스턴스의 ElasticSearch 인스턴스 관리.
더 많은 정보: <https://cradlephp.github.io/docs/3.B.-Reference-Command-Line-Tools.html#elastic>.

- ElasticSearch 색인 자르기:

`cradle elastic flush`

- 특정 패키지에 대한 ElasticSearch 색인 자르기:

`cradle elastic flush `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">패키지_명</span>

- ElasticSearch 스키마 제출:

`cradle elastic map`

- 특정 패키지에 대한 ElasticSearch 스키마 제출:

`cradle elastic map `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">패키지_명</span>

- 모든 패키지에 대한 ElasticSearch 색인 채우기:

`cradle elastic populate`

- 특정 패키지에 대한 ElasticSearch 색인 채우기:

`cradle elastic populate `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">패키지_명</span>
