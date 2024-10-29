---
layout: page
title: linux/zip (한국어)
description: "파일을 Zip 압축 파일로 패키징하고 압축."
content_hash: 3c768e088d1dbfee120d16c3a6a57951f01035eb
last_modified_at: 2024-10-29
related_topics:
  - title: English version
    url: /en/linux/zip.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/linux/zip.html
    icon: bi bi-globe
tldri18n_status: 2
---
# zip

파일을 Zip 압축 파일로 패키징하고 압축.
같이 보기: `unzip`.
더 많은 정보: <https://manned.org/zip>.

- 특정 아카이브에 파일/디렉터리 추가:

`zip -r `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/압축.zip</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일_또는_폴더1 경로/대상/파일_또는_폴더2 ...</span>

- 특정 아카이브에서 파일/디렉터리 제거:

`zip --delete `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/압축.zip</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일_또는_폴더1 경로/대상/파일_또는_폴더2 ...</span>

- 특정 파일/디렉터리를 제외하고 아카이브:

`zip `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/압축.zip</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일_또는_폴더1 경로/대상/파일_또는_폴더2 ...</span>` --exclude `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/제외할_파일_또는_폴더</span>

- 특정 압축 수준(`0` - 가장 낮음, `9` - 가장 높음)으로 파일/디렉터리 아카이브:

`zip -r -`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">0..9</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/압축.zip</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일_또는_폴더1 경로/대상/파일_또는_폴더2 ...</span>

- 특정 비밀번호로 암호화된 아카이브 생성:

`zip -r --encrypt `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/압축.zip</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일_또는_폴더1 경로/대상/파일_또는_폴더2 ...</span>

- 여러 부분으로 나눈 Zip 아카이브로 파일/디렉터리 아카이브 (예: 3GB 파트):

`zip -r -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">3g</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/압축.zip</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일_또는_폴더1 경로/대상/파일_또는_폴더2 ...</span>

- 특정 아카이브 내용 출력:

`zip -sf `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/압축.zip</span>
