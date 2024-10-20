---
layout: page
title: common/fdroidcl (한국어)
description: "ADB를 통해 연결된 장치의 F-Droid 앱을 관리."
content_hash: 5b00a4c0354e00a823d7870a8e11c3853eddc7a0
last_modified_at: 2024-10-20
related_topics:
  - title: Deutsch version
    url: /de/common/fdroidcl.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/fdroidcl.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/fdroidcl.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># fdroidcl

ADB를 통해 연결된 장치의 F-Droid 앱을 관리.
더 많은 정보: <https://github.com/mvdan/fdroidcl>.

- F-Droid 색인을 가져옴:

`fdroidcl update`

- 애플리케이션에 대한 정보 표시:

`fdroidcl show `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">앱_아이디</span>

- 애플리케이션의 APK 파일을 다운로드:

`fdroidcl download `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">앱_아이디</span>

- 색인에서 앱 검색:

`fdroidcl search `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">검색_패턴</span>

- 연결된 장치에 앱 설치:

`fdroidcl install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">앱_아이디</span>

- 저장소 추가:

`fdroidcl repo add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">저장소_이름</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">url</span>

- 저장소 제거, 활성화 또는 비활성화:

`fdroidcl repo `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">remove|enable|disable</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">저장소_이름</span>
