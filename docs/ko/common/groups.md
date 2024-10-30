---
layout: page
title: common/groups (한국어)
description: "사용자의 그룹 멤버십을 출력."
content_hash: 927d8978b332adc2fb410a5f6f492cc2cda184a6
last_modified_at: 2024-10-30
related_topics:
  - title: English version
    url: /en/common/groups.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/groups.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/groups.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># groups

사용자의 그룹 멤버십을 출력.
참고: `groupadd`, `groupdel`, `groupmod`.
더 많은 정보: <https://www.gnu.org/software/coreutils/groups>.

- 현재 사용자의 그룹 멤버십을 출력:

`groups`

- 사용자 목록의 그룹 구성원을 출력:

`groups `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">사용자명1 사용자명2 ...</span>
