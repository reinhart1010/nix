---
layout: page
title: common/cpdf (한국어)
description: "PDF 파일 조작."
content_hash: 0318c354b0c51700e38ae565f81c46e960b0fd4f
last_modified_at: 2024-10-12
related_topics:
  - title: English version
    url: /en/common/cpdf.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/cpdf.html
    icon: bi bi-globe
tldri18n_status: 2
---
# cpdf

PDF 파일 조작.
더 많은 정보: <https://www.coherentpdf.com/cpdfmanual/cpdfmanual.html>.

- 소스 문서에서 1, 2, 3 및 6페이지를 선택하고 이를 대상 문서에 작성:

`cpdf `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/소스_문서.pdf</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1-3,6</span>` -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/대상_문서.pdf</span>

- 두 개의 문서를 새 문서로 병합:

`cpdf -merge `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/소스_문서_1.pdf</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/소스_문서_2.pdf</span>` -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/대상_문서.pdf</span>

- 문서의 북마크 표시:

`cpdf -list-bookmarks `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/문서.pdf</span>

- 문서를 10페이지 단위로 나누어 `chunk001.pdf`, `chunk002.pdf` 등에 작성:

`cpdf -split `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/문서.pdf</span>` -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/문서%%%.pdf</span>` -chunk `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">10</span>

- 128비트 암호화를 사용하여 문서를 암호화하고, `fred`를 소유자 비밀번호로, `joe`를 사용자 비밀번호로 제공:

`cpdf -encrypt `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">128bit</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">fred</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">joe</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/소스_문서.pdf</span>` -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/암호화된_문서.pdf</span>

- 소유자 비밀번호 `fred`를 사용하여 문서를 해독:

`cpdf -decrypt `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/암호화된_문서.pdf</span>` owner=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">fred</span>` -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/복호화된_문서.pdf</span>

- 문서의 주석 표시:

`cpdf -list-annotations `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/문서.pdf</span>

- 추가 메타데이터를 사용하여 기존 문서에서 새 문서를 생성:

`cpdf -set-metadata `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/메타데이터.xml</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/소스_문서.pdf</span>` -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/대상_문서.pdf</span>
