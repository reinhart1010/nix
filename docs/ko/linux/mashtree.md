---
layout: page
title: linux/mashtree (한국어)
description: "유전체로부터 빠르게 트리를 생성합니다."
content_hash: cff1f715e333c8d7fe4a57a582a841b77b7e93e5
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/linux/mashtree.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/mashtree.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># mashtree

유전체로부터 빠르게 트리를 생성합니다.
계통수를 생성하지 않습니다.
더 많은 정보: <https://github.com/lskatz/mashtree>.

- fastq 및/또는 fasta 파일로부터 여러 스레드를 사용하여 가장 빠르게 트리를 생성하고, newick 파일로 출력:

`mashtree --numcpus `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">12</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">*.fastq.gz</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">*.fasta</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">mashtree.dnd</span>

- fastq 및/또는 fasta 파일로부터 여러 스레드를 사용하여 가장 정확하게 트리를 생성하고, newick 파일로 출력:

`mashtree --mindepth `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">0</span>` --numcpus `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">12</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">*.fastq.gz</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">*.fasta</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">mashtree.dnd</span>

- 신뢰값을 포함하여 트리를 가장 정확하게 생성 (참고: `mashtree` 자체의 옵션은 `--` 오른쪽에 위치해야 함):

`mashtree_bootstrap.pl --reps `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">100</span>` --numcpus `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">12</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">*.fastq.gz</span>` -- --min-depth `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">0</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">mashtree.bootstrap.dnd</span>
