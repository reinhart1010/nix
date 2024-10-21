---
layout: page
title: common/gdrive (한국어)
description: "Google 드라이브와 상호작용."
content_hash: cbc717212c073bbe3774dfd0e767ffc94e31fc64
last_modified_at: 2024-10-21
related_topics:
  - title: English version
    url: /en/common/gdrive.html
    icon: bi bi-globe
tldri18n_status: 2
---
# gdrive

Google 드라이브와 상호작용.
폴더/파일 ID는 구글 드라이브 폴더나 ID URL에서 얻을 수 있음.
더 많은 정보: <https://github.com/gdrive-org/gdrive>.

- 지정된 ID를 사용하여 상위 폴더에 대한 로컬 경로를 업로드:

`gdrive upload -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">아이디</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일_또는_폴더</span>

- ID 별로 파일이나 디렉터리를 현재 디렉터리로 다운로드:

`gdrive download `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">아이디</span>

- 해당 ID로 지정된 로컬 경로에 다운로드:

`gdrive download --path `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/폴더</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">아이디</span>

- 주어진 파일이나 폴더를 사용하여 ID의 새로운 개정판을 생성:

`gdrive update `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">아이디</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일_또는_폴더</span>
