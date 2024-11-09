---
layout: page
title: common/sysbench (한국어)
description: "시스템의 CPU, IO 및 메모리를 벤치마킹."
content_hash: 7d5bb24d48c251709aed50695e1dd285caebdd71
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/common/sysbench.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/sysbench.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># sysbench

시스템의 CPU, IO 및 메모리를 벤치마킹.
더 많은 정보: <https://github.com/akopytov/sysbench/>.

- 1개의 스레드로 10초 동안 CPU 벤치마크 실행:

`sysbench cpu run`

- 여러 스레드로 지정된 시간 동안 CPU 벤치마크 실행:

`sysbench --threads=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">스레드_수</span>` --time=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">초</span>

- 1개의 스레드로 10초 동안 메모리 벤치마크 실행:

`sysbench memory run`

- 파일 시스템 수준의 읽기 벤치마크 준비:

`sysbench fileio prepare`

- 파일 시스템 수준의 벤치마크 실행:

`sysbench --file-test-mode=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">rndrd|rndrw|rndwr|seqrd|seqrewr|seqwr</span>` fileio run`
