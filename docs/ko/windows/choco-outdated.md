---
layout: page
title: windows/choco-outdated (한국어)
description: "Chocolatey를 사용하여 업데이트가 필요한 패키지 확인."
content_hash: 3d31961b87b01a25e7acb759fc07afcf5813ee50
last_modified_at: 2024-10-15
related_topics:
  - title: Deutsch version
    url: /de/windows/choco-outdated.html
    icon: bi bi-globe
  - title: English version
    url: /en/windows/choco-outdated.html
    icon: bi bi-globe
  - title: français version
    url: /fr/windows/choco-outdated.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/windows/choco-outdated.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/windows/choco-outdated.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/windows/choco-outdated.html
    icon: bi bi-globe
tldri18n_status: 2
---
# choco outdated

Chocolatey를 사용하여 업데이트가 필요한 패키지 확인.
더 많은 정보: <https://chocolatey.org/docs/commands-outdated>.

- 표 형식으로 업데이트가 필요한 패키지 목록 표시:

`choco outdated`

- 고정된 패키지를 출력에서 무시:

`choco outdated --ignore-pinned`

- 패키지를 확인할 사용자 지정 소스 지정:

`choco outdated --source `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">source_url|alias</span>

- 인증을 위한 사용자 명과 비밀번호 제공:

`choco outdated --user `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">사용자_명</span>` --password `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">비밀번호</span>
