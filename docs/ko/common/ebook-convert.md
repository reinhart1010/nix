---
layout: page
title: common/ebook-convert (한국어)
description: "일반적인 형식 간 전자책을 변환하는 데 사용 가능(예: PDF, EPUB 및 MOBI)."
content_hash: 7e85aac82a0637d7ff9d098a938eec6df0fcfa6b
last_modified_at: 2024-10-16
related_topics:
  - title: Deutsch version
    url: /de/common/ebook-convert.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/ebook-convert.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/ebook-convert.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/ebook-convert.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/ebook-convert.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># ebook-convert

일반적인 형식 간 전자책을 변환하는 데 사용 가능(예: PDF, EPUB 및 MOBI).
Calibre 전자책 라이브러리 도구의 일부.
더 많은 정보: <https://manual.calibre-ebook.com/generated/en/ebook-convert.html>.

- 전자책을 다른 형식으로 변환:

`ebook-convert `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/입력_파일</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">출력_파일</span>

- Markdown 또는 HTML을 목차, 제목 및 저자가 포함된 전자책으로 변환:

`ebook-convert `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/입력_파일</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">출력_파일</span>` --level1-toc="//h:h1" --level2-toc="//h:h2" --level3-toc="//h:h3" --title=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">title</span>` --authors=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">author</span>
