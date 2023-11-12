---
layout: page
title: common/dokku (한국어)
description: "도커로 구동되는 미니-Heroku (PaaS)."
content_hash: e5964ee2d4a0071465121fb4b83083524cb37956
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/dokku.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/dokku.html
    icon: bi bi-globe
  - title: українська version
    url: /uk/common/dokku.html
    icon: bi bi-globe
tldri18n_status: 2
---
# dokku

도커로 구동되는 미니-Heroku (PaaS).
하나의 `git-push` 명령을 사용하여 여러 언어로 다른 앱을 쉽게 배포 할수 있습니다.
더 많은 정보: <https://github.com/dokku/dokku>.

- 실행중인 앱들 목록보기:

`dokku apps`

- 앱 생성하기:

`dokku apps:create `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">앱_이름</span>

- 앱 제거하기:

`dokku apps:destroy `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">앱_이름</span>

- 플러그인 설치하기:

`dokku plugin:install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">전체_폴더_경로</span>

- 앱에 데이터베이스 연결하기:

`dokku `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">db</span>`:link `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">데이터베이스_이름</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">앱_이름</span>
