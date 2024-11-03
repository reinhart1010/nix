---
layout: page
title: windows/net (한국어)
description: "네트워크 관련 설정을 보고 수정하는 시스템 유틸리티입니다."
content_hash: 8051b30c3130f8394d4471791ba931b364c6d1df
last_modified_at: 2024-11-03
related_topics:
  - title: বাংলা version
    url: /bn/windows/net.html
    icon: bi bi-globe
  - title: English version
    url: /en/windows/net.html
    icon: bi bi-globe
tldri18n_status: 2
---
# net

네트워크 관련 설정을 보고 수정하는 시스템 유틸리티입니다.
더 많은 정보: <https://learn.microsoft.com/previous-versions/windows/it-pro/windows-server-2012-r2-and-2012/gg651155(v=ws.11)>.

- 동기적으로 Windows 서비스 시작 또는 중지:

`net `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">start|stop</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">서비스</span>

- 현재 콘솔에서 SMB 공유 가능한지 확인:

`net use `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">\\smb_shared_folder</span>` /USER:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">사용자명</span>

- 현재 SMB로 공유되는 폴더 표시:

`net share`

- SMB 공유를 사용하는 사용자 표시 (관리자 권한 콘솔에서 실행):

`net session`

- 로컬 보안 그룹의 사용자 표시:

`net localgroup "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Administrators</span>`"`

- 로컬 보안 그룹에 사용자 추가 (관리자 권한 콘솔에서 실행):

`net localgroup "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Administrators</span>`" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">사용자명</span>` /add`

- 하위 명령에 대한 도움말 표시:

`net help `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">하위명령</span>

- 도움말 표시:

`net help`
