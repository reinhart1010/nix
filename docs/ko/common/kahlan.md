---
layout: page
title: common/kahlan (한국어)
description: "PHP용 단위 테스트 및 행동 주도 개발 테스트 프레임워크."
content_hash: 052d5e1fc82a7239ef53515db095ea5345af81c9
last_modified_at: 2024-11-03
related_topics:
  - title: English version
    url: /en/common/kahlan.html
    icon: bi bi-globe
tldri18n_status: 2
---
# kahlan

PHP용 단위 테스트 및 행동 주도 개발 테스트 프레임워크.
더 많은 정보: <https://kahlan.github.io>.

- "spec" 디렉토리의 모든 사양 실행:

`kahlan`

- 특정 구성 파일을 사용하여 사양 실행:

`kahlan --config=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/구성_파일</span>

- 리포터를 사용하여 사양 실행 및 출력:

`kahlan --reporter=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">dot|bar|json|tap|verbose</span>

- 코드 커버리지와 함께 사양 실행 (세부 수준은 0에서 4 사이):

`kahlan --coverage=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">세부_수준</span>
