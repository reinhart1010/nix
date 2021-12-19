---
layout: page
title: common/tesseract (English)
description: "OCR (Optical Character Recognition) engine."
content_hash: 9552afac7fbfe5ae66d021b5e238f77e0b766ae4
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

`tesseract -psm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">0_to_10</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">image.png</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">output</span>

- List page segmentation modes and their descriptions:

`tesseract --help-psm`
