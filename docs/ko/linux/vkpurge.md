---
layout: page
title: linux/vkpurge (한국어)
description: "`xbps`에 의해 남겨진 오래된 커널 버전을 나열하거나 제거합니다."
content_hash: be929c8f6db74ac3c1ec816a40a3f344f8e90cbd
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/linux/vkpurge.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/vkpurge.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># vkpurge

`xbps`에 의해 남겨진 오래된 커널 버전을 나열하거나 제거합니다.
`version` 인수는 셸 글롭을 지원합니다.
더 많은 정보: <https://man.voidlinux.org/vkpurge.8>.

- 제거 가능한 모든 커널 버전 나열 (또는 `version` 인수가 지정된 경우 해당 버전 나열):

`vkpurge list `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">버전</span>

- 사용되지 않는 모든 커널 제거:

`vkpurge rm all`

- `version`과 일치하는 커널 버전 제거:

`vkpurge rm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">버전</span>
