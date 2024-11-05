---
layout: page
title: windows/invoke-item (한국어)
description: "파일을 기본 프로그램에서 엽니다."
content_hash: 45550129a5b7924035e9b4f93928a9c259ea3999
last_modified_at: 2024-11-05
related_topics:
  - title: English version
    url: /en/windows/invoke-item.html
    icon: bi bi-globe
tldri18n_status: 2
---
# Invoke-Item

파일을 기본 프로그램에서 엽니다.
참고: 이 명령어는 PowerShell을 통해서만 사용할 수 있습니다.
더 많은 정보: <https://learn.microsoft.com/powershell/module/microsoft.powershell.management/invoke-item>.

- 파일을 기본 프로그램에서 열기:

`Invoke-Item -Path `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로\대상\파일</span>

- 디렉토리 내의 모든 파일 열기:

`Invoke-Item -Path `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로\대상\디렉토리</span>`\*`

- 디렉토리 내의 모든 PNG 파일 열기:

`Invoke-Item -Path `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로\대상\디렉토리</span>`\*.png`

- 특정 키워드가 포함된 디렉토리 내의 모든 파일 열기:

`Invoke-Item -Path `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로\대상\디렉토리</span>`\* -Include `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">*키워드*</span>

- 특정 키워드를 포함하는 파일을 제외한 디렉토리 내부의 모든 파일을 열기:

`Invoke-Item -Path `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로\대상\디렉토리</span>`\* -Exclude `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">*키워드*</span>

- `Invoke-Item`을 통해 디렉토리 내부에서 어떤 파일이 열릴지 확인하기 위한 테스트 실행:

`Invoke-Item -Path `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로\대상\디렉토리</span>`\* -WhatIf`
