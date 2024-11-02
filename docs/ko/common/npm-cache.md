---
layout: page
title: common/npm-cache (한국어)
description: "npm 패키지 캐시 관리."
content_hash: e1efceb25769f4474507d03187490412cb67f018
last_modified_at: 2024-11-02
related_topics:
  - title: English version
    url: /en/common/npm-cache.html
    icon: bi bi-globe
tldri18n_status: 2
---
# npm cache

npm 패키지 캐시 관리.
더 많은 정보: <https://docs.npmjs.com/cli/commands/npm-cache>.

- 특정 패키지를 캐시에 추가:

`npm cache add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">패키지_이름</span>

- 특정 패키지를 캐시에서 제거:

`npm cache remove `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">패키지_이름</span>

- 키를 사용하여 특정 캐시 항목 삭제:

`npm cache clean `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">키</span>

- 전체 npm 캐시 삭제:

`npm cache clean --force`

- npm 캐시의 내용 나열:

`npm cache ls`

- npm 캐시의 무결성 확인:

`npm cache verify`

- npm 캐시 위치 및 구성 정보 표시:

`npm cache dir`

- 캐시 경로 변경:

`npm config set cache `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/폴더</span>
