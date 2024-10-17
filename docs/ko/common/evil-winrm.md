---
layout: page
title: common/evil-winrm (한국어)
description: "침투 테스트를 위한 WinRM(Windows 원격 관리 쉘)."
content_hash: 4b58ab2cd2c7f06a1e8f2f281151e2249837c6a8
last_modified_at: 2024-10-17
related_topics:
  - title: English version
    url: /en/common/evil-winrm.html
    icon: bi bi-globe
tldri18n_status: 2
---
# evil-winrm

침투 테스트를 위한 WinRM(Windows 원격 관리 쉘).
연결되면, 대상 호스트에 PowerShell 프롬프트가 표시됨.
더 많은 정보: <https://github.com/Hackplayers/evil-winrm>.

- 호스트에 연결:

`evil-winrm --ip `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">아이피</span>` --user `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">사용자</span>` --password `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">비밀번호</span>

- 비밀번호 해시를 전달하여 호스트에 연결:

`evil-winrm --ip `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">아이피</span>` --user `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">사용자</span>` --hash `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nt_hash</span>

- 스크립트 및 실행 파일에 대한 디렉터리를 지정하여 호스트에 연결:

`evil-winrm --ip `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">아이피</span>` --user `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">사용자</span>` --password `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">비밀번호</span>` --scripts `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/스크립트</span>` --executables `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/실행파일</span>

- SSL을 사용하여 호스트에 연결:

`evil-winrm --ip `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">아이피</span>` --user `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">사용자</span>` --password `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">비밀번호</span>` --ssl --pub-key `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/공개키</span>` --priv-key `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/개인키</span>

- 호스트에 파일 업로드:

`PS > upload `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/로컬/파일</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/원격/파일</span>

- 로드된 모든 PowerShell 함수를 나열:

`PS > menu`

- `--scripts` 디렉터리에서 PowerShell 스크립트를 로드:

`PS > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">스크립트.ps1</span>

- `--executables` 디렉터리에서 호스트의 바이너리를 호출:

`PS > Invoke-Binary `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">바이너리.exe</span>
