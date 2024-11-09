---
layout: page
title: common/stormlock (한국어)
description: "중앙 집중식 잠금 시스템."
content_hash: 5ce0cddd96fca8e31f4776dbc04939c251510cf4
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/common/stormlock.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/stormlock.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># Stormlock

중앙 집중식 잠금 시스템.
더 많은 정보: <https://github.com/tmccombs/stormlock>.

- 리소스에 대한 임대 획득:

`stormlock acquire `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">리소스</span>

- 주어진 리소스에 대한 주어진 임대 해제:

`stormlock release `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">리소스</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">임대_ID</span>

- 리소스에 대한 현재 임대 정보 표시 (있는 경우):

`stormlock current `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">리소스</span>

- 주어진 리소스에 대한 임대가 현재 활성 상태인지 테스트:

`stormlock is-held `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">리소스</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">임대_ID</span>
