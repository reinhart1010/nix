---
layout: page
title: osx/osascript (English)
description: "Run AppleScript or JavaScript for Automation (JXA) from the command-line."
content_hash: 2a790a3fbccc86970e6b92220b4241154062ba5b
related_topics:
  - title: 中文 version
    url: /zh/osx/osascript.html
    icon: bi bi-globe
---
# osascript

Run AppleScript or JavaScript for Automation (JXA) from the command-line.
More information: <https://ss64.com/osx/osascript.html>.

- Run an AppleScript command:

`osascript -e '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">say "Hello world"</span>`'`

- Run multiple AppleScript commands:

`osascript -e '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">say "Hello"</span>`' -e '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">say "world"</span>`'`

- Run a compiled (`*.scpt`), bundled (`*.scptd`), or plaintext (`*.applescript`) AppleScript file:

`osascript `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/apple.scpt</span>

- Get the bundle identifier of an application (useful for `open -b`):

`osascript -e 'id of app "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Application</span>`"'`

- Run a JavaScript command:

`osascript -l JavaScript -e '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">console.log("Hello world");</span>`'`

- Run a JavaScript file:

`osascript -l JavaScript `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/script.js</span>
