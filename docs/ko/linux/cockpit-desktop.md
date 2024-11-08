---
layout: page
title: linux/cockpit-desktop (한국어)
description: "실행 중인 세션에서 Cockpit 페이지에 안전하게 접근."
content_hash: d61f12e8c33a3c21d1f5f1acf275513e5cf7c205
last_modified_at: 2024-11-08
related_topics:
  - title: English version
    url: /en/linux/cockpit-desktop.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/cockpit-desktop.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># cockpit-desktop

실행 중인 세션에서 Cockpit 페이지에 안전하게 접근.
격리된 네트워크 공간에서 `cockpit-ws` 및 웹 브라우저를 실행하고, 실행 중인 사용자 세션에서 `cockpit-bridge`를 시작합니다.
더 많은 정보: <https://cockpit-project.org/guide/latest/cockpit-desktop.1.html>.

- 페이지 열기:

`cockpit-desktop `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">url</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">SSH_호스트</span>

- 저장소 페이지 열기:

`cockpit-desktop `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/cockpit/@localhost/storage/index.html</span>
