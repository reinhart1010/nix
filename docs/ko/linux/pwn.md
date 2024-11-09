---
layout: page
title: linux/pwn (한국어)
description: "신속한 프로토타이핑을 위한 Exploit 개발 라이브러리."
content_hash: e9d3326df734fba6eea135e86f319c6944376427
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/linux/pwn.html
    icon: bi bi-globe
  - title: español version
    url: /es/linux/pwn.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/pwn.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># pwn

신속한 프로토타이핑을 위한 Exploit 개발 라이브러리.
더 많은 정보: <https://docs.pwntools.com/en/stable/commandline.html>.

- 주어진 어셈블리 코드를 `bytes`로 변환:

`pwn asm "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">xor edi, edi</span>`"`

- 특정 문자 수의 순환 패턴 생성:

`pwn cyclic `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">숫자</span>

- 주어진 데이터를 16진수로 인코딩:

`pwn hex `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">deafbeef</span>

- 주어진 데이터를 16진수에서 디코딩:

`pwn unhex `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">6c4f7645</span>

- 셸 실행을 위한 x64 Linux 쉘코드 출력:

`pwn shellcraft `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">amd64.linux.sh</span>

- 주어진 ELF 파일의 바이너리 보안 설정 확인:

`pwn checksec `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- Pwntools 업데이트 확인:

`pwn update`

- 버전 표시:

`pwn version`
