---
layout: page
title: osx/osascript (English)
description: "Run AppleScript or JavaScript for Automation (JXA)."
content_hash: 9278d3594a1ee3f223a101dab7959ceff1710d62
last_modified_at: 2024-01-31
related_topics:
  - title: español version
    url: /es/osx/osascript.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/osx/osascript.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/osx/osascript.html
    icon: bi bi-globe
tldri18n_status: 2
---
# osascript

Run AppleScript or JavaScript for Automation (JXA).
More information: <https://keith.github.io/xcode-man-pages/osascript.1.html>.

- Run an AppleScript command:

`osascript -e "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">say 'Hello world'</span>`"`

- Run multiple AppleScript commands:

`osascript -e "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">say 'Hello'</span>`" -e "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">say 'world'</span>`"`

- Run a compiled (`*.scpt`), bundled (`*.scptd`), or plaintext (`*.applescript`) AppleScript file:

`osascript `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/apple.scpt</span>

- Get the bundle identifier of an application (useful for `open -b`):

`osascript -e 'id of app "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Application</span>`"'`

- Run a JavaScript command:

`osascript -l JavaScript -e "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">console.log('Hello world');</span>`"`

- Run a JavaScript file:

`osascript -l JavaScript `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/script.js</span>
