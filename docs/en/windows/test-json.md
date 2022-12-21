---
layout: page
title: windows/test-json (English)
description: "Tests whether a string is a valid JSON document."
content_hash: 37b524b449d91ceec3440941d40b2c37a2382d3d
last_modified_at: 2022-12-21
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># Test-Json

Tests whether a string is a valid JSON document.
This command can only be used through PowerShell.
More information: <https://learn.microsoft.com/powershell/module/microsoft.powershell.utility/test-json>.

- Test if a string from stdin is in JSON format:

`'`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">string</span>`' | Test-Json`

- Test if a string JSON format:

`Test-Json -Json '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">json_to_test</span>`'`

- Test if a string from stdin matches a specific schema file:

`'`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">string</span>`' | Test-Json -SchemaFile `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/schema.json</span>
