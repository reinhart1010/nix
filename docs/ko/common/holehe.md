---
layout: page
title: common/holehe (한국어)
description: "Twitter, Instagram, Imgur 등 120개 이상의 사이트에서 이메일이 계정에 첨부되어 있는지 확인."
content_hash: 3718217942060dc97288f168f8af3c267bc76b19
last_modified_at: 2024-11-02
related_topics:
  - title: English version
    url: /en/common/holehe.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/holehe.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># holehe

Twitter, Instagram, Imgur 등 120개 이상의 사이트에서 이메일이 계정에 첨부되어 있는지 확인.
더 많은 정보: <https://github.com/megadose/holehe#-cli-example>.

- 지정된 이메일 주소에 대해 지원하는 모든 웹 사이트의 상태를 표시:

`holehe `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">사용자명@example.org</span>

- 지정된 이메일 주소가 사용중인 사이트에 대해서만 상태를 표시:

`holehe `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">사용자명@example.org</span>` --only-used`
