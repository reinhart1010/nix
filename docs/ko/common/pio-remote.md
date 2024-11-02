---
layout: page
title: common/pio-remote (한국어)
description: "PlatformIO 원격 개발을 위한 보조 명령어."
content_hash: 6022b244d4ba764483af1ca600dff2e28d9a7247
last_modified_at: 2024-11-02
related_topics:
  - title: English version
    url: /en/common/pio-remote.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/pio-remote.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/pio-remote.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># pio remote

PlatformIO 원격 개발을 위한 보조 명령어.
`pio remote [command]`는 로컬에서 실행되는 `pio [command]`와 동일한 인수를 사용합니다.
더 많은 정보: <https://docs.platformio.org/en/latest/core/userguide/remote/index.html>.

- 활성화된 모든 원격 에이전트 나열:

`pio remote agent list`

- 특정 이름으로 새로운 원격 에이전트를 시작하고 친구들과 공유:

`pio remote agent start --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">에이전트_이름</span>` --share `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example1@example.com</span>` --share `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example2@example.com</span>

- 지정된 에이전트의 장치 나열 (`--agent`를 생략하여 모든 에이전트 지정 가능):

`pio remote --agent `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">에이전트_이름1</span>` --agent `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">에이전트_이름2</span>` device list`

- 원격 장치의 직렬 포트에 연결:

`pio remote --agent `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">에이전트_이름</span>` device monitor`

- 지정된 에이전트에서 모든 타겟 실행:

`pio remote --agent `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">에이전트_이름</span>` run`

- 특정 에이전트에서 설치된 코어 패키지, 개발 플랫폼 및 전역 라이브러리 업데이트:

`pio remote --agent `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">에이전트_이름</span>` update`

- 특정 에이전트에서 모든 환경의 모든 테스트 실행:

`pio remote --agent `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">에이전트_이름</span>` test`
