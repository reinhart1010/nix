---
layout: page
title: windows/scoop-bucket (한국어)
description: "버킷 관리: Git 저장소는 scoop이 애플리케이션을 설치하는 방법을 설명하는 파일을 포함합니다."
content_hash: 0bf05861d402bf67def5c317c94d8bedfdba9c60
last_modified_at: 2024-10-25
related_topics:
  - title: Deutsch version
    url: /de/windows/scoop-bucket.html
    icon: bi bi-globe
  - title: English version
    url: /en/windows/scoop-bucket.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/windows/scoop-bucket.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/windows/scoop-bucket.html
    icon: bi bi-globe
tldri18n_status: 2
---
# scoop bucket

버킷 관리: Git 저장소는 scoop이 애플리케이션을 설치하는 방법을 설명하는 파일을 포함합니다.
Scoop이 버킷이 위치한 곳을 모르면 저장소 위치를 지정해야 합니다.
더 많은 정보: <https://github.com/lukesampson/scoop/wiki/Buckets>.

- 현재 사용 중인 모든 버킷 표시:

`scoop bucket list`

- 알려진 모든 버킷 표시:

`scoop bucket known`

- 알려진 버킷을 이름으로 추가:

`scoop bucket add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">이름</span>

- 이름과 Git 저장소 URL로 알려지지 않은 버킷을 추가:

`scoop bucket add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">이름</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://example.com/repository.git</span>

- 이름으로 버킷 제거:

`scoop bucket rm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">이름</span>
