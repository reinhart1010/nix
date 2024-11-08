---
layout: page
title: common/lzip (한국어)
description: "`gzip` 또는 `bzip2`와 유사한 사용자 인터페이스를 가진 무손실 데이터 압축기."
content_hash: b9b1e36800d20f52ad5fe1322c7b257d24658c7f
last_modified_at: 2024-11-08
related_topics:
  - title: English version
    url: /en/common/lzip.html
    icon: bi bi-globe
tldri18n_status: 2
---
# lzip

`gzip` 또는 `bzip2`와 유사한 사용자 인터페이스를 가진 무손실 데이터 압축기.
Lzip은 "Lempel-Ziv-Markovchain-Algorithm" (LZMA) 스트림 형식의 단순화된 형태를 사용하며 상호 운용성을 극대화하고 안전성을 최적화하기 위해 3단계 무결성 검사를 제공합니다.
더 많은 정보: <https://www.nongnu.org/lzip>.

- 파일을 압축하여 원본 파일을 대체:

`lzip `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- 파일을 압축하면서 원본 파일 유지:

`lzip -k `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- 가장 높은 압축률로 파일 압축 (레벨=9):

`lzip -k `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>` --best`

- 가장 빠른 속도로 파일 압축 (레벨=0):

`lzip -k `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>` --fast`

- 압축 파일의 무결성 테스트:

`lzip --test `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/아카이브.lz</span>

- 파일을 압축 해제하여 원본 파일로 대체:

`lzip -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/아카이브.lz</span>

- 파일을 압축 해제하면서 압축본 유지:

`lzip -d -k `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/아카이브.lz</span>

- 아카이브 내 파일 목록 및 압축 통계 표시:

`lzip --list `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/아카이브.lz</span>
