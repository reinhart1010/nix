---
layout: page
title: windows/test-json (English)
description: "Test whether a string is a valid JSON document."
content_hash: 44b745be58ed1c425ccf0532cb44f6c9d6d259cd
last_modified_at: 2023-11-15
tldri18n_status: 2
---
# Test-Json

Test whether a string is a valid JSON document.
This command can only be used through PowerShell.
More information: <https://learn.microsoft.com/powershell/module/microsoft.powershell.utility/test-json>.

- Test if a string from `stdin` is in JSON format:

`'`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">string</span>`' | Test-Json`

- Test if a string JSON format:

`Test-Json -Json '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">json_to_test</span>`'`

- Test if a string from `stdin` matches a specific schema file:

`'`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">string</span>`' | Test-Json -SchemaFile `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path\to\schema_file.json</span>
