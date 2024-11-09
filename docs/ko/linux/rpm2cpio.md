---
layout: page
title: linux/rpm2cpio (한국어)
description: "RPM 패키지를 `cpio` 아카이브로 변환."
content_hash: 2415998ca0bac15561cbe9a51cdc8a121ec49938
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/linux/rpm2cpio.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/rpm2cpio.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># rpm2cpio

RPM 패키지를 `cpio` 아카이브로 변환.
더 많은 정보: <http://ftp.rpm.org/max-rpm/s1-rpm-miscellania-rpm2cpio.html>.

- RPM 패키지를 `cpio` 아카이브로 변환하고 현재 디렉토리에 `파일.cpio`로 저장:

`rpm2cpio `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.rpm</span>
