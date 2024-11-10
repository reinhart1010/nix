---
layout: page
title: common/swagger-codegen (한국어)
description: "OpenAPI/swagger 정의에서 REST API에 대한 코드와 문서를 생성합니다."
content_hash: 548822a63b1fc61151c9ef983fc2e47b2ae82f1f
last_modified_at: 2024-11-10
related_topics:
  - title: English version
    url: /en/common/swagger-codegen.html
    icon: bi bi-globe
tldri18n_status: 2
---
# swagger-codegen

OpenAPI/swagger 정의에서 REST API에 대한 코드와 문서를 생성합니다.
더 많은 정보: <https://github.com/swagger-api/swagger-codegen>.

- OpenAPI/swagger 파일에서 문서와 코드 생성:

`swagger-codegen generate -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">swagger_파일</span>` -l `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">언어</span>

- 라이브러리 retrofit2와 옵션 useRxJava2를 사용하여 Java 코드 생성:

`swagger-codegen generate -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">http://petstore.swagger.io/v2/swagger.json</span>` -l `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">java</span>` --library `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">retrofit2</span>` -D`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">useRxJava2</span>`=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">true</span>

- 사용 가능한 언어 나열:

`swagger-codegen langs`

- 특정 명령에 대한 도움말 표시:

`swagger-codegen `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">generate|config-help|meta|langs|version</span>` --help`
