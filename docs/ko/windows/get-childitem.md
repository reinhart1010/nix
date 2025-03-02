---
layout: page
title: windows/get-childitem (한국어)
description: "디렉토리의 항목 나열."
content_hash: 7cac40b09dee2ff1c9d43fcd32644057725be88d
last_modified_at: 2024-11-04
related_topics:
  - title: English version
    url: /en/windows/get-childitem.html
    icon: bi bi-globe
tldri18n_status: 2
---
# Get-ChildItem

디렉토리의 항목 나열.
참고: 이 명령은 PowerShell을 통해서만 사용할 수 있습니다.
더 많은 정보: <https://learn.microsoft.com/powershell/module/microsoft.powershell.management/get-childitem>.

- 현재 디렉토리의 숨겨지지 않은 모든 항목 나열:

`Get-ChildItem`

- 현재 디렉토리의 디렉토리만 나열:

`Get-ChildItem -Directory`

- 현재 디렉토리의 파일만 나열:

`Get-ChildItem -File`

- 숨겨진 항목을 포함하여 현재 디렉토리의 항목 나열:

`Get-ChildItem -Hidden`

- 현재 디렉토리가 아닌 다른 디렉토리의 항목 나열:

`Get-ChildItem -Path `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로\대상\폴더</span>
