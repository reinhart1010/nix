---
layout: page
title: common/quarkus (한국어)
description: "Quarkus 프로젝트 생성, 확장 관리 및 기본 빌드 및 개발 작업 수행."
content_hash: a5b21101dd2eea3cc1787edb4242a08a493cad9a
last_modified_at: 2024-11-02
related_topics:
  - title: English version
    url: /en/common/quarkus.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/quarkus.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/quarkus.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># quarkus

Quarkus 프로젝트 생성, 확장 관리 및 기본 빌드 및 개발 작업 수행.
더 많은 정보: <https://quarkus.io/guides/cli-tooling>.

- 새 디렉토리에 새 애플리케이션 프로젝트 생성:

`quarkus create app `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">프로젝트_명</span>

- 현재 프로젝트를 실시간 코딩 모드로 실행:

`quarkus dev`

- 애플리케이션 실행:

`quarkus run`

- 현재 프로젝트를 지속 테스트 모드로 실행:

`quarkus test`

- 현재 프로젝트에 하나 이상의 확장 추가:

`quarkus extension add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">확장_명1 확장_명2 ...</span>

- Docker를 사용하여 컨테이너 이미지 빌드:

`quarkus image build docker`

- Kubernetes에 애플리케이션 배포:

`quarkus deploy kubernetes`

- 프로젝트 업데이트:

`quarkus update`
