---
layout: page
title: linux/bwa (한국어)
description: "Burrows-Wheeler 정렬 도구."
content_hash: 100f91eab205205f6f0c001df001e4c73c1eaea7
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/linux/bwa.html
    icon: bi bi-globe
  - title: español version
    url: /es/linux/bwa.html
    icon: bi bi-globe
tldri18n_status: 2
---
# bwa

Burrows-Wheeler 정렬 도구.
짧고 낮은 발산율의 DNA 서열을 인간 유전체와 같은 대형 참조 유전체에 매핑합니다.
더 많은 정보: <https://github.com/lh3/bwa>.

- 참조 유전체 색인 생성:

`bwa index `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/참조.fa</span>

- 단일 엔드 읽기(서열)를 색인된 유전체에 32 [t]스레드를 사용하여 매핑하고 결과를 압축하여 공간 절약:

`bwa mem -t 32 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/참조.fa</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/단일_엔드_읽기.fq.gz</span>` | gzip > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/정렬_단일_엔드.sam.gz</span>

- 쌍 엔드 읽기(서열)를 색인된 유전체에 32 [t]스레드를 사용하여 매핑하고 결과를 압축하여 공간 절약:

`bwa mem -t 32 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/참조.fa</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/쌍_엔드_읽기_1.fq.gz</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/쌍_엔드_읽기_2.fq.gz</span>` | gzip > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/정렬_쌍_엔드.sam.gz</span>

- Picard 소프트웨어의 출력 SAM 파일 호환성을 위해 짧은 분할 히트를 보조로 [M]표시하여 쌍 엔드 읽기(서열)를 색인된 유전체에 32 [t]스레드를 사용하여 매핑하고 결과를 압축:

`bwa mem -M -t 32 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/참조.fa</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/쌍_엔드_읽기_1.fq.gz</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/쌍_엔드_읽기_2.fq.gz</span>` | gzip > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/정렬_쌍_엔드.sam.gz</span>

- FASTA/Q [C]주석(예: BC:Z:CGTAC)을 압축된 결과에 추가하여 쌍 엔드 읽기(서열)를 색인된 유전체에 32 [t]스레드를 사용하여 매핑:

`bwa mem -C -t 32 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/참조.fa</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/쌍_엔드_읽기_1.fq.gz</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/쌍_엔드_읽기_2.fq.gz</span>` | gzip > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/정렬_쌍_엔드.sam.gz</span>
