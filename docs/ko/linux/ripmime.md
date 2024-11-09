---
layout: page
title: linux/ripmime (한국어)
description: "MIME 인코딩된 이메일 패키지에서 첨부 파일 추출."
content_hash: 46335275619da299cd6c784c0ebc5fc75ac1fb5f
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/linux/ripmime.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/ripmime.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># ripmime

MIME 인코딩된 이메일 패키지에서 첨부 파일 추출.
더 많은 정보: <https://pldaniels.com/ripmime>.

- 현재 디렉토리에 파일 내용 추출:

`ripmime -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- 특정 디렉토리에 파일 내용 추출:

`ripmime -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>` -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/폴더</span>

- 파일 내용을 추출하고 자세한 출력 표시:

`ripmime -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>` -v`

- 전체 디코딩 과정에 대한 자세한 정보 얻기:

`ripmime -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>` --debug`
