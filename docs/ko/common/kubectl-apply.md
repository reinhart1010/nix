---
layout: page
title: common/kubectl-apply (한국어)
description: "Kubernetes 리소스를 정의하는 파일을 통해 애플리케이션을 관리하세요."
content_hash: 6e7ab1d0a722c404902da612ff287b898f443b1d
last_modified_at: 2024-10-31
related_topics:
  - title: English version
    url: /en/common/kubectl-apply.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/kubectl-apply.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># kubectl apply

Kubernetes 리소스를 정의하는 파일을 통해 애플리케이션을 관리하세요.
클러스터에서 리소스를 생성하고 업데이트하세요.
더 많은 정보: <https://kubernetes.io/docs/reference/generated/kubectl/kubectl-commands#apply>.

- 파일 이름이나 `stdin`으로 리소스에 설정 적용:

`kubectl apply -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">리소스_파일명</span>

- 기본 편집기를 사용하여 리소스의 최신 마지막 적용 구성 주석 수정:

`kubectl apply edit-last-applied -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">리소스_파일명</span>

- 파일 내용과 일치하도록 설정하여 최신 마지막 적용 구성 주석 설정:

`kubectl apply set-last-applied -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">리소스_파일명</span>

- 유형/이름 또는 파일로 최신 마지막 적용 구성 주석 보기:

`kubectl apply view-last-applied -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">리소스_파일명</span>
