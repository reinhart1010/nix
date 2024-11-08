---
layout: page
title: common/mutool (한국어)
description: "PDF 파일에서 데이터를 변환, 정보 조회 및 추출."
content_hash: bedabef21851e5d18e4c281ca045850052c1845a
last_modified_at: 2024-11-08
related_topics:
  - title: English version
    url: /en/common/mutool.html
    icon: bi bi-globe
tldri18n_status: 2
---
# mutool

PDF 파일에서 데이터를 변환, 정보 조회 및 추출.
더 많은 정보: <https://mupdf.readthedocs.io/en/latest/mupdf-command-line.html>.

- 페이지 범위를 PNG로 변환 (참고: 출력 자리 표시자에서 `%nd`는 `%d` 또는 `%2d`와 같은 인쇄 수정자로 대체해야 함):

`mutool convert -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력%nd.png</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/입력.pdf</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1-10</span>

- PDF의 한 개 이상의 페이지를 `stdout`에 텍스트로 변환:

`mutool draw -F txt `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/입력.pdf</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">2,3,5,...</span>

- 여러 PDF 파일을 병합:

`mutool merge -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력.pdf</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/입력1.pdf 경로/대상/입력2.pdf ...</span>

- PDF에 포함된 모든 콘텐츠에 대한 정보 조회:

`mutool info `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/입력.pdf</span>

- PDF에 포함된 모든 이미지, 글꼴 및 리소스를 현재 디렉터리에 추출:

`mutool extract `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/입력.pdf</span>

- PDF의 목차 (책갈피) 표시:

`mutool show `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/입력.pdf</span>` outline`
