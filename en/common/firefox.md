---
layout: page
title: common/firefox (English)
description: "A free and open source web browser."
content_hash: 3b0791c84bdd7bd75993b367822ad231727abaa4
related_topics:
  - title: Deutsch version
    url: /de/common/firefox.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/firefox.html
    icon: bi bi-globe
---
# firefox

A free and open source web browser.
More information: <https://developer.mozilla.org/en-US/docs/Mozilla/Command_Line_Options>.

- Launch Firefox and open a web page:

`firefox `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://www.duckduckgo.com</span>

- Open a new window:

`firefox --new-window `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://www.duckduckgo.com</span>

- Open a private (incognito) window:

`firefox --private-window`

- Search for "wikipedia" using the default search engine:

`firefox --search "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">wikipedia</span>`"`

- Launch Firefox in safe mode, with all extensions disabled:

`firefox --safe-mode`

- Take a screenshot of a web page in headless mode:

`firefox --headless --screenshot `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output_file.png</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://example.com/</span>

- Use a specific profile to allow multiple separate instances of Firefox to run at once:

`firefox --profile `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://example.com/</span>

- Set Firefox as the default browser:

`firefox --setDefaultBrowser`
