---
layout: page
title: common/ocrmypdf (한국어)
description: "스캔한 PDF나 텍스트 이미지에서 검색 가능한 PDF 또는 PDF/A를 생성."
content_hash: 2df191c4c675d87e7dec5072ddff110da02e98ed
last_modified_at: 2024-10-29
related_topics:
  - title: English version
    url: /en/common/ocrmypdf.html
    icon: bi bi-globe
tldri18n_status: 2
---
# ocrmypdf

스캔한 PDF나 텍스트 이미지에서 검색 가능한 PDF 또는 PDF/A를 생성.
더 많은 정보: <https://ocrmypdf.readthedocs.io/en/latest/cookbook.html>.

- 스캔한 PDF 또는 이미지 파일에서 새로운 검색 가능한 PDF/A 파일 생성:

`ocrmypdf `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/입력_파일</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력.pdf</span>

- 스캔한 PDF 파일을 검색 가능한 PDF 파일로 교체:

`ocrmypdf `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.pdf</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.pdf</span>

- 텍스트가 이미 포함된 혼합 형식 입력 PDF 파일의 페이지 건너뛰기:

`ocrmypdf --skip-text `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/입력.pdf</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력.pdf</span>

- 불량 스캔의 페이지를 정리하고, 기울임 보정하고, 회전:

`ocrmypdf --clean --deskew --rotate-pages `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/입력_파일</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력.pdf</span>

- 검색 가능한 PDF 파일의 메타데이터 설정:

`ocrmypdf --title "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">제목</span>`" --author "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">저자</span>`" --subject "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">주제</span>`" --keywords "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">키워드; 키 구문; ...</span>`" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/입력_파일</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력.pdf</span>

- 도움말 표시:

`ocrmypdf --help`
