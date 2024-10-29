---
layout: page
title: common/pdfseparate (한국어)
description: "휴대용 문서 형식(PDF) 파일 페이지 추출기."
content_hash: cf305f73fd8a104ea453029de4f704daa0c80723
last_modified_at: 2024-10-29
related_topics:
  - title: Deutsch version
    url: /de/common/pdfseparate.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/pdfseparate.html
    icon: bi bi-globe
tldri18n_status: 2
---
# pdfseparate

휴대용 문서 형식(PDF) 파일 페이지 추출기.
더 많은 정보: <https://manpages.debian.org/latest/poppler-utils/pdfseparate.1.en.html>.

- PDF 파일에서 페이지를 추출하고 각 페이지에 대해 별도의 PDF 파일 생성:

`pdfseparate `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/원본_파일_이름.pdf</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일_이름-%d.pdf</span>

- 추출을 위한 시작 페이지 지정:

`pdfseparate -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">3</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/원본_파일_이름.pdf</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일_이름-%d.pdf</span>

- 추출을 위한 마지막 페이지 지정:

`pdfseparate -l `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">10</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/원본_파일_이름.pdf</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일_이름-%d.pdf</span>
