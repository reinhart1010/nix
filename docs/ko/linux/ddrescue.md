---
layout: page
title: linux/ddrescue (한국어)
description: "손상된 블록 장치에서 데이터를 읽는 데이터 복구 도구."
content_hash: 9c686fd78565e73e7ad81268cd2ebc1aa5f304d0
last_modified_at: 2024-11-08
related_topics:
  - title: English version
    url: /en/linux/ddrescue.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/ddrescue.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># ddrescue

손상된 블록 장치에서 데이터를 읽는 데이터 복구 도구.
더 많은 정보: <https://www.gnu.org/software/ddrescue/>.

- 장치의 이미지를 생성하고 로그 파일 생성:

`sudo ddrescue `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sdb</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/이미지.dd</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/로그.txt</span>

- 디스크 A를 디스크 B로 클론하고 로그 파일 생성:

`sudo ddrescue --force --no-scrape `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sdX</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sdY</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/로그.txt</span>
