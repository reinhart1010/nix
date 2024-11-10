---
layout: page
title: common/snakefmt (한국어)
description: "Snakemake 파일을 포맷합니다."
content_hash: 330da83df6d552dfa56ce7eeebb7fca8ecd54847
last_modified_at: 2024-11-10
related_topics:
  - title: English version
    url: /en/common/snakefmt.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/snakefmt.html
    icon: bi bi-globe
tldri18n_status: 2
---
# snakefmt

Snakemake 파일을 포맷합니다.
더 많은 정보: <https://github.com/snakemake/snakefmt>.

- 특정 Snakefile 포맷:

`snakefmt `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/snakefile</span>

- 특정 디렉토리 내 모든 Snakefile을 재귀적으로 포맷:

`snakefmt `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/폴더</span>

- 특정 구성 파일을 사용하여 파일 포맷:

`snakefmt --config `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/구성.toml</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/snakefile</span>

- 특정 최대 줄 길이를 사용하여 파일 포맷:

`snakefmt --line-length `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">100</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/snakefile</span>

- 변경 사항을 수행하지 않고 표시만 하기 (드라이런):

`snakefmt --diff `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/snakefile</span>
