---
layout: page
title: linux/po4a-gettextize (한국어)
description: "파일을 PO 파일로 변환합니다."
content_hash: 8060b0e3de624ec8381c4dfd8e2432f1d70170ef
last_modified_at: 2024-11-10
related_topics:
  - title: English version
    url: /en/linux/po4a-gettextize.html
    icon: bi bi-globe
tldri18n_status: 2
---
# po4a-gettextize

파일을 PO 파일로 변환합니다.
더 많은 정보: <https://po4a.org/man/man1/po4a-gettextize.1.php>.

- 텍스트 파일을 PO 파일로 변환:

`po4a-gettextize --format `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">text</span>` --master `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/원본.txt</span>` --po `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/결과.po</span>

- 사용 가능한 모든 형식 나열:

`po4a-gettextize --help-format`

- 번역된 문서와 함께 텍스트 파일을 PO 파일로 변환 (`-l` 옵션은 여러 번 제공할 수 있음):

`po4a-gettextize --format `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">text</span>` --master `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/원본.txt</span>` --localized `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/번역된.txt</span>` --po `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/결과.po</span>
