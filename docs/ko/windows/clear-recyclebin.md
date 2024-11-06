---
layout: page
title: windows/clear-recyclebin (한국어)
description: "휴지통의 항목을 삭제."
content_hash: 5c5b9eca4920786ddac635c5edba3574ec810e1d
last_modified_at: 2024-11-06
related_topics:
  - title: English version
    url: /en/windows/clear-recyclebin.html
    icon: bi bi-globe
tldri18n_status: 2
---
# Clear-RecycleBin

휴지통의 항목을 삭제.
이 명령은 PowerShell 버전 5.1 이하 또는 7.1 이상에서만 사용할 수 있습니다.
더 많은 정보: <https://learn.microsoft.com/powershell/module/microsoft.powershell.management/clear-recyclebin>.

- 휴지통의 모든 항목 삭제:

`Clear-RecycleBin`

- 특정 드라이브의 휴지통 삭제:

`Clear-RecycleBin -DriveLetter `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">C</span>

- 추가 확인 없이 휴지통 삭제:

`Clear-RecycleBin -Force`
