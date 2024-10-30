---
layout: page
title: common/grafana-cli (한국어)
description: "Grafana 서브와 함께 번들로 제공되는 작은 실행 파일."
content_hash: 4e6ac9784f81ea95f2d9b6eef4aa0ddbfa597404
last_modified_at: 2024-10-30
related_topics:
  - title: English version
    url: /en/common/grafana-cli.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/grafana-cli.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># grafana-cli

Grafana 서브와 함께 번들로 제공되는 작은 실행 파일.
더 많은 정보: <https://grafana.com/docs/grafana/latest/cli/>.

- 특정 플러그인을 설치, 업데이트 또는 제거:

`grafana-cli plugins `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">install|update|remove</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">플러그인_아이디1 플러그인_아이디2 ...</span>

- 설치된 모든 플러그인을 나열:

`grafana-cli plugins ls`
