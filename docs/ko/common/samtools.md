---
layout: page
title: common/samtools (한국어)
description: "고처리량 시퀀싱(유전체학) 데이터를 처리하기 위한 도구."
content_hash: 213acaea1f8b58ea689f7af93973c1b6732c11df
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/common/samtools.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/samtools.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># samtools

고처리량 시퀀싱(유전체학) 데이터를 처리하기 위한 도구.
SAM/BAM/CRAM 형식의 데이터를 읽기/쓰기/편집/색인/보기 위해 사용됩니다.
더 많은 정보: <https://www.htslib.org>.

- SAM 입력 파일을 BAM 스트림으로 변환하고 파일로 저장:

`samtools view -S -b `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">입력.sam</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">출력.bam</span>

- `stdin`(-)에서 입력을 받아 특정 영역과 겹치는 모든 읽기 및 SAM 헤더를 `stdout`에 출력:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">다른_명령어</span>` | samtools view -h - chromosome:start-end`

- 파일을 정렬하여 BAM으로 저장 (출력 형식은 출력 파일의 확장자로 자동 결정됨):

`samtools sort `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">입력</span>` -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">출력.bam</span>

- 정렬된 BAM 파일 색인 (`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">sorted_input.bam.bai</span>` 생성):

`samtools index `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">정렬된_입력.bam</span>

- 파일의 정렬 통계 출력:

`samtools flagstat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">정렬된_입력</span>

- 각 색인(염색체/컨티그)에 대한 정렬 수 계산:

`samtools idxstats `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">정렬된_색인_입력</span>

- 여러 파일 병합:

`samtools merge `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">출력</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">입력1 입력2 ...</span>

- 읽기 그룹에 따라 입력 파일 분할:

`samtools split `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">병합된_입력</span>
