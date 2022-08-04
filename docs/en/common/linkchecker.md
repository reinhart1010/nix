---
layout: page
title: common/linkchecker (English)
description: "Command-line client to check HTML documents and websites for broken links."
content_hash: 095ac8d900907bb081e9160b7663f3e08d214973
---
# linkchecker

Command-line client to check HTML documents and websites for broken links.
More information: <https://linkchecker.github.io/linkchecker/>.

- Find broken links on https://example.com/:

`linkchecker `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://example.com/</span>

- Also check URLs that point to external domains:

`linkchecker --check-extern `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://example.com/</span>

- Ignore URLs that match a specific regular expression:

`linkchecker --ignore-url `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">regular_expression</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://example.com/</span>

- Output results to a CSV file:

`linkchecker --file-output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">csv</span>`/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://example.com/</span>
