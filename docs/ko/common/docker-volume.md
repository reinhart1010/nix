---
layout: page
title: common/docker-volume (한국어)
description: "Docker 볼륨 관리."
content_hash: cd02da0c9018b8bf00e0d323a562fd5fba5ee285
last_modified_at: 2024-10-11
related_topics:
  - title: English version
    url: /en/common/docker-volume.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/docker-volume.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/docker-volume.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/docker-volume.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># docker volume

Docker 볼륨 관리.
더 많은 정보: <https://docs.docker.com/reference/cli/docker/volume/>.

- 볼륨 생성:

`docker volume create `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">볼륨_이름</span>

- 특정 레이블을 사용하여 볼륨 생성:

`docker volume create --label `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">레이블</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">볼륨_이름</span>

- 100 MiB의 크기와 1000의 uid를 가진 `tmpfs` 볼륨 생성:

`docker volume create --opt `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">type</span>`=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">tmpfs</span>` --opt `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">device</span>`=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">tmpfs</span>` --opt `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">o</span>`=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">size=100m,uid=1000</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">볼륨_이름</span>

- 모든 볼륨 나열:

`docker volume ls`

- 볼륨 제거:

`docker volume rm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">볼륨_이름</span>

- 볼륨에 대한 정보 표시:

`docker volume inspect `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">볼륨_이름</span>

- 사용되지 않는 모든 로컬 볼륨 제거:

`docker volume prune`

- 하위 명령에 대한 도움말 표시:

`docker volume `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">서브커맨드</span>` --help`
