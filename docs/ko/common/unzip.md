---
layout: page
title: common/unzip (한국어)
description: "ZIP 아카이브에서 파일/폴더 추출."
content_hash: 3636c09f7cd74199be68cef4fa916523197b600d
last_modified_at: 2023-10-23
related_topics:
  - title: English version
    url: /en/common/unzip.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/unzip.html
    icon: bi bi-globe
  - title: русский version
    url: /ru/common/unzip.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># unzip

ZIP 아카이브에서 파일/폴더 추출.
같이 보기: `zip`.
더 많은 정보: <https://manned.org/unzip>.

- 특정 폴더의 모든 파일/폴더를 현재 폴더로 추출:

`unzip `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/아카이브1.zip 경로/대상/아카이브2.zip ...</span>

- 아카이브에서 특정 경로로 파일/폴더 추출:

`unzip `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/아카이브1.zip 경로/대상/아카이브2.zip ...</span>` -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력</span>

- 아카이브에서 `stdout`으로 파일/폴더 추출:

`unzip -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/아카이브1.zip 경로/대상/아카이브2.zip ...</span>

- 추출된 파일 이름과 함께 파일 내용을 `stdout`으로 추출:

`unzip -O `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">gbk</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/아카이브1.zip 경로/대상/아카이브2.zip ...</span>

- 특정 아카이브의 내용을 추출하지 않고 나열:

`unzip -l `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/아카이브.zip</span>

- 아카이브에서 특정 파일 추출:

`unzip -j `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/아카이브.zip</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/아카이브1_파일 경로/대상/아카이브2_파일 ...</span>
