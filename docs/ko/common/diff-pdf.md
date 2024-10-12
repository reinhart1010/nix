---
layout: page
title: common/diff-pdf (한국어)
description: "2개의 PDF를 비교."
content_hash: 609a7ea327e4031c5688859cafaf2c055be5a76d
last_modified_at: 2024-10-12
related_topics:
  - title: English version
    url: /en/common/diff-pdf.html
    icon: bi bi-globe
tldri18n_status: 2
---
# diff-pdf

2개의 PDF를 비교.
더 많은 정보: <https://github.com/vslavik/diff-pdf>.

- 반환 코드를 사용하여, 변경 사항을 나타내는 PDF를 비교 (`0` = 차이 없음, `1` = PDF가 다름):

`diff-pdf `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/a.pdf</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/b.pdf</span>

- PDF를 비교하여, 시각적으로 강조된 차이점이 있는 PDF를 출력:

`diff-pdf --output-diff=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/diff.pdf</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/a.pdf</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/b.pdf</span>

- PDF를 비교하고, 간단한 GUI에서 차이점을 확인:

`diff-pdf --view `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/a.pdf</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/b.pdf</span>
