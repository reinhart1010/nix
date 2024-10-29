---
layout: page
title: common/img2pdf (한국어)
description: "래스터 이미지를 무손실로 PDF 파일로 변환."
content_hash: 292e4919029130bddd525c2dfc0fcb4b84954724
last_modified_at: 2024-10-29
related_topics:
  - title: English version
    url: /en/common/img2pdf.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/img2pdf.html
    icon: bi bi-globe
tldri18n_status: 2
---
# img2pdf

래스터 이미지를 무손실로 PDF 파일로 변환.
지원되는 이미지 포맷으로는 GIF, JPEG, JPEG2000, PNG, GIF, TIFF 등이 있습니다.
더 많은 정보: <https://gitlab.mister-muffin.de/josch/img2pdf>.

- 하나 이상의 이미지를 각각의 페이지에 넣어 단일 PDF로 변환:

`img2pdf `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/이미지1.확장자 경로/대상/이미지2.확장자 ...</span>` --output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.pdf</span>

- 다중 프레임 이미지의 첫 프레임만 PDF로 변환:

`img2pdf `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.gif</span>` --first-frame-only --output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.pdf</span>

- 이미지를 자동으로 방향 설정하고, 가로 모드의 특정 페이지 크기를 사용하며, 가로 및 세로로 특정 크기의 테두리를 설정:

`img2pdf `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/이미지.확장자</span>` --auto-orient --pagesize `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">A4^T</span>` --border `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">2cm</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">5.1cm</span>` --output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.pdf</span>

- 페이지의 특정 크기 내에 지정된 치수로만 큰 이미지를 축소:

`img2pdf `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/이미지.확장자</span>` --pagesize `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">30cm</span>`x`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">20cm</span>` --imgsize `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">10cm</span>`x`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">15cm</span>` --fit `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">shrink</span>` --output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.pdf</span>

- 이미지를 PDF로 변환하고, 결과 파일에 메타데이터 지정:

`img2pdf `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/이미지.확장자</span>` --title `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">제목</span>` --author `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">저자</span>` --creationdate `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1970-01-31</span>` --keywords `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">키워드1 키워드2</span>` --subject `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">주제</span>` --output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.pdf</span>
