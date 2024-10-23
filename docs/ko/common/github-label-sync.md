---
layout: page
title: common/github-label-sync (한국어)
description: "GitHub 라벨 동기화."
content_hash: e6aeb414206c093c474484c26b4b7f3d3a5a49f7
last_modified_at: 2024-10-23
related_topics:
  - title: English version
    url: /en/common/github-label-sync.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/github-label-sync.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/github-label-sync.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># github-label-sync

GitHub 라벨 동기화.
더 많은 정보: <https://github.com/Financial-Times/github-label-sync>.

- 로컬 `labels.json` 파일을 사용하여 라벨을 동기화:

`github-label-sync --access-token `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">토큰</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">레포지토리_이름</span>

- 특정 라벨 JSON 파일을 사용하여 라벨을 동기화:

`github-label-sync --access-token `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">토큰</span>` --labels `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">url|경로/대상/json_파일</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">레포지토리_이름</span>

- 실제로 라벨을 동기화하는 대신 테스트 실행을 수행:

`github-label-sync --access-token `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">토큰</span>` --dry-run `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">레포지토리_이름</span>

- `labels.json`에 없는 라벨을 유지:

`github-label-sync --access-token `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">토큰</span>` --allow-added-labels `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">레포지토리_이름</span>

- `GITHUB_ACCESS_TOKEN` 환경 변수를 사용하여 동기화:

`github-label-sync `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">레포지토리_이름</span>
