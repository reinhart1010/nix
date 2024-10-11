---
layout: page
title: common/docker-inspect (한국어)
description: "Docker 객체에 대한 저수준 정보를 반환."
content_hash: 7b48fdb5fc9efd80e67375ce50bbe1637f60d56d
last_modified_at: 2024-10-11
related_topics:
  - title: Deutsch version
    url: /de/common/docker-inspect.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/docker-inspect.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/docker-inspect.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/docker-inspect.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/docker-inspect.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/docker-inspect.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/docker-inspect.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># docker inspect

Docker 객체에 대한 저수준 정보를 반환.
더 많은 정보: <https://docs.docker.com/reference/cli/docker/inspect/>.

- 도움말 표시:

`docker inspect`

- 이름 또는 ID를 사용하여 컨테이너, 이미지 또는 볼륨에 대한 정보 표시:

`docker inspect `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">컨테이너|이미지|ID</span>

- 컨테이너의 IP 주소 표시:

`docker inspect --format '\{\{range.NetworkSettings.Networks\}\}\{\{.IPAddress\}\}\{\{end\}\}' `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">컨테이너</span>

- 컨테이너의 로그 파일 경로 표시:

`docker inspect --format='\{\{.LogPath\}\}' `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">컨테이너</span>

- 컨테이너의 이미지 이름 표시:

`docker inspect --format='\{\{.Config.Image\}\}' `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">컨테이너</span>

- JSON 형식으로 구성 정보 표시:

`docker inspect --format='\{\{json .Config\}\}' `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">컨테이너</span>

- 모든 포트 바인딩 표시:

`docker inspect --format='\{\{range $p, $conf := .NetworkSettings.Ports\}\} \{\{$p\}\} -> \{\{(index $conf 0).HostPort\}\} \{\{end\}\}' `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">컨테이너</span>
