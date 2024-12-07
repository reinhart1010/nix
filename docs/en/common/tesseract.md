---
layout: page
title: common/tesseract (English)
description: "OCR (Optical Character Recognition) engine."
content_hash: e94b360e75e2a6ac51f42f5ba66793f65b6bdf50
last_modified_at: 2024-12-07
related_topics:
  - title: 한국어 version
    url: /ko/common/tesseract.html
    icon: bi bi-globe
tldri18n_status: 2
---
# tesseract

OCR (Optical Character Recognition) engine.
More information: <https://github.com/tesseract-ocr/tesseract>.

- Recognize text in an image and save it to `output.txt` (the `.txt` extension is added automatically):

`tesseract `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">image.png</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">output</span>

- Specify a custom language (default is English) with an ISO 639-2 code (e.g. deu = Deutsch = German):

`tesseract -l deu `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">image.png</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">output</span>

- List the ISO 639-2 codes of available languages:

`tesseract --list-langs`

- Specify a custom page segmentation mode (default is 3):

`tesseract --psm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">0_to_10</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">image.png</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">output</span>

- List page segmentation modes and their descriptions:

`tesseract --help-psm`
