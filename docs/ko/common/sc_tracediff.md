---
layout: page
title: common/sc_tracediff (한국어)
description: "경로가 변경된 traceroute 경로를 표시."
content_hash: fb02daaa6212a67d5e57ced5fcb4cb84cfdfe051
last_modified_at: 2024-11-09
related_topics:
  - title: Deutsch version
    url: /de/common/sc_tracediff.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/sc_tracediff.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/sc_tracediff.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># sc_tracediff

경로가 변경된 traceroute 경로를 표시.
더 많은 정보: <https://www.caida.org/catalog/software/scamper/>.

- 두 `warts` 파일에서 traceroute의 차이점 표시:

`sc_tracediff `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일1.warts</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일2.warts</span>

- 두 `warts` 파일에서 변경되지 않은 traceroute도 포함하여 차이점 표시:

`sc_tracediff -a `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일1.warts</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일2.warts</span>

- 두 `warts` 파일에서 traceroute의 차이점을 표시하고 가능하면 IP 주소 대신 DNS 이름을 표시:

`sc_tracediff -n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일1.warts</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일2.warts</span>
