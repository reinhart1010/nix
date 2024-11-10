---
layout: page
title: common/sphinx-build (한국어)
description: "Sphinx 문서 생성기."
content_hash: da66a165513bc564461075e73888e072ecb64300
last_modified_at: 2024-11-10
related_topics:
  - title: English version
    url: /en/common/sphinx-build.html
    icon: bi bi-globe
tldri18n_status: 2
---
# sphinx-build

Sphinx 문서 생성기.
더 많은 정보: <https://www.sphinx-doc.org/en/master/man/sphinx-build.html>.

- 문서 빌드:

`sphinx-build -b `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">html|epub|text|latex|man|...</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/소스_폴더</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/빌드_폴더</span>

- readthedocs.io를 위한 문서 빌드 (sphinx-rtd-theme pip 패키지가 필요):

`sphinx-build -b `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">html</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/문서_폴더</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/빌드_폴더</span>
