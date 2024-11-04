---
layout: page
title: windows/get-dedupproperties (한국어)
description: "데이터 중복 제거 정보 가져오기."
content_hash: 4205a7cd24203c55255694e83e83dc2fc52a05da
last_modified_at: 2024-11-04
related_topics:
  - title: English version
    url: /en/windows/get-dedupproperties.html
    icon: bi bi-globe
tldri18n_status: 2
---
# Get-DedupProperties

데이터 중복 제거 정보 가져오기.
참고: 이 명령은 PowerShell을 통해서만 사용할 수 있습니다.
더 많은 정보: <https://learn.microsoft.com/powershell/module/storage/get-dedupproperties>.

- 드라이브의 데이터 중복 제거 정보 가져오기:

`Get-DedupProperties -DriveLetter 'C'`

- 드라이브 레이블을 사용하여 데이터 중복 제거 정보 가져오기:

`Get-DedupProperties -FileSystemLabel 'Label'`

- 입력 객체를 사용하여 드라이브의 데이터 중복 제거 정보 가져오기:

`Get-DedupProperties -InputObject $(Get-Volume -DriveLetter 'E')`
