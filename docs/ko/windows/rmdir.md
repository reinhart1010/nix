---
layout: page
title: windows/rmdir (한국어)
description: "디렉토리와 그 내용을 삭제합니다."
content_hash: 9d94f6f305400dcf5efe2d5e949721aa0bba8933
last_modified_at: 2024-10-25
related_topics:
  - title: English version
    url: /en/windows/rmdir.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/windows/rmdir.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/windows/rmdir.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/windows/rmdir.html
    icon: bi bi-globe
  - title: 中文 (繁體, 台灣) version
    url: /zh_TW/windows/rmdir.html
    icon: bi bi-globe
tldri18n_status: 2
---
# rmdir

디렉토리와 그 내용을 삭제합니다.
PowerShell에서 이 명령어는 `Remove-Item`의 별칭입니다. 이 문서는 명령 프롬프트(`cmd`) 버전의 `rmdir`를 기반으로 합니다.
더 많은 정보: <https://learn.microsoft.com/windows-server/administration/windows-commands/rmdir>.

- 해당 PowerShell 명령어의 문서 보기:

`tldr remove-item`

- 빈 디렉토리 삭제:

`rmdir `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로\대상\디렉토리</span>

- 디렉토리와 그 내용 재귀적으로 삭제:

`rmdir `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로\대상\디렉토리</span>` /s`

- 디렉토리와 그 내용을 프롬프트 없이 재귀적으로 삭제:

`rmdir `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로\대상\디렉토리</span>` /s /q`
