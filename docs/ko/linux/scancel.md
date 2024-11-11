---
layout: page
title: linux/scancel (한국어)
description: "Slurm 작업을 취소합니다."
content_hash: 157caee7b97edf6f4bb815e0162fb3ca29133b83
last_modified_at: 2024-11-11
related_topics:
  - title: English version
    url: /en/linux/scancel.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/scancel.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># scancel

Slurm 작업을 취소합니다.
더 많은 정보: <https://slurm.schedmd.com/scancel.html>.

- 작업 ID를 사용하여 작업 취소:

`scancel `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">작업_ID</span>

- 사용자로부터 모든 작업 취소:

`scancel `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">사용자_이름</span>
