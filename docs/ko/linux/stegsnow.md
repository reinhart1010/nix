---
layout: page
title: linux/stegsnow (한국어)
description: "탭과 공백으로 인코딩된 텍스트 파일에 메시지를 숨기고 추출하는 스테가노그래피 도구."
content_hash: 5ec31b000285d7c0a95dc7b7fada2870b66d0e4a
last_modified_at: 2024-11-11
related_topics:
  - title: English version
    url: /en/linux/stegsnow.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/stegsnow.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># stegsnow

탭과 공백으로 인코딩된 텍스트 파일에 메시지를 숨기고 추출하는 스테가노그래피 도구.
더 많은 정보: <https://darkside.com.au/snow/manual.html>.

- 파일에서 [m]메시지 추출:

`stegsnow `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.txt</span>

- 파일에서 [C]압축되고 [p]비밀번호로 보호된 [m]메시지 추출:

`stegsnow -C -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">비밀번호</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.txt</span>

- 파일의 줄 [l]길이가 72보다 작은 경우 대략적인 [S]저장 용량 확인:

`stegsnow -S -l 72 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.txt</span>

- 파일의 텍스트에 [m]메시지 숨기고 결과로 저장:

`stegsnow -m '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">메시지</span>`' `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.txt</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/결과.txt</span>

- 파일의 텍스트에 [C]압축된 메시지 [f]파일 내용을 숨기고 결과로 저장:

`stegsnow -C -f '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/메시지.txt</span>`' `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.txt</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/결과.txt</span>

- 파일의 텍스트에 [C]압축되고 [p]비밀번호로 보호된 [m]메시지 숨기고 결과로 저장:

`stegsnow -C -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">비밀번호</span>` -m '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">메시지</span>`' `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.txt</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/결과.txt</span>
