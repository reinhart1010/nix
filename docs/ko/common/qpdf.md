---
layout: page
title: common/qpdf (한국어)
description: "다재다능한 PDF 변환 소프트웨어."
content_hash: e748cb3941d5904160de347882f985a14982f0af
last_modified_at: 2024-10-29
related_topics:
  - title: English version
    url: /en/common/qpdf.html
    icon: bi bi-globe
tldri18n_status: 2
---
# qpdf

다재다능한 PDF 변환 소프트웨어.
더 많은 정보: <https://github.com/qpdf/qpdf>.

- PDF 파일에서 페이지 1-3, 5 및 6-10을 추출하여 다른 파일로 저장:

`qpdf --empty --pages `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/입력.pdf</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1-3,5,6-10</span>` -- `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력.pdf</span>

- 여러 PDF 파일의 모든 페이지를 병합하여 새 PDF 파일로 저장:

`qpdf --empty --pages `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일1.pdf 파일2.pdf ...</span>` -- `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력.pdf</span>

- 주어진 페이지를 여러 PDF 파일에서 병합하여 새 PDF 파일로 저장:

`qpdf --empty --pages `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일1.pdf</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1,6-8</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일2.pdf</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">3,4,5</span>` -- `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력.pdf</span>

- 각 `n` 페이지 그룹을 주어진 파일명 패턴으로 별도의 출력 파일로 작성:

`qpdf --split-pages=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">n</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/입력.pdf</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력_%d.pdf</span>

- 특정 PDF 페이지를 주어진 각도로 회전:

`qpdf --rotate=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">90:2,4,6</span>` --rotate=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">180:7-8</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/입력.pdf</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력.pdf</span>

- 암호로 보호된 파일의 암호 제거:

`qpdf --password=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">암호</span>` --decrypt `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/입력.pdf</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력.pdf</span>
