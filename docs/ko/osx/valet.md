---
layout: page
title: osx/valet (한국어)
description: "Laravel 개발 환경으로, `http://<example>.test`에서 로컬 터널을 통해 사이트를 호스팅할 수 있습니다."
content_hash: 676b1c6b7fd7b8d3f3eef5dc68f3c6409fe9c547
last_modified_at: 2024-11-12
related_topics:
  - title: English version
    url: /en/osx/valet.html
    icon: bi bi-globe
  - title: español version
    url: /es/osx/valet.html
    icon: bi bi-globe
tldri18n_status: 2
---
# valet

Laravel 개발 환경으로, `http://<example>.test`에서 로컬 터널을 통해 사이트를 호스팅할 수 있습니다.
더 많은 정보: <https://laravel.com/docs/valet>.

- valet 데몬 시작:

`valet start`

- 현재 작업 중인 디렉토리를 Valet이 사이트를 검색할 경로로 등록:

`valet park`

- '주차된' 경로 보기:

`valet paths`

- 전체 디렉토리가 아닌 단일 사이트 제공:

`valet link `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">애플리케이션_이름</span>

- Ngrok 터널을 통해 프로젝트 공유:

`valet share`
