---
layout: page
title: common/rhash (한국어)
description: "일반적인 메시지 다이제스트를 계산하거나 확인."
content_hash: 87b893908598767297f7f5471850becddc7df5a9
last_modified_at: 2024-11-08
related_topics:
  - title: English version
    url: /en/common/rhash.html
    icon: bi bi-globe
tldri18n_status: 2
---
# rhash

일반적인 메시지 다이제스트를 계산하거나 확인.
더 많은 정보: <https://rhash.sourceforge.net/manpage.php>.

- 파일의 기본 CRC32 다이제스트 계산:

`rhash `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- 디렉터리를 재귀적으로 처리하여 SHA1을 사용한 SFV 파일 생성:

`rhash --sha1 --recursive `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/폴더</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력.sfv</span>

- SFV 파일을 기반으로 파일의 무결성 확인:

`rhash --check `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.sfv</span>

- 텍스트 메시지의 SHA3 다이제스트 계산:

`rhash --sha3-256 --message '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">메시지</span>`'`

- 파일의 CRC32 다이제스트를 계산하고 BSD 형식을 사용하여 base64로 인코딩된 다이제스트 출력:

`rhash --base64 --bsd `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- 사용자 정의 출력 템플릿 사용:

`rhash --printf '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">%p\t%s\t%{mtime}\t%m\n</span>`' `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>
