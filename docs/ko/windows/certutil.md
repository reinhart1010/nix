---
layout: page
title: windows/certutil (한국어)
description: "인증서 정보를 관리하고 구성하는 도구."
content_hash: 2b73f0f2eac55b2470797f9f51cdc208df942cdf
last_modified_at: 2024-11-06
related_topics:
  - title: English version
    url: /en/windows/certutil.html
    icon: bi bi-globe
  - title: हिन्दी version
    url: /hi/windows/certutil.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/windows/certutil.html
    icon: bi bi-globe
tldri18n_status: 2
---
# certutil

인증서 정보를 관리하고 구성하는 도구.
더 많은 정보: <https://learn.microsoft.com/windows-server/administration/windows-commands/certutil>.

- 구성 정보 또는 파일 덤프:

`certutil `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">파일_이름</span>

- 파일을 16진수로 인코딩:

`certutil -encodehex `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로\대상\입력_파일</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로\대상\출력_파일</span>

- 파일을 Base64로 인코딩:

`certutil -encode `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로\대상\입력_파일</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로\대상\출력_파일</span>

- Base64로 인코딩된 파일을 디코딩:

`certutil -decode `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로\대상\입력_파일</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로\대상\출력_파일</span>

- 파일에 대한 암호화 해시 생성 및 표시:

`certutil -hashfile `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로\대상\입력_파일</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">md2|md4|md5|sha1|sha256|sha384|sha512</span>
