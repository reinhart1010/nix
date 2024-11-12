---
layout: page
title: linux/smbclient (한국어)
description: "서버의 SMB/CIFS 리소스에 접근하기 위한 FTP 유사 클라이언트."
content_hash: 73421a52042513ffaffbfd99b228c839d06ce32b
last_modified_at: 2024-11-12
related_topics:
  - title: English version
    url: /en/linux/smbclient.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/linux/smbclient.html
    icon: bi bi-globe
tldri18n_status: 2
---
# smbclient

서버의 SMB/CIFS 리소스에 접근하기 위한 FTP 유사 클라이언트.
더 많은 정보: <https://manned.org/smbclient>.

- 공유 서버에 연결(비밀번호 입력이 필요하며, `exit` 명령으로 세션 종료):

`smbclient `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">//서버/공유</span>

- 다른 사용자명으로 연결:

`smbclient `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">//서버/공유</span>` --user `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">사용자명</span>

- 다른 작업 그룹으로 연결:

`smbclient `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">//서버/공유</span>` --workgroup `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">도메인</span>` --user `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">사용자명</span>

- 사용자명과 비밀번호로 연결:

`smbclient `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">//서버/공유</span>` --user `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">사용자명%비밀번호</span>

- 서버에서 파일 다운로드:

`smbclient `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">//서버/공유</span>` --directory `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/폴더</span>` --command "get `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">파일.txt</span>`"`

- 서버에 파일 업로드:

`smbclient `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">//서버/공유</span>` --directory `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/폴더</span>` --command "put `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">파일.txt</span>`"`

- 서버의 공유 목록을 익명으로 나열:

`smbclient --list=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">서버</span>` --no-pass`
