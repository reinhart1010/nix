---
layout: page
title: common/zip2john (한국어)
description: "Zip 아카이브에서 암호 해시를 추출하여 John the Ripper 암호 크래커에서 사용."
content_hash: fa8eddfd36fa84cf826941b67e503008de35f53c
last_modified_at: 2024-11-02
related_topics:
  - title: English version
    url: /en/common/zip2john.html
    icon: bi bi-globe
tldri18n_status: 2
---
# zip2john

Zip 아카이브에서 암호 해시를 추출하여 John the Ripper 암호 크래커에서 사용.
일반적으로 John the Ripper 설치의 일부로 설치되는 유틸리티 도구입니다.
더 많은 정보: <https://www.openwall.com/john/>.

- 아카이브의 모든 파일을 나열하여 암호 해시 추출:

`zip2john `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.zip</span>

- 특정 압축 파일만 사용하여 암호 해시 추출:

`zip2john -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/압축_파일</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.zip</span>

- 특정 파일로 압축 파일에서 암호 해시 추출 (John the Ripper에서 사용하기 위해):

`zip2john -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/압축_파일</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.zip</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">파일.hash</span>
