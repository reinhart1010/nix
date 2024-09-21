---
layout: page
title: common/bru (한국어)
description: "API 탐색 및 테스트를 위한 오픈소스 IDE인 Bruno용 CLI."
content_hash: 53a3e4424937485a9aff653a205e769a695a7c81
last_modified_at: 2024-09-21
related_topics:
  - title: English version
    url: /en/common/bru.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/bru.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/bru.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># bru

API 탐색 및 테스트를 위한 오픈소스 IDE인 Bruno용 CLI.
더 많은 정보: <https://docs.usebruno.com/bru-cli/overview>.

- 현재 디렉터리에서 모든 요청된 파일을 실행:

`bru run`

- 파일 이름을 지정하여, 현재 디렉터리에서 단일 요청을 실행:

`bru run `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file.bru</span>

- 환경 파일을 사용해 요청을 실행:

`bru run --env `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">환경_이름</span>

- 변수가 있는 환경을 사용하여 요청을 실행:

`bru run --env `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">환경_이름</span>` --env-var `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">변수_이름</span>`=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">변수_값</span>

- 요청을 실행하고, 출력 파일에 결과를 수집:

`bru run --output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력.json</span>

- 도움말 표시:

`bru run --help`
