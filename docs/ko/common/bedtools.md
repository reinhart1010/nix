---
layout: page
title: common/bedtools (한국어)
description: "유전자 분석 작업을 위한 도구의 swiss-army knife. BAM, BED, GFF/GTF, VCF 형식으로 데이터를 교차, 그룹화, 변환 및 카운트하는 데 사용."
content_hash: df62413e9e747328fc5db858c7532f8f4bfd98ee
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/bedtools.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/bedtools.html
    icon: bi bi-globe
tldri18n_status: 2
---
# bedtools

유전자 분석 작업을 위한 도구의 swiss-army knife. BAM, BED, GFF/GTF, VCF 형식으로 데이터를 교차, 그룹화, 변환 및 카운트하는 데 사용.
더 많은 정보: <https://bedtools.readthedocs.io>.

- sequence의 strand를 기준으로 두개의 파일을 교차하고 결과를 `path/to/output_file`의 경로에 저장:

`bedtools intersect -a `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file1</span>` -b `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file2</span>` -s > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output_file</span>

- 외부 조인이 왼쪽인 두개의 파일을 교차, 예시. `file1`에서 각 기능을 보고하고 `file2`와 겹치지 않으면 NULL:

`bedtools intersect -a `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file1</span>` -b `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file2</span>` -lof > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output_file</span>

- 더 효율적인 알고리즘을 사용하여 두개의 사전 정렬된 파일을 교차:

`bedtools intersect -a `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file1</span>` -b `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file2</span>` -sorted > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output_file</span>

- 첫 3열과 5열을 기준으로 `path/to/file`을 그룹화하여 6열을 요약:

`bedtools groupby -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>` -c 1-3,5 -g 6 -o sum`

- bam-formated 파일을 bed-formated 파일로 변환:

`bedtools bamtobed -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.bam</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.bed</span>

- `file_2.bed`와 가장 가까운 `file1.bed`에서의 모든 기능을 찾고,그들의 거리와 추가 열을 기록 (입력 파일 정렬 필요):

`bedtools closest -a `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file1.bed</span>` -b `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file2.bed</span>` -d`
