---
layout: page
title: common/k9s (한국어)
description: "Kubernetes 클러스터를 보고 관리."
content_hash: ec9526abb767a635c8c3616b8a718cee09f5fb88
last_modified_at: 2024-11-02
related_topics:
  - title: English version
    url: /en/common/k9s.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/k9s.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># k9s

Kubernetes 클러스터를 보고 관리.
더 많은 정보: <https://k9scli.io/topics/commands/>.

- kubeconfig 컨텍스트를 사용하여 클러스터 관리:

`k9s --context `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">kubeconfig_컨텍스트_이름</span>

- 읽기 전용 모드로 클러스터 관리 (수정을 초래할 수 있는 모든 명령 비활성화):

`k9s --readonly --cluster `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">클러스터_이름</span>

- 주어진 Kubernetes 네임스페이스를 사용하여 클러스터 관리:

`k9s --namespace `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Kubernetes_네임스페이스</span>` --cluster `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">클러스터_이름</span>

- pod 보기로 k9s를 실행하고 디버그 로깅을 활성화하여 클러스터 관리:

`k9s --command `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pod</span>` --logLevel debug --cluster `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">클러스터_이름</span>
