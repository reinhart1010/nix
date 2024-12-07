---
layout: page
title: common/tesseract (한국어)
description: "OCR (Optical Character Recognition) 엔진."
content_hash: f612683e8ef0471fbd4cfb635f9ed3bab748b0d7
last_modified_at: 2024-12-07
related_topics:
  - title: English version
    url: /en/common/tesseract.html
    icon: bi bi-globe
tldri18n_status: 2
---
# tesseract

OCR (Optical Character Recognition) 엔진.
더 많은 정보: <https://github.com/tesseract-ocr/tesseract>.

- 이미지에서 텍스트를 인식하여 `output.txt`에 저장 (`.txt` 확장자는 자동으로 추가됨):

`tesseract `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">이미지.png</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">출력</span>

- ISO 639-2 코드로 사용자 정의 언어 지정 (기본값은 영어, 예: deu = Deutsch = 독일어):

`tesseract -l deu `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">이미지.png</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">출력</span>

- 사용 가능한 언어의 ISO 639-2 코드 나열:

`tesseract --list-langs`

- 사용자 정의 페이지 세분화 모드 지정 (기본값은 3):

`tesseract --psm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">0에서_10</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">이미지.png</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">출력</span>

- 페이지 세분화 모드 및 설명 나열:

`tesseract --help-psm`
