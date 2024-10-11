---
layout: page
title: common/gcloud-container (한국어)
description: "Kubernetes 및 클러스터에서 컨테이너화된 애플리케이션 관리."
content_hash: b7871e3f1e8a198ed4a860072c26078811079901
last_modified_at: 2024-10-11
related_topics:
  - title: English version
    url: /en/common/gcloud-container.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/gcloud-container.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># gcloud container

Kubernetes 및 클러스터에서 컨테이너화된 애플리케이션 관리.
같이 보기: `gcloud`.
더 많은 정보: <https://cloud.google.com/sdk/gcloud/reference/container>.

- `gcloud`를 Docker 자격 증명 도우미로 등록:

`gcloud auth configure-docker`

- GKE 컨테이너를 실행할 클러스터 생성:

`gcloud container clusters create `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">클러스터_이름</span>

- GKE 컨테이너를 실행할 클러스터 나열:

`gcloud container clusters list`

- `kubectl`이 GKE 클러스터를 사용하도록 kubeconfig 업데이트:

`gcloud container clusters get-credentials `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">클러스터_이름</span>

- 컨테이너 이미지의 태그 및 다이제스트 메타데이터 나열:

`gcloud container images list-tags `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">이미지</span>
