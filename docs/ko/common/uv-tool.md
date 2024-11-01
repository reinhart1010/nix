---
layout: page
title: common/uv-tool (한국어)
description: "Python 패키지가 제공하는 명령을 설치하고 실행."
content_hash: e5aa274a2c64752b3dcdbb9a185549af3452e250
last_modified_at: 2024-11-01
related_topics:
  - title: English version
    url: /en/common/uv-tool.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/uv-tool.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># uv tool

Python 패키지가 제공하는 명령을 설치하고 실행.
더 많은 정보: <https://docs.astral.sh/uv/reference/cli/#uv-tool>.

- 패키지를 설치하지 않고 명령 실행:

`uv tool run `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">명령</span>

- Python 패키지를 시스템 전역에 설치:

`uv tool install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">패키지</span>

- 설치된 Python 패키지 업그레이드:

`uv tool upgrade `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">패키지</span>

- Python 패키지 제거:

`uv tool uninstall `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">패키지</span>

- 시스템 전역에 설치된 Python 패키지 나열:

`uv tool list`
