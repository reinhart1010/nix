---
layout: page
title: linux/rpmconf (한국어)
description: "패키지 업그레이드 후 남겨진 RPMNEW, RPMSAVE 및 RPMORIG 파일 처리."
content_hash: aaf02b957b32b2e09db3348a6c9e64c30a495a8f
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/linux/rpmconf.html
    icon: bi bi-globe
  - title: español version
    url: /es/linux/rpmconf.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/rpmconf.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># rpmconf

패키지 업그레이드 후 남겨진 RPMNEW, RPMSAVE 및 RPMORIG 파일 처리.
같이 보기: `rpm`.
더 많은 정보: <https://github.com/xsuchy/rpmconf>.

- 남겨진 파일을 나열하고 각 파일에 대해 수행할 작업을 인터랙티브하게 선택:

`sudo rpmconf --all`

- 고아가 된 RPMNEW 및 RPMSAVE 파일 삭제:

`sudo rpmconf --all --clean`
