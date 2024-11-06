---
layout: page
title: windows/ftp (한국어)
description: "로컬 및 원격 FTP 서버 간에 파일을 상호작용하며 전송."
content_hash: 174763e0d159dca0c73d28b710024ec76aeb2dfa
last_modified_at: 2024-11-06
related_topics:
  - title: Deutsch version
    url: /de/windows/ftp.html
    icon: bi bi-globe
  - title: English version
    url: /en/windows/ftp.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/windows/ftp.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/windows/ftp.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/windows/ftp.html
    icon: bi bi-globe
tldri18n_status: 2
---
# ftp

로컬 및 원격 FTP 서버 간에 파일을 상호작용하며 전송.
더 많은 정보: <https://learn.microsoft.com/windows-server/administration/windows-commands/ftp>.

- 원격 FTP 서버에 상호작용하며 연결:

`ftp `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">호스트</span>

- 익명 사용자로 로그인:

`ftp -A `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">호스트</span>

- 초기 연결 시 자동 로그인 비활성화:

`ftp -n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">호스트</span>

- FTP 명령 목록이 포함된 파일 실행:

`ftp -s:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로\대상\파일</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">호스트</span>

- 여러 파일 다운로드(글롭 표현식):

`mget `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">*.png</span>

- 여러 파일 업로드(글롭 표현식):

`mput `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">*.zip</span>

- 원격 서버에서 여러 파일 삭제:

`mdelete `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">*.txt</span>

- 도움말 표시:

`ftp --help`
