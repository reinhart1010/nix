---
layout: page
title: common/kompose (한국어)
description: "Docker Compose 애플리케이션을 Kubernetes로 변환."
content_hash: 39e54956df85cc975882687f1ef330c8f8f1f409
last_modified_at: 2024-11-02
related_topics:
  - title: English version
    url: /en/common/kompose.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/kompose.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># kompose

Docker Compose 애플리케이션을 Kubernetes로 변환.
더 많은 정보: <https://github.com/kubernetes/kompose>.

- 도커화된 애플리케이션을 Kubernetes에 배포:

`kompose up -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">docker-compose.yml</span>

- Kubernetes에서 서비스/배포 인스턴스 삭제:

`kompose down -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">docker-compose.yml</span>

- docker-compose 파일을 Kubernetes 리소스 파일로 변환:

`kompose convert -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">docker-compose.yml</span>
