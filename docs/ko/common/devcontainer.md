---
layout: page
title: common/devcontainer (한국어)
description: "Docker 컨테이너를 개발 환경으로 사용."
content_hash: 555db25836647786a8771181b7a541db2fb1ab29
last_modified_at: 2024-10-12
related_topics:
  - title: English version
    url: /en/common/devcontainer.html
    icon: bi bi-globe
tldri18n_status: 2
---
# devcontainer

Docker 컨테이너를 개발 환경으로 사용.
더 많은 정보: <https://containers.dev/>.

- Dev Container 생성 및 실행:

`devcontainer up`

- 작업 공간에 Dev Container 템플릿을 적용:

`devcontainer templates apply --template-id `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">템플릿_아이디</span>` --template-args `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">템플릿_매개변수</span>` --workspace-folder `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/작업공간</span>

- 현재 작업공간에서 실행 중인 Dev Container에 명령을 실행:

`devcontainer exec `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">명령어</span>

- `devcontainer.json`에서 Dev Container 이미지를 빌드:

`devcontainer build `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/작업공간</span>

- VS Code에서 Dev 컨테이너를 열기 (경로는 선택사항):

`devcontainer open `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/작업공간</span>

- `devcontainer.json`에서 Dev Container의 구성을 읽고 출력:

`devcontainer read-configuration`
