---
layout: page
title: common/pdftotext (한국어)
description: "PDF 파일을 일반 텍스트 형식으로 변환."
content_hash: ac84d74fc3283035ab90638298d30fa229d10602
last_modified_at: 2024-10-29
related_topics:
  - title: Deutsch version
    url: /de/common/pdftotext.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/pdftotext.html
    icon: bi bi-globe
tldri18n_status: 2
---
# pdftotext

PDF 파일을 일반 텍스트 형식으로 변환.
더 많은 정보: <https://www.xpdfreader.com/pdftotext-man.html>.

- `filename.pdf`를 일반 텍스트로 변환하고 `stdout`에 출력:

`pdftotext `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">filename.pdf</span>` -`

- `filename.pdf`를 일반 텍스트로 변환하고 `filename.txt`로 저장:

`pdftotext `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">filename.pdf</span>

- `filename.pdf`를 일반 텍스트로 변환하고 레이아웃 유지:

`pdftotext -layout `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">filename.pdf</span>

- `input.pdf`를 일반 텍스트로 변환하고 `output.txt`로 저장:

`pdftotext `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">input.pdf</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">output.txt</span>

- `input.pdf`의 2, 3, 4 페이지를 일반 텍스트로 변환하고 `output.txt`로 저장:

`pdftotext -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">2</span>` -l `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">4</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">input.pdf</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">output.txt</span>
