---
layout: page
title: linux/vgchange (한국어)
description: "논리 볼륨 관리자(LVM) 볼륨 그룹의 속성을 변경합니다."
content_hash: 2693bc6d4818f244c48a3acd1e63b46437871b02
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/linux/vgchange.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/vgchange.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># vgchange

논리 볼륨 관리자(LVM) 볼륨 그룹의 속성을 변경합니다.
같이 보기: `lvm`.
더 많은 정보: <https://manned.org/vgchange>.

- 모든 볼륨 그룹의 논리 볼륨 활성화 상태 변경:

`sudo vgchange --activate `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">y|n</span>

- 지정된 볼륨 그룹의 논리 볼륨 활성화 상태 변경 (`vgscan`으로 확인 가능):

`sudo vgchange --activate `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">y|n</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">볼륨_그룹</span>
