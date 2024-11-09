---
layout: page
title: common/snort (한국어)
description: "오픈 소스 네트워크 침입 탐지 시스템."
content_hash: ccec5085d252152c4cb5619d583a5998c1b7c658
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/common/snort.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/snort.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># snort

오픈 소스 네트워크 침입 탐지 시스템.
더 많은 정보: <https://www.snort.org/#documents>.

- 자세한 출력으로 패킷 캡처:

`sudo snort -v -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">인터페이스</span>

- 애플리케이션 계층 데이터를 덤프하여 자세한 출력으로 패킷 캡처:

`sudo snort -vd -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">인터페이스</span>

- 링크 계층 패킷 헤더를 표시하며 자세한 출력으로 패킷 캡처:

`sudo snort -ve -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">인터페이스</span>

- 지정한 디렉토리에 패킷 저장하며 캡처:

`sudo snort -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">인터페이스</span>` -l `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/폴더</span>

- 규칙에 따라 패킷 캡처하고 경고와 함께 문제 패킷 저장:

`sudo snort -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">인터페이스</span>` -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/규칙.conf</span>` -l `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/폴더</span>
