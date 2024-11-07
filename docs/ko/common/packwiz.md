---
layout: page
title: common/packwiz (한국어)
description: "Minecraft 모드팩을 생성, 편집 및 관리."
content_hash: 669ba60843c0f11437c78de479cb00363a276e70
last_modified_at: 2024-11-07
related_topics:
  - title: English version
    url: /en/common/packwiz.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/packwiz.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># packwiz

Minecraft 모드팩을 생성, 편집 및 관리.
더 많은 정보: <https://packwiz.infra.link/reference/commands/packwiz/>.

- 현재 디렉토리에서 대화식으로 새로운 모드팩 생성:

`packwiz init`

- Modrinth 또는 Curseforge에서 모드 추가:

`packwiz `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">modrinth|curseforge</span>` add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">url|slug|검색_용어</span>

- 모드팩의 모든 모드 나열:

`packwiz list`

- 파일을 수동으로 편집한 후 `index.toml` 업데이트:

`packwiz refresh`

- Modrinth (`.mrpack`) 또는 Curseforge (Zip) 파일로 내보내기:

`packwiz `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">modrinth|curseforge</span>` export`
