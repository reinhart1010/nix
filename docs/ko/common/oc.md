---
layout: page
title: common/oc (한국어)
description: "OpenShift 컨테이너 플랫폼 CLI."
content_hash: 3d349c04ee1ec9a602b76cc73c7d74c3610239e6
last_modified_at: 2024-11-05
related_topics:
  - title: English version
    url: /en/common/oc.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/oc.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># oc

OpenShift 컨테이너 플랫폼 CLI.
애플리케이션 및 컨테이너 관리를 허용합니다.
더 많은 정보: <https://docs.openshift.com/container-platform/3.11/cli_reference/get_started_cli.html>.

- OpenShift 컨테이너 플랫폼 서버에 로그인:

`oc login`

- 새 프로젝트 생성:

`oc new-project `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">프로젝트_이름</span>

- 기존 프로젝트로 전환:

`oc project `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">프로젝트_이름</span>

- 프로젝트에 새 애플리케이션 추가:

`oc new-app `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">저장소_URL</span>` --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">애플리케이션</span>

- 컨테이너에 원격 셸 세션 열기:

`oc rsh `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">포드_이름</span>

- 프로젝트 내 포드 나열:

`oc get pods`

- 현재 세션에서 로그아웃:

`oc logout`
