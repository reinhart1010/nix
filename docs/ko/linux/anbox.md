---
layout: page
title: linux/anbox (한국어)
description: "모든 Linux 운영 체제에서 Android 애플리케이션 실행."
content_hash: c420ea1969a85a410892d9714f149c4e58de2b91
last_modified_at: 2024-11-08
related_topics:
  - title: Deutsch version
    url: /de/linux/anbox.html
    icon: bi bi-globe
  - title: English version
    url: /en/linux/anbox.html
    icon: bi bi-globe
  - title: norsk version
    url: /no/linux/anbox.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/linux/anbox.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/anbox.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/anbox.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># anbox

모든 Linux 운영 체제에서 Android 애플리케이션 실행.
더 많은 정보: <https://manned.org/anbox>.

- Anbox를 앱 관리자에서 실행:

`anbox launch --package=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">org.anbox.appmgr</span>` --component=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">org.anbox.appmgr.AppViewActivity</span>
