---
layout: page
title: linux/wine (한국어)
description: "Unix 기반 시스템에서 Windows 실행 파일을 실행."
content_hash: 03016905e0a54721de0bd288d94565dd7095557a
last_modified_at: 2024-11-10
related_topics:
  - title: English version
    url: /en/linux/wine.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/linux/wine.html
    icon: bi bi-globe
tldri18n_status: 2
---
# wine

Unix 기반 시스템에서 Windows 실행 파일을 실행.
더 많은 정보: <https://wiki.winehq.org/>.

- `wine` 환경에서 특정 프로그램 실행:

`wine `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">명령어</span>

- 백그라운드에서 특정 프로그램 실행:

`wine start `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">명령어</span>

- MSI 패키지 설치/제거:

`wine msiexec /`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">i|x</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/패키지.msi</span>

- `파일 탐색기`, `메모장`, 또는 `워드패드` 실행:

`wine `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">explorer|notepad|write</span>

- `레지스트리 편집기`, `제어판`, 또는 `작업 관리자` 실행:

`wine `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">regedit|control|taskmgr</span>

- 설정 도구 실행:

`wine winecfg`
