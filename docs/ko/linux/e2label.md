---
layout: page
title: linux/e2label (한국어)
description: "ext2/ext3/ext4 파일 시스템의 레이블을 변경합니다."
content_hash: 527a8b3a19aa9954570f78cec616863153c787e4
last_modified_at: 2024-11-08
related_topics:
  - title: English version
    url: /en/linux/e2label.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/e2label.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># e2label

ext2/ext3/ext4 파일 시스템의 레이블을 변경합니다.
더 많은 정보: <https://manned.org/e2label>.

- 특정 ext 파티션의 볼륨 레이블 변경:

`e2label `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sda1</span>` "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">레이블_이름</span>`"`
