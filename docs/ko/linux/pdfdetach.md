---
layout: page
title: linux/pdfdetach (한국어)
description: "PDF 파일에서 첨부 파일(내장 파일)을 나열하거나 추출."
content_hash: 4104474a1b90605a4fd388b562a9358aea985223
last_modified_at: 2024-10-29
related_topics:
  - title: English version
    url: /en/linux/pdfdetach.html
    icon: bi bi-globe
tldri18n_status: 2
---
# pdfdetach

PDF 파일에서 첨부 파일(내장 파일)을 나열하거나 추출.
같이 보기: `pdfattach`, `pdfimages`, `pdfinfo`.
더 많은 정보: <https://manned.org/pdfdetach>.

- 특정 텍스트 인코딩으로 파일의 모든 첨부 파일 나열:

`pdfdetach list -enc `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">UTF-8</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/입력.pdf</span>

- 번호를 지정하여 특정 내장 파일 저장:

`pdfdetach -save `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">번호</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/입력.pdf</span>

- 이름을 지정하여 특정 내장 파일 저장:

`pdfdetach -savefile `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">이름</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/입력.pdf</span>

- 사용자 지정 출력 파일 이름으로 내장 파일 저장:

`pdfdetach -save `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">번호</span>` -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/입력.pdf</span>

- 소유자/사용자 암호로 보호된 파일에서 첨부 파일 저장:

`pdfdetach -save `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">번호</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-opw|-upw</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">암호</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/입력.pdf</span>
