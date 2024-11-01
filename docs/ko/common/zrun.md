---
layout: page
title: common/zrun (한국어)
description: "인수 파일을 명령어에 투명하게 압축 해제하여 실행."
content_hash: 05f17a78b13116244e30c6af0d33461066dab9d2
last_modified_at: 2024-11-01
related_topics:
  - title: English version
    url: /en/common/zrun.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/zrun.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># zrun

인수 파일을 명령어에 투명하게 압축 해제하여 실행.
더 많은 정보: <https://joeyh.name/code/moreutils/>.

- 압축된 인수 파일의 압축을 해제하여 지정된 명령 실행:

`zrun `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">cat 경로/대상/파일1.gz 경로/대상/파일2.bz2 ...</span>
