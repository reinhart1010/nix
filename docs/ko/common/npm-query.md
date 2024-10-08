---
layout: page
title: common/npm-query (한국어)
description: "CSS와 유사한 선택자를 사용하여 의존성 객체 배열을 출력합니다."
content_hash: f83b80e03876077d3588b48e6da766e67b231fc2
last_modified_at: 2024-10-10
related_topics:
  - title: English version
    url: /en/common/npm-query.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/npm-query.html
    icon: bi bi-globe
tldri18n_status: 2
---
# npm query

CSS와 유사한 선택자를 사용하여 의존성 객체 배열을 출력합니다.
더 많은 정보: <https://docs.npmjs.com/cli/commands/npm-query>.

- 직접 의존성 출력:

`npm query ':root > *'`

- 모든 직접 프로덕션/개발 의존성을 출력:

`npm query ':root > .`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">prod|dev</span>`'`

- 특정 이름으로 의존성 출력:

`npm query '#`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">패키지</span>`'`

- 특정 이름과 시맨틱 버전 관리 범위 내에서 의존성을 출력:

`npm query '#`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">패키지</span>`@`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">시멘틱 버전</span>`'`

- 의존성이 없는 의존성을 출력:

`npm query ':empty'`

- 설치 후 스크립트로 모든 의존성을 찾아 제거:

`npm query ":attr(scripts, [postinstall])" | jq 'map(.name) | join("\n")' -r | xargs -I {} npm uninstall {}`

- 모든 Git 종속성을 찾아 어떤 애플리케이션에 필요한지 출력:

`npm query ":type(git)" | jq 'map(.name)' | xargs -I {} npm why {}`
