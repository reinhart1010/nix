---
layout: page
title: common/kustomize (한국어)
description: "Kubernetes 리소스를 쉽게 배포."
content_hash: 84b69233a073065057b3e3bc2d6f75791f68a81e
last_modified_at: 2024-10-31
related_topics:
  - title: English version
    url: /en/common/kustomize.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/kustomize.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># kustomize

Kubernetes 리소스를 쉽게 배포.
더 많은 정보: <https://github.com/kubernetes-sigs/kustomize>.

- 리소스 및 네임스페이스가 포함된 커스터마이제이션 파일 생성:

`kustomize create --resources `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">deployment.yaml,service.yaml</span>` --namespace `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">staging</span>

- 커스터마이제이션 파일을 빌드하고 `kubectl`로 배포:

`kustomize build . | kubectl apply -f -`

- 커스터마이제이션 파일에 이미지 설정:

`kustomize edit set image `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">busybox=alpine:3.6</span>

- 현재 디렉터리의 Kubernetes 리소스를 검색하여 커스터마이제이션 파일에 추가:

`kustomize create --autodetect`
