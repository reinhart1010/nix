---
layout: page
title: linux/systemd-escape (한국어)
description: "systemd 유닛 이름에서 사용할 문자열을 이스케이프합니다."
content_hash: 157c746b64587e72058b2f4cec36993f5ef9ea3f
last_modified_at: 2024-10-07
related_topics:
  - title: English version
    url: /en/linux/systemd-escape.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/systemd-escape.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># systemd-escape

systemd 유닛 이름에서 사용할 문자열을 이스케이프합니다.
더 많은 정보: <https://www.freedesktop.org/software/systemd/man/systemd-escape.html>.

- 주어진 텍스트 이스케이프:

`systemd-escape `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">텍스트</span>

- 이스케이프 처리 역전:

`systemd-escape --unescape `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">텍스트</span>

- 주어진 텍스트를 경로로 처리:

`systemd-escape --path `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">텍스트</span>

- 이스케이프된 텍스트에 주어진 접미사 추가:

`systemd-escape --suffix `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">접미사</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">텍스트</span>

- 템플릿을 사용하여 이스케이프된 텍스트 삽입:

`systemd-escape --template `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">템플릿</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">텍스트</span>
