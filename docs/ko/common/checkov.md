---
layout: page
title: common/checkov (한국어)
description: "Checkov는 IaC(Infrastructure as Code)를 위한 정적 코드 분석 도구."
content_hash: 1802d3ae5ceb7307e9560f7001e6f0fdeaa93441
last_modified_at: 2024-09-30
related_topics:
  - title: English version
    url: /en/common/checkov.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/checkov.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/checkov.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># checkov

Checkov는 IaC(Infrastructure as Code)를 위한 정적 코드 분석 도구.
이미지 및 오픈소스 패키지를 위한 SCA(소프트웨어 구성 분석) 도구.
더 많은 정보: <https://www.checkov.io/1.Welcome/Quick%20Start.html>.

- IaC(Terraform, Cloudformation, ARM, Ansible, Bicep, Dockerfile 등)가 포함된 디렉터리를 스캔:

`checkov --directory `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/디렉터리</span>

- 출력에서 코드 블록을 생략하고 IaC 파일을 스캔:

`checkov --compact --file `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- 모든 IaC 유형에 대한 모든 검사를 나열:

`checkov --list`
