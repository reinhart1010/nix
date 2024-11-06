---
layout: page
title: windows/gpupdate (한국어)
description: "Windows 그룹 정책 설정을 확인하고 적용합니다."
content_hash: 1c5c144e0e8a2bd5f6607d893ee4ecfb0bcfa5d6
last_modified_at: 2024-11-06
related_topics:
  - title: English version
    url: /en/windows/gpupdate.html
    icon: bi bi-globe
  - title: svenska version
    url: /sv/windows/gpupdate.html
    icon: bi bi-globe
tldri18n_status: 2
---
# gpupdate

Windows 그룹 정책 설정을 확인하고 적용합니다.
더 많은 정보: <https://learn.microsoft.com/windows-server/administration/windows-commands/gpupdate>.

- 업데이트된 그룹 정책 설정 확인 및 적용:

`gpupdate`

- 업데이트할 그룹 정책 설정 지정:

`gpupdate /target:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">computer|user</span>

- 모든 그룹 정책 설정 재적용:

`gpupdate /force`

- 도움말 표시:

`gpupdate /?`
