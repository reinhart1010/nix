---
layout: page
title: linux/tlp (한국어)
description: "Linux용 고급 전원 관리 도구."
content_hash: 2394293905cba56732f37b669971226528d712bb
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/linux/tlp.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/tlp.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># tlp

Linux용 고급 전원 관리 도구.
같이 보기: `tlp-stat`.
더 많은 정보: <https://linrunner.de/tlp/>.

- 설정 적용 (현재 전원 공급원에 따라):

`sudo tlp start`

- 배터리 설정 적용 (현재 전원 공급원을 무시하고):

`sudo tlp bat`

- AC 설정 적용 (현재 전원 공급원을 무시하고):

`sudo tlp ac`
