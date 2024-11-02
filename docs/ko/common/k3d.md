---
layout: page
title: common/k3d (한국어)
description: "Docker 내에 k3s 클러스터를 쉽게 생성할 수 있는 래퍼."
content_hash: 5b95811cdba531057fa565a3f95dcb307a928297
last_modified_at: 2024-11-02
related_topics:
  - title: English version
    url: /en/common/k3d.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/k3d.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># k3d

Docker 내에 k3s 클러스터를 쉽게 생성할 수 있는 래퍼.
더 많은 정보: <https://k3d.io>.

- 클러스터 생성:

`k3d cluster create `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">클러스터_이름</span>

- 클러스터 삭제:

`k3d cluster delete `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">클러스터_이름</span>

- 새로운 컨테이너화된 k3s 노드 생성:

`k3d node create `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">노드_이름</span>

- Docker에서 k3d 클러스터로 이미지 가져오기:

`k3d image import `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">이미지_이름</span>` --cluster `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">클러스터_이름</span>

- 새로운 레지스트리 생성:

`k3d registry create `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">레지스트리_이름</span>
