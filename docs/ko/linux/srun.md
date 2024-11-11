---
layout: page
title: linux/srun (한국어)
description: "대화형 슬럼 작업을 생성하거나 기존 작업에 연결합니다."
content_hash: a7d6745502dd3d02f1e0a386da6e73d756a7a703
last_modified_at: 2024-11-11
related_topics:
  - title: English version
    url: /en/linux/srun.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/srun.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># srun

대화형 슬럼 작업을 생성하거나 기존 작업에 연결합니다.
더 많은 정보: <https://slurm.schedmd.com/srun.html>.

- 기본 대화형 작업 제출:

`srun --pty /bin/bash`

- 다양한 속성으로 대화형 작업 제출:

`srun --ntasks-per-node=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">코어_수</span>` --mem-per-cpu=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">메모리_MB</span>` --pty /bin/bash`

- 작업이 실행 중인 워커 노드에 연결:

`srun --jobid=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">작업_ID</span>` --pty /bin/bash`
