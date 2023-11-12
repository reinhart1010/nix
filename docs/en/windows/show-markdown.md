---
layout: page
title: windows/show-markdown (English)
description: "Shows a Markdown file or string in the console in a friendly way using VT100 escape sequences or in a browser using HTML."
content_hash: 1f0b68fd0e14311c13892ef1f87e0fd03c38c997
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# Show-Markdown

Shows a Markdown file or string in the console in a friendly way using VT100 escape sequences or in a browser using HTML.
This command can only be used through PowerShell.
More information: <https://learn.microsoft.com/powershell/module/microsoft.powershell.utility/show-markdown>.

- Render markdown to console from a file:

`Show-Markdown -Path `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path\to\file</span>

- Render markdown to console from string:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">"# Markdown content"</span>` | Show-Markdown`

- Open Markdown file in a browser:

`Show-Markdown -Path `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path\to\file</span>` -UseBrowser`
