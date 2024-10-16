---
layout: page
title: common/dumpcap (한국어)
description: "네트워크 트래픽 덤프 도구."
content_hash: d1973c0be3e3b247bd98fec4f9bd9d9c59bdd4ab
last_modified_at: 2024-10-16
related_topics:
  - title: English version
    url: /en/common/dumpcap.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/dumpcap.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># dumpcap

네트워크 트래픽 덤프 도구.
더 많은 정보: <https://www.wireshark.org/docs/man-pages/dumpcap.html>.

- 사용 가능한 인터페이스 표시:

`dumpcap --list-interfaces`

- 특정 인터페이스에서 패킷을 캡처:

`dumpcap --interface `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1</span>

- 특정 위치로 패킷을 캡처:

`dumpcap --interface `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1</span>` -w `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력_파일.pcapng</span>

- 특정 크기의 특정 최대 파일 제한을 사용해 링 버퍼에 쓰기:

`dumpcap --interface `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1</span>` -w `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력_파일.pcapng</span>` --ring-buffer filesize:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">500000</span>` --ring-buffer files:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">10</span>
