---
layout: page
title: linux/tftp (한국어)
description: "Trivial File Transfer Protocol 클라이언트."
content_hash: a7ea92d3d1c8da0913cadcea49ef1437e1f96ed0
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/linux/tftp.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/linux/tftp.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/tftp.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># tftp

Trivial File Transfer Protocol 클라이언트.
더 많은 정보: <https://manned.org/tftp.1>.

- TFTP 서버의 IP 주소와 포트를 지정하여 연결:

`tftp `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">서버_IP</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">포트</span>

- TFTP 서버에 연결하고 TFTP [c]명령 실행:

`tftp `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">서버_IP</span>` -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">명령</span>

- IPv6를 사용하여 TFTP 서버에 연결하고 시작 포트를 [R]범위 내로 강제 설정:

`tftp `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">서버_IP</span>` -6 -R `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">포트</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">포트</span>

- tftp 클라이언트를 통해 전송 모드를 바이너리 또는 ASCII로 설정:

`mode `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">binary|ascii</span>

- tftp 클라이언트를 통해 서버로부터 파일 다운로드:

`get `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">파일</span>

- tftp 클라이언트를 통해 서버로 파일 업로드:

`put `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">파일</span>

- tftp 클라이언트 종료:

`quit`
