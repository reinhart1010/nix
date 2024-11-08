---
layout: page
title: common/podman-build (한국어)
description: "컨테이너 이미지를 빌드하기 위한 데몬리스 도구."
content_hash: 9f5308fc45be8749f1918fb0e04e105637b5f966
last_modified_at: 2024-11-08
related_topics:
  - title: English version
    url: /en/common/podman-build.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/podman-build.html
    icon: bi bi-globe
tldri18n_status: 2
---
# podman build

컨테이너 이미지를 빌드하기 위한 데몬리스 도구.
Podman은 Docker-CLI와 유사한 명령줄을 제공합니다. 간단히 말해: `alias docker=podman`.
더 많은 정보: <https://docs.podman.io/en/latest/markdown/podman-build.1.html>.

- 지정된 디렉토리의 `Dockerfile` 또는 `Containerfile`을 사용하여 이미지 생성:

`podman build `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/폴더</span>

- 지정된 태그로 이미지 생성:

`podman build --tag `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">이미지_이름:버전</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/폴더</span>

- 비표준 파일에서 이미지 생성:

`podman build --file `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Containerfile.different</span>` .`

- 이전에 캐시된 이미지를 사용하지 않고 이미지 생성:

`podman build --no-cache `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/폴더</span>

- 모든 출력을 억제하여 이미지 생성:

`podman build --quiet `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/폴더</span>
