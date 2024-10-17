---
layout: page
title: windows/test-json (한국어)
description: "문자열이 유효한 JSON 문서인지 여부를 테스트합니다."
content_hash: 6dbd67a2c08055443783a553dc4c5b0e14592d16
last_modified_at: 2024-10-17
related_topics:
  - title: English version
    url: /en/windows/test-json.html
    icon: bi bi-globe
tldri18n_status: 2
---
# Test-Json

문자열이 유효한 JSON 문서인지 여부를 테스트합니다.
참고: 이 명령어는 PowerShell을 통해서만 사용할 수 있습니다.
더 많은 정보: <https://learn.microsoft.com/powershell/module/microsoft.powershell.utility/test-json>.

- `stdin`에서 문자열이 JSON 형식인지 테스트:

`'`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">문자열</span>`' | Test-Json`

- 문자열이 JSON 형식인지 테스트:

`Test-Json -Json '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">테스트_대상_json</span>`'`

- `stdin`에서 문자열이 특정 스키마 파일과 일치하는지 테스트:

`'`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">문자열</span>`' | Test-Json -SchemaFile `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로\대상\스키마_파일.json</span>
