---
layout: page
title: common/jf (한국어)
description: "Artifactory, Xray, Distribution, Pipelines, Mission Control과 같은 JFrog 제품과 상호작용."
content_hash: 887f4ccf62e7149b57094c2e5ae47be6122fc6bf
last_modified_at: 2024-11-05
related_topics:
  - title: English version
    url: /en/common/jf.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/jf.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/jf.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># jf

Artifactory, Xray, Distribution, Pipelines, Mission Control과 같은 JFrog 제품과 상호작용.
더 많은 정보: <https://jfrog.com/help/r/jfrog-cli/usage>.

- 새 구성 추가:

`jf config add`

- 현재 구성 표시:

`jf config show`

- 지정된 저장소 및 디렉토리 내에서 아티팩트 검색:

`jf rt search --recursive `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">저장소_이름</span>`/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로</span>`/`
