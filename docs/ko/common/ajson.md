---
layout: page
title: common/ajson (한국어)
description: "JSON 객체에서 JSONPath를 실행합니다."
content_hash: 26cafdc3e337380ae6e48f78fe00348c6016cfd3
last_modified_at: 2023-12-11
related_topics:
  - title: English version
    url: /en/common/ajson.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/ajson.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/ajson.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/ajson.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/ajson.html
    icon: bi bi-globe
tldri18n_status: 2
---
# ajson

JSON 객체에서 JSONPath를 실행합니다.
더 많은 정보: <https://github.com/spyzhov/ajson>.

- 파일에서 JSON을 읽고 지정된 JSONPath 표현식을 실행:

`ajson '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">$..json[?(@.path)]</span>`' `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.json</span>

- `stdin`에서 JSON을 읽고 지정된 JSONPath 표현식을 실행:

`cat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.json</span>` | ajson '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">$..json[?(@.path)]</span>`'`

- URL에서 JSON을 읽고 지정된 JSONPath 표현식을 평가:

`ajson '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">avg($..price)</span>`' '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://example.com/api/</span>`'`

- 간단한 JSON을 읽고 값을 계산:

`echo '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">3</span>`' | ajson '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">2 * pi * $</span>`'`
