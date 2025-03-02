---
layout: page
title: common/doppler-secrets (한국어)
description: "Doppler 프로젝트의 비밀을 관리."
content_hash: 13a875a860efadf5c3af6940a36eae0e45498be0
last_modified_at: 2024-11-01
related_topics:
  - title: English version
    url: /en/common/doppler-secrets.html
    icon: bi bi-globe
tldri18n_status: 2
---
# doppler secrets

Doppler 프로젝트의 비밀을 관리.
더 많은 정보: <https://docs.doppler.com/docs/accessing-secrets>.

- 모든 비밀을 얻기:

`doppler secrets`

- 하나 이상의 비밀 값을 가져오기:

`doppler secrets get `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">비밀</span>

- 비밀 파일 업로드:

`doppler secrets upload `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.env</span>

- 하나 이상의 비밀 값을 삭제:

`doppler secrets delete `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">비밀</span>

- 비밀을 `.env`로 다운로드:

`doppler secrets download --format=env --no-file > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/.env</span>
