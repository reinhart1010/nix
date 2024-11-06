---
layout: page
title: common/jest (한국어)
description: "제로 구성 JavaScript 테스트 플랫폼."
content_hash: 0d75bc5f3056bee60d6ca0a0cd228b91c874ce51
last_modified_at: 2024-11-06
related_topics:
  - title: English version
    url: /en/common/jest.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/jest.html
    icon: bi bi-globe
tldri18n_status: 2
---
# jest

제로 구성 JavaScript 테스트 플랫폼.
더 많은 정보: <https://jestjs.io>.

- 사용 가능한 모든 테스트 실행:

`jest`

- 지정된 파일의 테스트 스위트 실행:

`jest `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일1 경로/대상/파일2 ...</span>

- 현재 디렉토리 및 하위 디렉토리 내에서 경로가 주어진 정규 표현식과 일치하는 파일의 테스트 스위트 실행:

`jest `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">정규_표현식1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">정규_표현식2</span>

- 이름이 주어진 정규 표현식과 일치하는 테스트 실행:

`jest --testNamePattern `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">정규_표현식</span>

- 특정 소스 파일과 관련된 테스트 스위트 실행:

`jest --findRelatedTests `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/소스_파일.js</span>

- 커밋되지 않은 모든 파일과 관련된 테스트 스위트 실행:

`jest --onlyChanged`

- 파일 변경을 감시하고 관련 테스트를 자동으로 다시 실행:

`jest --watch`

- 도움말 표시:

`jest --help`
