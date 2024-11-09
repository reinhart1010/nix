---
layout: page
title: linux/pvremove (한국어)
description: "물리적 볼륨에서 LVM 레이블 제거."
content_hash: d2367673e2636d15c5529524ce742fa12a41a603
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/linux/pvremove.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/pvremove.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># pvremove

물리적 볼륨에서 LVM 레이블 제거.
더 많은 정보: <https://manned.org/pvremove>.

- 물리적 볼륨에서 LVM 레이블 제거:

`sudo pvremove `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sdXY</span>

- 작업 중 자세한 출력 표시:

`sudo pvremove --verbose `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sdXY</span>

- 확인을 묻지 않고 LVM 레이블 제거:

`sudo pvremove --yes `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sdXY</span>

- 강제로 LVM 레이블 제거:

`sudo pvremove --force `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sdXY</span>

- 출력을 JSON 형식으로 표시:

`sudo pvremove --reportformat json `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sdXY</span>
