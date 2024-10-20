---
layout: page
title: common/func (한국어)
description: "Azure Functions 핵심 도구: Azure Functions를 로컬에서 개발하고 테스트."
content_hash: f2d4b9438249d6f1ba5d34dfaabccd268245ad65
last_modified_at: 2024-10-20
related_topics:
  - title: English version
    url: /en/common/func.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/func.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># func

Azure Functions 핵심 도구: Azure Functions를 로컬에서 개발하고 테스트.
로컬 함수는 라이브 Azure 서비스에 연결할 수 있고, Azure 구독에 함수 앱을 배포할 수 있음.
더 많은 정보: <https://learn.microsoft.com/azure/azure-functions/functions-run-local>.

- 새로운 함수 프로젝트를 생성:

`func init `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">project</span>

- 새로운 함수 생성:

`func new`

- 로컬에서 함수 실행:

`func start`

- Azure의 함수 앱에 코드를 게시:

`func azure functionapp publish `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">함수</span>

- 기존 함수 앱에서 모든 설정을 다운로드:

`func azure functionapp fetch-app-settings `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">함수</span>

- 특정 스토리지 계정에 대한 연결 문자열을 가져옴:

`func azure storage fetch-connection-string `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">스토리지_계정</span>
