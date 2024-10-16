---
layout: page
title: common/etcd (한국어)
description: "분산 시스템의 가장 중요한 데이터를 위한, 신뢰할 수 있는 분산 키-값 저장소."
content_hash: e7180b4454bece811fd602ebfe26127a578af12d
last_modified_at: 2024-10-16
related_topics:
  - title: English version
    url: /en/common/etcd.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/etcd.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/etcd.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># etcd

분산 시스템의 가장 중요한 데이터를 위한, 신뢰할 수 있는 분산 키-값 저장소.
더 많은 정보: <https://etcd.io>.

- 단일 노드 etcd 클러스터를 시작:

`etcd`

- 단일 노드 etcd 클러스터를 시작하고, 사용자 정의 URL에서 클라이언트 요청을 수신:

`etcd --advertise-client-urls `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">http://127.0.0.1:1234</span>` --listen-client-urls `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">http://127.0.0.1:1234</span>

- 사용자 정의 이름으로 단일 노드 etcd 클러스터를 시작:

`etcd --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">내_etcd_클러스터</span>

- <http://localhost:2379/debug/pprof/>에서 사용할 수 있는 광범위한 측정항목을 사용하여, 단일 노드 etcd 클러스터를 시작:

`etcd --enable-pprof --metrics extensive`
