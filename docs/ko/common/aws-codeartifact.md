---
layout: page
title: common/aws-codeartifact (한국어)
description: "CodeArtifact 리포지토리, 도메인, 패키지, 패키지 버전 및 자산을 관리."
content_hash: 90019210351d45180f02d2e61b70df45484b4f96
last_modified_at: 2024-09-21
related_topics:
  - title: English version
    url: /en/common/aws-codeartifact.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/aws-codeartifact.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/aws-codeartifact.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># aws codeartifact

CodeArtifact 리포지토리, 도메인, 패키지, 패키지 버전 및 자산을 관리.
CodeArtifact는 인기 있는 패키지 관리자 및 Maven, Gradle, npm, Yarn, Twine, pip, NuGet 및 SwiftPM과 같은 빌드 도구와 호환되는 아티팩트 리포지토리.
더 많은 정보: <https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codeartifact/index.html>.

- AWS 계정에 사용 가능한 도메인 나열:

`aws codeartifact list-domains`

- 특정 패키지 관리자에 대한 자격 증명 생성:

`aws codeartifact login --tool `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">npm|pip|twine</span>` --domain `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">_도메인</span>` --repository `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">레포지토리_이름</span>

- CodeArtifact 레포지토리의 엔드포인트 URL 가져오기:

`aws codeartifact get-repository-endpoint --domain `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">your_domain</span>` --repository `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">레포지토리_이름</span>` --format `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">npm|pypi|maven|nuget|generic</span>

- 도움말 표시:

`aws codeartifact help`

- 특정 하위 명령어에 대한 도움말 표시:

`aws codeartifact `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">subcommand</span>` help`
