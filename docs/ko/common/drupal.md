---
layout: page
title: common/drupal (한국어)
description: "상용구 코드를 생성하고, Drupal 프로젝트와 상호작용하며 디버그."
content_hash: d45a589588594324882f882a5d4667fa2ca37aa4
last_modified_at: 2024-10-17
related_topics:
  - title: English version
    url: /en/common/drupal.html
    icon: bi bi-globe
tldri18n_status: 2
---
# drupal

상용구 코드를 생성하고, Drupal 프로젝트와 상호작용하며 디버그.
`check`와 같은 일부 하위 명령에는 자체 사용법 문서가 존재.
더 많은 정보: <https://drupalconsole.com/>.

- 모듈 설치:

`drupal module:install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">모듈_이름</span>

- 모듈 삭제:

`drupal module:uninstall `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">모듈_이름</span>

- 모든 캐시 지우기:

`drupal cache:rebuild`

- 현재 Drupal 설치 상태 보기:

`drupal site:status`
