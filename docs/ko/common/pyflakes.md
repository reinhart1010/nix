---
layout: page
title: common/pyflakes (한국어)
description: "Python 소스 코드 파일에서 오류를 검사."
content_hash: a847ecba26af724b9c34533ee8c514a5618c66ec
last_modified_at: 2024-11-02
related_topics:
  - title: English version
    url: /en/common/pyflakes.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/pyflakes.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># pyflakes

Python 소스 코드 파일에서 오류를 검사.
더 많은 정보: <https://pypi.org/project/pyflakes>.

- 단일 Python 파일 검사:

`pyflakes check `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.py</span>

- 특정 폴더 내 Python 파일 검사:

`pyflakes checkPath `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/폴더</span>

- 폴더 내의 Python 파일을 재귀적으로 검사:

`pyflakes checkRecursive `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/폴더</span>

- 여러 폴더에서 발견된 모든 Python 파일 검사:

`pyflakes iterSourceCode `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/폴더_1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/폴더_2</span>
