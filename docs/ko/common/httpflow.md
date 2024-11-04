---
layout: page
title: common/httpflow (한국어)
description: "HTTP 스트림을 캡처하고 덤프하는 커멘드라인 유틸리티."
content_hash: a5f3ec540b5ab9298162087d324acee5feeca9f8
last_modified_at: 2024-11-04
related_topics:
  - title: English version
    url: /en/common/httpflow.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/httpflow.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># httpflow

HTTP 스트림을 캡처하고 덤프하는 커멘드라인 유틸리티.
더 많은 정보: <https://github.com/six-ddc/httpflow>.

- 모든 인터페이스에서 트래픽 캡처:

`httpflow -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">any</span>

- bpf-스타일 캡처를 사용하여 결과를 필터링:

`httpflow `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">host httpbin.org 또는 host baidu.com</span>

- 정규식을 사용하여 URL별로 요청을 필터링:

`httpflow -u '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">정규_표현식</span>`'`

- PCAP 형식 바이너리 파일에서 패킷을 읽음:

`httpflow -r `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">out.cap</span>

- 출력을 디렉터리에 씀:

`httpflow -w `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/디렉터리</span>
