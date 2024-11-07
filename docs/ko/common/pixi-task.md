---
layout: page
title: common/pixi-task (한국어)
description: "프로젝트 환경에서 작업을 관리."
content_hash: a4c0724af297bc6b69c0a05724884b60240a9350
last_modified_at: 2024-11-07
related_topics:
  - title: English version
    url: /en/common/pixi-task.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/pixi-task.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># pixi task

프로젝트 환경에서 작업을 관리.
더 많은 정보: <https://pixi.sh/latest/reference/cli/#task>.

- 새 작업 생성:

`pixi task add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">작업_이름</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">작업_명령</span>

- 프로젝트의 모든 작업 나열:

`pixi task list`

- 작업 제거:

`pixi task remove `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">작업_이름</span>

- 작업에 대한 별칭 생성:

`pixi task alias `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">별칭_이름</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">작업1 작업2 ...</span>
