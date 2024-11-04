---
layout: page
title: windows/get-alias (한국어)
description: "현재 PowerShell 세션에서 명령 별칭을 나열하고 가져옵니다."
content_hash: 265ead4a74368bdf3de49132bb4c42f0e2b0ee9f
last_modified_at: 2024-11-04
related_topics:
  - title: English version
    url: /en/windows/get-alias.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/windows/get-alias.html
    icon: bi bi-globe
tldri18n_status: 2
---
# Get-Alias

현재 PowerShell 세션에서 명령 별칭을 나열하고 가져옵니다.
이 명령은 PowerShell에서만 실행할 수 있습니다.
더 많은 정보: <https://learn.microsoft.com/powershell/module/microsoft.powershell.utility/get-alias>.

- 현재 세션의 모든 별칭 나열:

`Get-Alias`

- 별칭이 가리키는 명령 이름 가져오기:

`Get-Alias `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">명령_별칭</span>

- 특정 명령에 할당된 모든 별칭 나열:

`Get-Alias -Definition `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">명령</span>

- `abc`로 시작하고 `def`로 끝나지 않는 별칭 나열:

`Get-Alias `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">abc</span>`* -Exclude *`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">def</span>
