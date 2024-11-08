---
layout: page
title: linux/debsecan (한국어)
description: "Debian 보안 분석기, 특정 Debian 설치에서 취약점을 나열하는 도구."
content_hash: 66946478a4ab76b89b6879efb416ec9266447f57
last_modified_at: 2024-11-08
related_topics:
  - title: English version
    url: /en/linux/debsecan.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/debsecan.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># debsecan

Debian 보안 분석기, 특정 Debian 설치에서 취약점을 나열하는 도구.
더 많은 정보: <https://gitlab.com/fweimer/debsecan>.

- 현재 호스트에서 취약한 설치 패키지 나열:

`debsecan`

- 특정 스위트의 취약한 설치 패키지 나열:

`debsecan --suite `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">릴리스_코드_이름</span>

- 수정된 취약점만 나열:

`debsecan --suite `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">릴리스_코드_이름</span>` --only-fixed`

- 불안정("sid") 버전의 수정된 취약점만 나열하고 루트로 메일 발송:

`debsecan --suite `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">sid</span>` --only-fixed --format `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">report</span>` --mailto `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">root</span>` --update-history`

- 취약한 설치 패키지 업그레이드:

`sudo apt upgrade $(debsecan --only-fixed --format `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">packages</span>`)`
