---
layout: page
title: windows/psexec (한국어)
description: "원격 컴퓨터에서 명령줄 프로세스 실행."
content_hash: 920d2a20b80203abd6b988885c1c036c74f5317f
last_modified_at: 2024-10-31
related_topics:
  - title: English version
    url: /en/windows/psexec.html
    icon: bi bi-globe
tldri18n_status: 2
---
# psexec

원격 컴퓨터에서 명령줄 프로세스 실행.
이 명령은 고급 명령이며 잠재적으로 위험할 수 있습니다.
더 많은 정보: <https://learn.microsoft.com/sysinternals/downloads/psexec>.

- 원격 쉘에서 `cmd`를 사용하여 명령 실행:

`psexec \\`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">원격_호스트</span>` cmd`

- 원격 호스트에서 명령 실행 (사전 인증됨):

`psexec \\`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">원격_호스트</span>` -u `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">사용자명</span>` -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">암호</span>

- 원격으로 명령 실행하고 결과를 파일로 출력:

`psexec \\`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">원격_호스트</span>` cmd /c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">명령</span>` -an ^>`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로\대상\파일.txt</span>

- 사용자와 상호 작용하는 프로그램 실행:

`psexec \\`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">원격_호스트</span>` -d -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">프로그램명</span>

- 원격 호스트의 IP 구성 표시:

`psexec \\`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">원격_호스트</span>` ipconfig /all`
