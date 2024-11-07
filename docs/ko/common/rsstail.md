---
layout: page
title: common/rsstail (한국어)
description: "RSS 피드를 위한 `tail`."
content_hash: 0f0789ead0ec929fd5b8d6a281713492611703a1
last_modified_at: 2024-11-07
related_topics:
  - title: English version
    url: /en/common/rsstail.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/rsstail.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># rsstail

RSS 피드를 위한 `tail`.
더 많은 정보: <https://github.com/gvalkov/rsstail.py>.

- 주어진 URL의 피드를 표시하고 새 항목이 아래에 나타날 때까지 대기:

`rsstail -u `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">URL</span>

- 피드를 역순으로 표시 (최신 항목이 아래에 위치):

`rsstail -r -u `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">URL</span>

- 발행 날짜와 링크 포함:

`rsstail -pl -u `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">URL</span>

- 업데이트 간격 설정:

`rsstail -u `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">URL</span>` -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">초_간격</span>

- 피드를 표시하고 종료:

`rsstail -1 -u `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">URL</span>
