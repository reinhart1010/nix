---
layout: page
title: linux/pdfattach (한국어)
description: "기존 PDF 파일에 새 첨부 파일(내장 파일)을 추가."
content_hash: 4a750c545b3b907c7c01c36d4a834fe360b39e4e
last_modified_at: 2024-10-29
related_topics:
  - title: English version
    url: /en/linux/pdfattach.html
    icon: bi bi-globe
tldri18n_status: 2
---
# pdfattach

기존 PDF 파일에 새 첨부 파일(내장 파일)을 추가.
같이 보기: `pdfdetach`, `pdfimages`, `pdfinfo`.
더 많은 정보: <https://manned.org/pdfattach>.

- 기존 PDF 파일에 새 첨부 파일 추가:

`pdfattach `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/input.pdf</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/첨부할_파일</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/output.pdf</span>

- 같은 이름의 첨부 파일이 존재할 경우 교체:

`pdfattach -replace `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/input.pdf</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/첨부할_파일</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/output.pdf</span>

- 도움말 표시:

`pdfattach -h`

- 버전 표시:

`pdfattach -v`
