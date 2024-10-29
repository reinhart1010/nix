---
layout: page
title: common/pdfjoin (한국어)
description: "pdfjam을 기반으로 한 PDF 병합 도구."
content_hash: adb24a7588567c8c86e98857f17ee0d11d01bcb2
last_modified_at: 2024-10-29
related_topics:
  - title: English version
    url: /en/common/pdfjoin.html
    icon: bi bi-globe
tldri18n_status: 2
---
# pdfjoin

pdfjam을 기반으로 한 PDF 병합 도구.
더 많은 정보: <https://github.com/rrthomas/pdfjam-extras>.

- 두 개의 PDF를 기본 접미사 "joined"로 하나로 병합:

`pdfjoin `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일1.pdf</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일2.pdf</span>

- 각 파일의 첫 번째 페이지를 함께 병합:

`pdfjoin `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일1.pdf 경로/대상/파일2.pdf ...</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1</span>` --outfile `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">출력_파일</span>

- 페이지 3에서 5까지와 페이지 1을 순서대로 새로운 PDF로 저장하고 사용자 정의 접미사를 추가:

`pdfjoin `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.pdf</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">3-5,1</span>` --suffix `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">재정렬했음</span>

- 두 PDF의 페이지 하위 범위를 병합:

`pdfjoin `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일1.pdf</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">2-</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">파일2</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">last-3</span>` --outfile `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">출력_파일</span>
