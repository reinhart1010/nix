---
layout: page
title: common/quarto (한국어)
description: "Pandoc 기반의 오픈 소스 과학 및 기술 출판 시스템."
content_hash: f56543081472a5a3268abeb522b85d25b507d6c4
last_modified_at: 2024-11-02
related_topics:
  - title: English version
    url: /en/common/quarto.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/quarto.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># quarto

Pandoc 기반의 오픈 소스 과학 및 기술 출판 시스템.
더 많은 정보: <https://quarto.org/>.

- 새 프로젝트 생성:

`quarto create-project `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/폴더</span>` --type `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">book|default|website</span>

- 새 블로그 웹사이트 생성:

`quarto create-project `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/폴더</span>` --type `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">website</span>` --template `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">blog</span>

- 입력 파일을 다양한 형식으로 렌더링:

`quarto render `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">qmd|rmd|ipynb}</span>`} --to `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">html|pdf|docx</span>

- 문서나 웹사이트를 렌더링하고 미리보기:

`quarto preview `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/폴더|경로/대상/파일</span>

- 문서나 프로젝트를 Quarto Pub, Github Pages, RStudio Connect 또는 Netlify에 게시:

`quarto publish `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">quarto-pub|gh-pages|connect|netlify</span>
