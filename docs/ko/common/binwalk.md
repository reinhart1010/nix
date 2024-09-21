---
layout: page
title: common/binwalk (한국어)
description: "펌웨어 분석 도구."
content_hash: 172122f16f5a45f06b00e0d618b056c5d35f1a24
last_modified_at: 2024-09-21
related_topics:
  - title: English version
    url: /en/common/binwalk.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/binwalk.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/binwalk.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/binwalk.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/binwalk.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># binwalk

펌웨어 분석 도구.
더 많은 정보: <https://github.com/ReFirmLabs/binwalk>.

- 바이너리 파일 스캔:

`binwalk `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/바이너리</span>

- 출력 디렉터리를 지정하여 바이너리에서 파일을 추출:

`binwalk --extract --directory `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">출력_디렉토리</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/바이너리</span>

- 재귀 깊이를 2로 제한하는 바이너리에서 파일을 재귀적으로 추출:

`binwalk --extract --matryoshka --depth `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">2</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/바이너리</span>

- 지정된 파일 서명을 사용하여 바이너리에서 파일을 추출:

`binwalk --dd '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">png image:png</span>`' `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/바이너리</span>

- 바이너리의 엔트로피를 분석하여, 바이너리와 동일한 이름과 `.png` 확장자를 추가하여 플롯을 저장:

`binwalk --entropy --save `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/바이너리</span>

- 엔트로피, 서명 및 opcode 분석을 단일 명령으로 결합:

`binwalk --entropy --signature --opcodes `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/바이너리</span>
