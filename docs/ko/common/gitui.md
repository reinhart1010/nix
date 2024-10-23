---
layout: page
title: common/gitui (한국어)
description: "Git용 경량 키보드 전용 TUI."
content_hash: 7eefc642e1b498f401ec321de3968cb92ce09836
last_modified_at: 2024-10-23
related_topics:
  - title: English version
    url: /en/common/gitui.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/gitui.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># gitui

Git용 경량 키보드 전용 TUI.
참고: `tig`, `git-gui`.
더 많은 정보: <https://github.com/extrawurst/gitui>.

- 색상 테마를 지정 (기본값은 `theme.ron`):

`gitui --theme `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">테마</span>

- 로깅 출력을 캐시 디렉터리에 저장:

`gitui --logging`

- tick 기반 업데이트 대신, 알림 기반 파일 시스템 감시자를 사용:

`gitui --watcher`

- 버그 리포트를 생성:

`gitui --bugreport`

- 특정 Git 레포지토리 사용:

`gitui --directory `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/디렉터리</span>

- 특정 작업 디렉터리 사용:

`gitui --workdir `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/디렉터리</span>

- 도움말 표시:

`gitui --help`

- 버전 정보 표시:

`gitui --version`
