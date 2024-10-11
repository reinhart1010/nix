---
layout: page
title: common/disown (한국어)
description: "하위 프로세스가 연결된 쉘 외부에서 작동하도록 허용."
content_hash: f259097721bbd2c599b4cfb660a88d6802bbce3a
last_modified_at: 2024-10-11
related_topics:
  - title: English version
    url: /en/common/disown.html
    icon: bi bi-globe
  - title: हिन्दी version
    url: /hi/common/disown.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/disown.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># disown

하위 프로세스가 연결된 쉘 외부에서 작동하도록 허용.
`jobs` 명령도 참조.
더 많은 정보: <https://www.gnu.org/software/bash/manual/bash.html#index-disown>.

- 현재 작업을 해제:

`disown`

- 특정 작업을 해제:

`disown %`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">작업_번호</span>

- 모든 작업 해제:

`disown -a`

- 작업을 유지 (해제하지 않음), 쉘 종료 시 향후 SIGHUP이 수신되지 않도록 표시:

`disown -h %`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">작업_번호</span>
