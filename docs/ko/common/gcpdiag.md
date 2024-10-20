---
layout: page
title: common/gcpdiag (한국어)
description: "Google Cloud Platform 문제 해결 및 진단 도구."
content_hash: ee0553ba7f6c369ed7bfdf4e23391b589d7fe6d5
last_modified_at: 2024-10-20
related_topics:
  - title: English version
    url: /en/common/gcpdiag.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/gcpdiag.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># gcpdiag

Google Cloud Platform 문제 해결 및 진단 도구.
Docker 컨테이너 또는 GCP Cloudshell에서 실행.
더 많은 정보: <https://github.com/GoogleCloudPlatform/gcpdiag>.

- 프로젝트에서 `gcpdiag`를 실행하고, 모든 규칙을 반환:

`gcpdiag lint --project=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">gcp_프로젝트_아이디</span>

- 괜찮은 규칙 숨기기:

`gcpdiag lint --project=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">gcp_프로젝트_아이디</span>` --hide-ok`

- 서비스 계정 비공개 키 파일을 사용해 인증:

`gcpdiag lint --project=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">gcp_프로젝트_아이디</span>` --auth-key `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/개인_키</span>

- 며칠 전의 로그 및 지표를 검색 (기본값: 3일):

`gcpdiag lint --project=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">gcp_프로젝트_아이디</span>` --within-days `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">숫자</span>

- 도움말 표시:

`gcpdiag lint --help`
