---
layout: page
title: common/salt-run (한국어)
description: "minion에서 salt-runners를 실행하기 위한 프론트엔드."
content_hash: 3dc7758e59c292b5a8d286442a34a97d225f43a6
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/common/salt-run.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/salt-run.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># salt-run

minion에서 salt-runners를 실행하기 위한 프론트엔드.
더 많은 정보: <https://docs.saltproject.io/en/latest/ref/cli/salt-run.html>.

- 모든 minion의 상태 표시:

`salt-run manage.status`

- 연결이 끊긴 모든 minion 표시:

`salt-run manage.up`
