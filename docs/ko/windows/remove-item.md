---
layout: page
title: windows/remove-item (한국어)
description: "파일, 폴더, 레지스트리 키 및 하위 키를 삭제합니다."
content_hash: f0848e60e90bdec272373b235d3d5766e6c879dc
last_modified_at: 2024-11-12
related_topics:
  - title: English version
    url: /en/windows/remove-item.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/windows/remove-item.html
    icon: bi bi-globe
tldri18n_status: 2
---
# Remove-Item

파일, 폴더, 레지스트리 키 및 하위 키를 삭제합니다.
이 명령어는 PowerShell을 통해서만 사용할 수 있습니다.
더 많은 정보: <https://learn.microsoft.com/powershell/module/microsoft.powershell.management/remove-item>.

- 특정 파일 또는 레지스트리 키 삭제 (하위 키 없음):

`Remove-Item `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로\대상\파일_또는_키1 , 경로\대상\파일_또는_키2 ...</span>

- 숨김 또는 읽기 전용 파일 삭제:

`Remove-Item -Force `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로\대상\파일1 , 경로\대상\파일2 ...</span>

- 특정 파일 또는 레지스트리 키를 각 삭제 전에 확인 메시지를 표시:

`Remove-Item -Confirm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로\대상\파일_또는_키1 , 경로\대상\파일_또는_키2 ...</span>

- 특정 파일 및 디렉토리를 재귀적으로 삭제 (Windows 10 버전 1909 이상):

`Remove-Item -Recurse `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로\대상\파일_또는_디렉토리1 , 경로\대상\파일_또는_디렉토리2 ...</span>

- 특정 Windows 레지스트리 키 및 모든 하위 키 삭제:

`Remove-Item -Recurse `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로\대상\키1 , 경로\대상\키2 ...</span>

- 삭제 프로세스를 건너뛰고 예상 실행 결과 표시:

`Remove-Item -WhatIf `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로\대상\파일1 , 경로\대상\파일2 ...</span>
