---
layout: page
title: windows/add-appxpackage (한국어)
description: "서명된 앱 패키지(`.appx`, `.msix`, `.appxbundle`, `.msixbundle`)를 사용자 계정에 추가하는 PowerShell 유틸리티."
content_hash: a46b0123ec89f2d85d404c0f5319b27c8e3263b0
last_modified_at: 2024-11-06
related_topics:
  - title: English version
    url: /en/windows/add-appxpackage.html
    icon: bi bi-globe
  - title: हिन्दी version
    url: /hi/windows/add-appxpackage.html
    icon: bi bi-globe
tldri18n_status: 2
---
# Add-AppxPackage

서명된 앱 패키지(`.appx`, `.msix`, `.appxbundle`, `.msixbundle`)를 사용자 계정에 추가하는 PowerShell 유틸리티.
더 많은 정보: <https://learn.microsoft.com/powershell/module/appx/Add-AppxPackage>.

- 앱 패키지 추가:

`Add-AppxPackage -Path `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로\대상\패키지.msix</span>

- 의존성과 함께 앱 패키지 추가:

`Add-AppxPackage -Path `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로\대상\패키지.msix</span>` -DependencyPath `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로\대상\의존성.msix</span>

- 앱 설치 파일을 사용하여 앱 설치:

`Add-AppxPackage -AppInstallerFile `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로\대상\앱.appinstaller</span>

- 서명되지 않은 패키지 추가:

`Add-AppxPackage -Path `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로\대상\패키지.msix</span>` -DependencyPath `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로\대상\의존성.msix</span>` -AllowUnsigned`
