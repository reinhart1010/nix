---
layout: page
title: windows/sfc (한국어)
description: "Windows 시스템 파일의 무결성을 검사합니다."
content_hash: a09afc6bbeb88572d79734a58dd1ab8abefbd4bd
last_modified_at: 2024-10-20
related_topics:
  - title: English version
    url: /en/windows/sfc.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/windows/sfc.html
    icon: bi bi-globe
tldri18n_status: 2
---
# sfc

Windows 시스템 파일의 무결성을 검사합니다.
더 많은 정보: <https://learn.microsoft.com/windows-server/administration/windows-commands/sfc>.

- 명령어 사용 정보 표시:

`sfc`

- 모든 시스템 파일을 검사하고 가능하면 문제 수정:

`sfc /scannow`

- 모든 시스템 파일을 검사하고 문제 수정 시도 없음:

`sfc /verifyonly`

- 특정 파일을 검사하고 가능하면 문제 수정:

`sfc /scanfile=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로\대상\파일</span>

- 특정 파일을 검사하고 문제 수정 시도 없음:

`sfc /verifyfile=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로\대상\파일</span>

- 오프라인 복구 시 부팅 디렉터리 지정:

`sfc /offbootdir=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로\대상\폴더</span>

- 오프라인 복구 시 Windows 디렉터리 지정:

`sfc /offwindir=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로\대상\폴더</span>
