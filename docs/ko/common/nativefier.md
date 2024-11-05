---
layout: page
title: common/nativefier (한국어)
description: "최소한의 설정으로 모든 웹사이트를 위한 데스크탑 앱 생성."
content_hash: c19fbde482592ba422ce4fc2ae904a92a4e2096a
last_modified_at: 2024-11-05
related_topics:
  - title: Deutsch version
    url: /de/common/nativefier.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/nativefier.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/nativefier.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/nativefier.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># nativefier

최소한의 설정으로 모든 웹사이트를 위한 데스크탑 앱 생성.
더 많은 정보: <https://github.com/jiahaog/nativefier>.

- 웹사이트를 위한 데스크탑 앱 만들기:

`nativefier `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">url</span>

- 사용자 지정 이름으로 데스크탑 앱 생성:

`nativefier --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">이름</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">url</span>

- 사용자 지정 아이콘 사용 (PNG 형식이어야 함):

`nativefier --icon `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/아이콘.png</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">url</span>
