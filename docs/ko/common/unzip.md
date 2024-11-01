---
layout: page
title: common/unzip (한국어)
description: "Zip 아카이브에서 파일/디렉토리를 추출."
content_hash: efe54fe3301091363b383ec67e951b6748ea4d0a
last_modified_at: 2024-11-01
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
  - title: українська version
    url: /uk/common/unzip.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/unzip.html
    icon: bi bi-globe
tldri18n_status: 2
---
# unzip

Zip 아카이브에서 파일/디렉토리를 추출.
같이 보기: `zip`.
더 많은 정보: <https://manned.org/unzip>.

- 특정 아카이브에서 모든 파일/디렉토리를 현재 디렉토리에 추출:

`unzip `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/아카이브1.zip 경로/대상/아카이브2.zip ...</span>

- 아카이브에서 파일/디렉토리를 특정 경로로 추출:

`unzip `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/아카이브1.zip 경로/대상/아카이브2.zip ...</span>` -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력</span>

- 아카이브에서 파일/디렉토리를 추출하고 추출된 파일 이름과 함께 `stdout`으로 출력:

`unzip -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/아카이브1.zip 경로/대상/아카이브2.zip ...</span>

- 비ASCII 문자(예: 중국어나 일본어 문자)를 포함한 파일 이름이 있는 Windows에서 생성된 아카이브를 추출:

`unzip -O `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">gbk</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/아카이브1.zip 경로/대상/아카이브2.zip ...</span>

- 특정 아카이브의 내용을 추출하지 않고 나열:

`unzip -l `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/아카이브.zip</span>

- 아카이브에서 특정 파일 추출:

`unzip -j `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/아카이브.zip</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/아카이브_내_파일1 경로/대상/아카이브_내_파일2 ...</span>
