---
layout: page
title: linux/sinfo (한국어)
description: "Slurm 노드 및 파티션 정보를 표시합니다."
content_hash: 759cb4ccc70e3dd4bc57ad50bc1cba5663258644
last_modified_at: 2024-11-11
related_topics:
  - title: English version
    url: /en/linux/sinfo.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/sinfo.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># sinfo

Slurm 노드 및 파티션 정보를 표시합니다.
같이 보기: `squeue` 및 `sbatch`, 이는 Slurm 작업 관리자에 포함됩니다.
더 많은 정보: <https://slurm.schedmd.com/sinfo.html>.

- 클러스터의 빠른 요약 개요 표시:

`sinfo --summarize`

- 클러스터 전체의 모든 파티션에 대한 자세한 상태 보기:

`sinfo`

- 특정 파티션에 대한 자세한 상태 보기:

`sinfo --partition `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">파티션_이름</span>

- 유휴 노드 정보 보기:

`sinfo --states `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">idle</span>

- 죽은 노드 요약:

`sinfo --dead`

- 죽은 노드와 그 이유 나열:

`sinfo --list-reasons`
