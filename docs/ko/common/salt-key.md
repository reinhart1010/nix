---
layout: page
title: common/salt-key (한국어)
description: "Salt 마스터에서 Salt 미니언 키를 관리."
content_hash: c122264627599ec179b528ac1679b6fc81677d17
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/common/salt-key.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/salt-key.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># salt-key

Salt 마스터에서 Salt 미니언 키를 관리.
루트 사용자로 또는 sudo와 함께 Salt 마스터에서 실행해야 함.
더 많은 정보: <https://docs.saltproject.io/en/latest/ref/cli/salt-key.html>.

- 수락된, 수락되지 않은 및 거부된 모든 미니언 키 나열:

`salt-key -L`

- 이름으로 미니언 키 수락:

`salt-key -a `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">미니언_ID</span>

- 이름으로 미니언 키 거부:

`salt-key -r `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">미니언_ID</span>

- 모든 공개 키의 지문 출력:

`salt-key -F`
