---
layout: page
title: common/tar (한국어)
description: "아카이브 유틸리티."
content_hash: c538d93f9c27ae4cdadd86380f9c2b49f22176e6
last_modified_at: 2024-11-09
related_topics:
  - title: Deutsch version
    url: /de/common/tar.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/tar.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/tar.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/tar.html
    icon: bi bi-globe
  - title: 日本語 version
    url: /ja/common/tar.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/tar.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/tar.html
    icon: bi bi-globe
  - title: русский version
    url: /ru/common/tar.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/tar.html
    icon: bi bi-globe
  - title: українська version
    url: /uk/common/tar.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/tar.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/tar.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># tar

아카이브 유틸리티.
종종 `gzip` 또는 `bzip2`와 같은 압축 방법과 결합하여 사용됩니다.
더 많은 정보: <https://www.gnu.org/software/tar>.

- 아카이브 생성 후 파일로 저장:

`tar cf `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.tar</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일1 경로/대상/파일2 ...</span>

- g[z]ipped 아카이브 생성 후 파일로 저장:

`tar czf `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.tar.gz</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일1 경로/대상/파일2 ...</span>

- 디렉토리에서 상대 경로를 사용하여 g[z]ipped (압축된) 아카이브 생성:

`tar czf `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.tar.gz</span>` --directory=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/폴더</span>` .`

- (압축된) 아카이브 파일을 현재 디렉토리에 상세히 추출:

`tar xvf `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/원본.tar[.gz|.bz2|.xz]</span>

- (압축된) 아카이브 파일을 대상 디렉토리에 추출:

`tar xf `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/원본.tar[.gz|.bz2|.xz]</span>` --directory=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/폴더</span>

- 파일 확장자를 사용하여 압축 프로그램을 자동으로 결정하고 압축 아카이브 생성 후 파일로 저장:

`tar caf `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.tar.xz</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일1 경로/대상/파일2 ...</span>

- tar 파일의 내용을 상세히 목록화:

`tar tvf `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/원본.tar</span>

- 아카이브 파일에서 패턴과 일치하는 파일 추출:

`tar xf `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/원본.tar</span>` --wildcards "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">*.html</span>`"`
