---
layout: page
title: common/podman-compose (한국어)
description: "Compose Specification 컨테이너 정의를 실행하고 관리."
content_hash: 87e5ce10f133dec84fd90854b9cde00d584072f0
last_modified_at: 2024-11-07
related_topics:
  - title: English version
    url: /en/common/podman-compose.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/podman-compose.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/podman-compose.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># podman-compose

Compose Specification 컨테이너 정의를 실행하고 관리.
더 많은 정보: <https://github.com/containers/podman-compose>.

- 실행 중인 모든 컨테이너 나열:

`podman-compose ps`

- 로컬 `docker-compose.yml`을 사용하여 백그라운드에서 모든 컨테이너 생성 및 시작:

`podman-compose up -d`

- 필요한 경우 빌드하여 모든 컨테이너 시작:

`podman-compose up --build`

- 다른 컴포즈 파일을 사용하여 모든 컨테이너 시작:

`podman-compose `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-f|--file</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.yaml</span>` up`

- 실행 중인 모든 컨테이너 중지:

`podman-compose stop`

- 모든 컨테이너, 네트워크 및 볼륨 제거:

`podman-compose down --volumes`

- 컨테이너의 로그를 실시간으로 팔로우 (모든 컨테이너 이름 생략):

`podman-compose logs --follow `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">컨테이너_이름</span>

- 포트 매핑 없이 서비스에서 일회성 명령 실행:

`podman-compose run `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">서비스_이름</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">명령</span>
