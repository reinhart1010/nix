---
layout: page
title: common/jhipster (한국어)
description: "모놀리식 또는 마이크로서비스 아키텍처를 사용하는 웹 애플리케이션 생성기."
content_hash: dc84d67a321e8d768132d730b7b1cd5985eb4555
last_modified_at: 2024-11-05
related_topics:
  - title: English version
    url: /en/common/jhipster.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/jhipster.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># jhipster

모놀리식 또는 마이크로서비스 아키텍처를 사용하는 웹 애플리케이션 생성기.
더 많은 정보: <https://www.jhipster.tech/>.

- 간단한 풀스택 프로젝트 생성 (모놀리식 또는 마이크로서비스):

`jhipster`

- 간단한 프론트엔드 프로젝트 생성:

`jhipster --skip-server`

- 간단한 백엔드 프로젝트 생성:

`jhipster --skip-client`

- 프로젝트에 최신 JHipster 업데이트 적용:

`jhipster upgrade`

- 생성된 프로젝트에 새로운 엔티티 추가:

`jhipster entity `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">엔티티_이름</span>

- JDL 파일을 가져와 애플리케이션 구성 (참고: <https://start.jhipster.tech/jdl-studio/>):

`jhipster import-jdl `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">첫번째_파일.jh 두번째_파일.jh ... n번째_파일.jh</span>

- 애플리케이션을 위한 CI/CD 파이프라인 생성:

`jhipster ci-cd`

- 애플리케이션을 위한 Kubernetes 구성 생성:

`jhipster kubernetes`
