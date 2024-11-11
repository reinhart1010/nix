---
layout: page
title: linux/slapt-src (한국어)
description: "SlackBuilds의 빌드를 자동화하는 유틸리티."
content_hash: 19789744f7511c22fdef118139067f770e7de4b9
last_modified_at: 2024-11-11
related_topics:
  - title: English version
    url: /en/linux/slapt-src.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/slapt-src.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># slapt-src

SlackBuilds의 빌드를 자동화하는 유틸리티.
SlackBuild 소스는 slapt-srcrc 파일에 구성해야 합니다.
더 많은 정보: <https://github.com/jaos/slapt-src>.

- 사용 가능한 SlackBuilds 및 버전 목록 업데이트:

`slapt-src --update`

- 사용 가능한 모든 SlackBuilds 나열:

`slapt-src --list`

- 지정된 SlackBuild(들)을 가져와서 빌드하고 설치:

`slapt-src --install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">slackbuild_이름</span>

- 이름 또는 설명으로 SlackBuilds 찾기:

`slapt-src --search `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">검색_어구</span>

- SlackBuild에 대한 정보 표시:

`slapt-src --show `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">slackbuild_이름</span>
