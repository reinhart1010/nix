---
layout: page
title: common/podman-ps (한국어)
description: "Podman 컨테이너 목록을 나열합니다."
content_hash: b008c89f650bd1ff528d4e337c33dd02a2a4197e
last_modified_at: 2024-11-08
related_topics:
  - title: English version
    url: /en/common/podman-ps.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/podman-ps.html
    icon: bi bi-globe
tldri18n_status: 2
---
# podman ps

Podman 컨테이너 목록을 나열합니다.
더 많은 정보: <https://docs.podman.io/en/latest/markdown/podman-ps.1.html>.

- 현재 실행 중인 Podman 컨테이너 나열:

`podman ps`

- 모든 Podman 컨테이너 나열 (실행 중 및 중지된 컨테이너 포함):

`podman ps --all`

- 가장 최근에 생성된 컨테이너 표시 (모든 상태 포함):

`podman ps --latest`

- 이름에 특정 문자열이 포함된 컨테이너 필터링:

`podman ps --filter "name=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">이름</span>`"`

- 주어진 이미지를 조상으로 공유하는 컨테이너 필터링:

`podman ps --filter "ancestor=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">이미지</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">태그</span>`"`

- 종료 상태 코드로 컨테이너 필터링:

`podman ps --all --filter "exited=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">코드</span>`"`

- 상태별로 컨테이너 필터링 (생성됨, 실행 중, 제거 중, 일시 중지됨, 종료됨, 죽은 상태):

`podman ps --filter "status=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">상태</span>`"`

- 특정 볼륨을 마운트했거나 특정 경로에 볼륨이 마운트된 컨테이너 필터링:

`podman ps --filter "volume=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/폴더</span>`" --format "table `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">.ID</span>`\t`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">.Image</span>`\t`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">.Names</span>`\t`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">.Mounts</span>`"`
