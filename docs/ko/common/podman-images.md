---
layout: page
title: common/podman-images (한국어)
description: "Podman 이미지 관리."
content_hash: 50003557192dea4c2e8b8415c0b9496c9e592fd6
last_modified_at: 2024-11-08
related_topics:
  - title: English version
    url: /en/common/podman-images.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/podman-images.html
    icon: bi bi-globe
tldri18n_status: 2
---
# podman images

Podman 이미지 관리.
더 많은 정보: <https://docs.podman.io/en/latest/markdown/podman-images.1.html>.

- 모든 Podman 이미지 나열:

`podman images`

- 중간 이미지를 포함한 모든 Podman 이미지 나열:

`podman images --all`

- 조용한 모드로 출력 나열 (숫자 ID만 표시):

`podman images --quiet`

- 어떤 컨테이너에서도 사용되지 않는 모든 Podman 이미지 나열:

`podman images --filter dangling=true`

- 이름에 특정 부분 문자열이 포함된 이미지 나열:

`podman images "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">*이미지|이미지*</span>`"`
