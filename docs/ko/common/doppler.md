---
layout: page
title: common/doppler (한국어)
description: "Doppler를 사용하여 다양한 환경의 환경 변수를 관리."
content_hash: 0ff081491ddbe5b5dd8de0c4158f9a510cdc4bf4
last_modified_at: 2024-10-31
related_topics:
  - title: English version
    url: /en/common/doppler.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/doppler.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/doppler.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># doppler

Doppler를 사용하여 다양한 환경의 환경 변수를 관리.
`run` 및 `secrets`와 같은 일부 하위 명령에는 자체 사용법 문서가 존재.
더 많은 정보: <https://docs.doppler.com/docs/cli>.

- 현재 디렉터리에 Doppler CLI를 설정:

`doppler setup`

- 현재 디렉터리에 Doppler 프로젝트 및 구성을 설정:

`doppler setup`

- 환경에 비밀을 삽입하여 명령을 실행:

`doppler run --command `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">명령어</span>

- 프로젝트 목록 보기:

`doppler projects`

- 현재 프로젝트에 대한 비밀 보기:

`doppler secrets`

- 브라우저에서 Doppler 대시보기를 열기:

`doppler open`
