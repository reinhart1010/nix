---
layout: page
title: common/cs-fetch (한국어)
description: "Fetch는 종속성의 JAR를 가져옴."
content_hash: 019de7ef8974b32f26c792e2d69c6ce76984961e
last_modified_at: 2024-10-11
related_topics:
  - title: English version
    url: /en/common/cs-fetch.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/cs-fetch.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># cs fetch

Fetch는 종속성의 JAR를 가져옴.
더 많은 정보: <https://get-coursier.io/docs/cli-fetch>.

- jar의 특정 버전을 가져옴:

`cs fetch `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">그룹_아이디</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">아티팩트_아이디</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">아티팩트_버전</span>

- 패키지를 가져오고 env var에서 선택한 패키지에 해당하는 클래스 경로를 평가:

`CP="$(cs fetch --classpath org.scalameta::scalafmt-cli:latest.release)"`

- 특정 jar의 소스를 가져옴:

`cs fetch --sources `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">그룹_아이디</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">아티팩트_아이디</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">아티팩트_버전</span>

- javadoc jar를 가져옴:

`cs fetch --javadoc `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">그룹_아이디</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">아티팩트_아이디</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">아티팩트_버전</span>

- javadoc jar 및 소스 jar로 종속성을 가져옴:

`cs fetch --default=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">true</span>` --sources --javadoc `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">그룹_아이디</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">아티팩트_아이디</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">아티팩트_버전</span>

- 종속성 파일에서 오는 jar 가져오기:

`cs fetch `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">--dependency-file 경로/대상/파일1 --dependency-file 경로/대상/파일2 ...</span>
