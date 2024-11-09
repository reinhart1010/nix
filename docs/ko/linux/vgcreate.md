---
layout: page
title: linux/vgcreate (한국어)
description: "여러 대용량 저장 장치를 결합하여 볼륨 그룹 생성."
content_hash: 676b6217a1726d6768f6e35bbf466d56f2eb82a9
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/linux/vgcreate.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/vgcreate.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># vgcreate

여러 대용량 저장 장치를 결합하여 볼륨 그룹 생성.
같이 보기: `lvm`.
더 많은 정보: <https://manned.org/vgcreate>.

- `/dev/sda1` 장치를 사용하여 vg1이라는 새 볼륨 그룹 생성:

`vgcreate `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">vg1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sda1</span>

- 여러 장치를 사용하여 vg1이라는 새 볼륨 그룹 생성:

`vgcreate `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">vg1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sda1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sdb1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sdc1</span>
