---
layout: page
title: common/envoy (한국어)
description: "Laravel 원격 서버를 위한 PHP 기반 작업 관리자."
content_hash: 5464cda6f748d1c06fb3950e1e0b5847eb8e5b01
last_modified_at: 2024-10-17
related_topics:
  - title: English version
    url: /en/common/envoy.html
    icon: bi bi-globe
tldri18n_status: 2
---
# envoy

Laravel 원격 서버를 위한 PHP 기반 작업 관리자.
더 많은 정보: <https://laravel.com/docs/envoy>.

- 구성 파일을 초기화:

`envoy init `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">호스트_파일</span>

- 작업 실행:

`envoy run `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">작업_이름</span>

- 특정 프로젝트에서 작업 실행:

`envoy run --path `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/디렉터리</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">작업_이름</span>

- 작업을 실행하고 실패 시 계속 진행:

`envoy run --continue `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">작업_이름</span>

- 검사를 위해 작업을 Bash 스크립트로 덤프:

`envoy run --pretend `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">작업_이름</span>

- SSH를 통해 지정된 서버에 연결:

`envoy ssh `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">서버_이름</span>
