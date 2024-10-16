---
layout: page
title: common/doctl-kubernetes-options (한국어)
description: "`doctl`의 Kubernetes 명령에 사용할 수 있는 값을 가져옴."
content_hash: f758dc3b0e6f07fa106259f35db2da734f64a2c1
last_modified_at: 2024-10-16
related_topics:
  - title: English version
    url: /en/common/doctl-kubernetes-options.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/doctl-kubernetes-options.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># doctl kubernetes options

`doctl`의 Kubernetes 명령에 사용할 수 있는 값을 가져옴.
더 많은 정보: <https://docs.digitalocean.com/reference/doctl/reference/kubernetes/options/>.

- Kubernetes 클러스터를 지원하는 지역 목록 나열:

`doctl kubernetes options regions`

- Kubernetes 클러스터에서 사용할 수 있는 머신 크기를 나열:

`doctl kubernetes options sizes`

- DigitalOcean 클러스터와 함께 사용할 수 있는 Kubernetes 버전을 나열:

`doctl kubernetes options versions`
