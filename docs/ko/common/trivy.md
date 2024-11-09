---
layout: page
title: common/trivy (한국어)
description: "컨테이너 이미지, 파일 시스템 및 Git 저장소의 취약점과 구성 문제를 스캔하는 도구."
content_hash: 3d427222abb11d43974a1c82ad37d58437c3d27d
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/common/trivy.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/trivy.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># trivy

컨테이너 이미지, 파일 시스템 및 Git 저장소의 취약점과 구성 문제를 스캔하는 도구.
더 많은 정보: <https://aquasecurity.github.io/trivy>.

- Docker 이미지를 취약점 및 노출된 비밀 키에 대해 스캔:

`trivy image `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">이미지:태그</span>

- 심각도에 따라 출력 결과를 필터링하여 Docker 이미지 스캔:

`trivy image --severity `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">HIGH,CRITICAL</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">alpine:3.15</span>

- 수정되지 않거나 패치되지 않은 취약점을 무시하고 Docker 이미지 스캔:

`trivy image --ignore-unfixed `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">alpine:3.15</span>

- 파일 시스템을 취약점 및 잘못된 구성에 대해 스캔:

`trivy fs --security-checks `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">vuln,config</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/프로젝트_폴더</span>

- IaC(Terraform, CloudFormation, ARM, Helm 및 Dockerfile) 디렉토리를 잘못된 구성에 대해 스캔:

`trivy config `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/iac_폴더</span>

- 로컬 또는 원격 Git 저장소를 취약점에 대해 스캔:

`trivy repo `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/로컬_저장소_폴더|원격_저장소_URL</span>

- 특정 커밋 해시까지 Git 저장소 스캔:

`trivy repo --commit `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">커밋_해시</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">저장소</span>

- SARIF 템플릿으로 출력 생성:

`trivy image --format `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">template</span>` --template `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">"@sarif.tpl"</span>` -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/보고서.sarif</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">이미지:태그</span>
