---
layout: page
title: windows/resolve-path (한국어)
description: "경로에서 와일드카드 문자를 확인하고 경로 내용을 표시합니다."
content_hash: 7866c666c99e2ff68f6f09c04e9c3a7b15b298ac
last_modified_at: 2024-10-26
related_topics:
  - title: English version
    url: /en/windows/resolve-path.html
    icon: bi bi-globe
tldri18n_status: 2
---
# Resolve-Path

경로에서 와일드카드 문자를 확인하고 경로 내용을 표시합니다.
참고: 이 명령어는 PowerShell을 통해서만 사용할 수 있습니다.
더 많은 정보: <https://learn.microsoft.com/powershell/module/microsoft.powershell.management/resolve-path>.

- 홈 폴더 경로 확인:

`Resolve-Path `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">~</span>

- UNC 경로 확인:

`Resolve-Path -Path "\\`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">호스트명</span>`\`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로\대상\파일</span>`"`

- 상대 경로 확인:

`Resolve-Path -Path `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로\대상\파일_또는_디렉토리</span>` -Relative`
