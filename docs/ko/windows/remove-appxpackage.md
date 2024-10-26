---
layout: page
title: windows/remove-appxpackage (한국어)
description: "사용자 계정에서 앱 패키지를 제거하는 PowerShell 유틸리티입니다."
content_hash: a849ec9b7661c17c03eb302daa89bdf1fc28eda9
last_modified_at: 2024-10-26
related_topics:
  - title: English version
    url: /en/windows/remove-appxpackage.html
    icon: bi bi-globe
tldri18n_status: 2
---
# Remove-AppxPackage

사용자 계정에서 앱 패키지를 제거하는 PowerShell 유틸리티입니다.
더 많은 정보: <https://learn.microsoft.com/powershell/module/appx/Remove-AppxPackage>.

- 앱 패키지 삭제:

`Remove-AppxPackage `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">패키지</span>

- 특정 사용자에 대한 앱 패키지 삭제:

`Remove-AppxPackage `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">패키지</span>` -User `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">사용자명</span>

- 모든 사용자에 대한 앱 패키지 삭제:

`Remove-AppxPackage `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">패키지</span>` -AllUsers`

- 앱 패키지를 제거하지만 앱 데이터는 보존:

`Remove-AppxPackage `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">패키지</span>` -PreserveApplicationData`
