---
layout: page
title: common/ack (한국어)
description: "프로그래머에게 최적화된 grep과 같은 검색툴."
content_hash: 5a5d550630625637ea0847498f8a5f0f33782eba
last_modified_at: 2023-11-12
related_topics:
  - title: বাংলা version
    url: /bn/common/ack.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/ack.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/ack.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/ack.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/ack.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/ack.html
    icon: bi bi-globe
  - title: norsk version
    url: /no/common/ack.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/common/ack.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/ack.html
    icon: bi bi-globe
  - title: русский version
    url: /ru/common/ack.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/common/ack.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/ack.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># ack

프로그래머에게 최적화된 grep과 같은 검색툴.
더 많은 정보: <https://beyondgrep.com/documentation>.

- "foo"를 포함하고 있는 파일 검색:

`ack `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">foo</span>

- 특정 타입의 파일 검색:

`ack --ruby `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">foo</span>

- "foo"라는 용어와 일치하는 총 합을 계산:

`ack -ch `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">foo</span>

- "foo"를 포함하고있는 파일의 이름과 각각 파일에서 일치하는 수를 표시:

`ack -cl `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">foo</span>

- 모든 가능한 타입 리스트:

`ack --help-types`
