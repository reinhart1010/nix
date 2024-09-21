---
layout: page
title: common/az-repos (한국어)
description: "Azure DevOps 레포지토리를 관리."
content_hash: 34a974be2fa3c143f1287f8a1387d6d70abb406e
last_modified_at: 2024-09-21
related_topics:
  - title: English version
    url: /en/common/az-repos.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/az-repos.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># az repos

Azure DevOps 레포지토리를 관리.
`azure-cli`의 일부 (`az`라고도 함).
더 많은 정보: <https://learn.microsoft.com/cli/azure/repos>.

- 특정 프로젝트의 모든 저장소 나열:

`az repos list --project `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">프로젝트_이름</span>

- 특정 저장소의 특정 분기에 정책을 추가해, 기본 병합을 제한:

`az repos policy merge-strategy create --repository-id `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">저장소_목록_내부_레포지토리</span>` --branch `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">브랜치_이름</span>` --blocking --enabled --allow-no-fast-forward false --allow-rebase true --allow-rebase-merge true --allow-squash true`

- 소스 업데이트 할때 자동으로 추적되도록 기존 빌드 파이프라인을 사용하여, 특정 저장소에 빌드 유효성 검사를 추가:

`az repos policy build create --repository-id `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">레포지토리_아이디</span>` --build-definition-id `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">빌드_파이프라인_아이디</span>` --branch main --blocking --enabled --queue-on-source-update-only true --display-name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">이름</span>` --valid-duration `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">분</span>

- 특정 프로젝트 내의 특정 저장소의 모든 활성 끌어오기 요청을 나열:

`az repos pr list --project `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">프로젝트_이름</span>` --repository `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">레포지토리_이름</span>` --status active`
