---
layout: page
title: common/nextclade (한국어)
description: "바이러스 유전체 정렬, 계통 할당 및 품질 검사를 위한 생물정보학 도구."
content_hash: 7438c1edc8dcb160867dd75b79c816f40660822c
last_modified_at: 2024-11-05
related_topics:
  - title: English version
    url: /en/common/nextclade.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/nextclade.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># nextclade

바이러스 유전체 정렬, 계통 할당 및 품질 검사를 위한 생물정보학 도구.
더 많은 정보: <https://docs.nextstrain.org/projects/nextclade/en/stable/user/nextclade-cli/index.html>.

- 사용자 제공 [r]eference에 시퀀스를 정렬하고, 정렬 결과를 파일로 출력:

`nextclade run `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/시퀀스.fa</span>` -r `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/레퍼런스.fa</span>` -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/정렬결과.fa</span>

- 최신 [d]ataset을 자동으로 다운로드하여 [t]SV 보고서 생성:

`nextclade run `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/fasta</span>` -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">데이터셋_이름</span>` -t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/보고서.tsv</span>

- 사용 가능한 모든 데이터셋 나열:

`nextclade dataset list`

- 최신 SARS-CoV-2 데이터셋 다운로드:

`nextclade dataset get --name sars-cov-2 --output-dir `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/폴더</span>

- 다운로드한 [D]ataset을 사용하여 모든 [O]utputs 생성:

`nextclade run -D `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/데이터셋_폴더</span>` -O `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력_폴더</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/시퀀스.fasta</span>

- 여러 파일에서 실행:

`nextclade run -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">데이터셋_이름</span>` -t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력_tsv</span>` -- `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/입력_fasta_1 경로/대상/입력_fasta_2 ...</span>

- 시퀀스가 정렬되지 않을 경우 역상보 시도:

`nextclade run --retry-reverse-complement -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">데이터셋_이름</span>` -t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력_tsv</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/입력_fasta</span>
