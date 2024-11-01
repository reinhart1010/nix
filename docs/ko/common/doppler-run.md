---
layout: page
title: common/doppler-run (한국어)
description: "환경에 주입된 Doppler 비밀 정보를 사용하여 명령을 실행."
content_hash: 72c32b06983fc8adb1e2fcfee03fdca5444fcae0
last_modified_at: 2024-11-01
related_topics:
  - title: English version
    url: /en/common/doppler-run.html
    icon: bi bi-globe
tldri18n_status: 2
---
# doppler run

환경에 주입된 Doppler 비밀 정보를 사용하여 명령을 실행.
더 많은 정보: <https://docs.doppler.com/docs/cli#run-a-command-with-secrets-populated-in-environment>.

- 명령어 실행:

`doppler run --command `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">명령어</span>

- 다중 명령어 실행:

`doppler run --command `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">명령어1 && 명령어2</span>

- 스크립트 실행:

`doppler run `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/명령어.sh</span>

- 지정된 프로젝트 및 구성으로 명령을 실행:

`doppler run -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">프로젝트_이름</span>` -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">구성_이름</span>` -- `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">명령어</span>

- 비밀이 변경되면 자동으로 프로세스를 다시 시작:

`doppler run --watch `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">명령어</span>
