---
layout: page
title: linux/pstoedit (한국어)
description: "PDF 파일을 다양한 이미지 형식으로 변환합니다."
content_hash: bd0856fa71ef31750df4548233758453b2a32d42
last_modified_at: 2024-11-10
related_topics:
  - title: English version
    url: /en/linux/pstoedit.html
    icon: bi bi-globe
tldri18n_status: 2
---
# pstoedit

PDF 파일을 다양한 이미지 형식으로 변환합니다.
더 많은 정보: <http://www.pstoedit.net>.

- PDF 페이지를 PNG 또는 JPEG 형식으로 변환:

`pstoedit -page `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">페이지_번호</span>` -f magick `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.pdf</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">페이지.png|페이지.jpg]</span>

- 여러 PDF 페이지를 번호가 매겨진 이미지로 변환:

`pstoedit -f magick `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">페이지%d.png|페이지%d.jpg</span>
