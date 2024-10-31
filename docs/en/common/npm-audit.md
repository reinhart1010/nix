---
layout: page
title: common/npm-audit (English)
description: "Scan for known vulnerabilities in project dependencies."
content_hash: 7df1f8b69035eb249d40c33e1d76a6fab765991b
last_modified_at: 2024-10-31
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/npm-audit.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># npm audit

Scan for known vulnerabilities in project dependencies.
Reports vulnerabilities and suggests remediation.
More information: <https://docs.npmjs.com/cli/npm-audit>.

- Scan the project’s dependencies for known vulnerabilities:

`npm audit`

- Automatically fix vulnerabilities in the project's dependencies:

`npm audit fix`

- Force an automatic fix to dependencies with vulnerabilities:

`npm audit fix `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-f|--force</span>

- Update the lock file without modifying the `node_modules` directory:

`npm audit fix --package-lock-only`

- Perform a dry run. Simulate the fix process without making any changes:

`npm audit fix --dry-run`

- Output audit results in JSON format:

`npm audit --json`

- Configure the audit to only fail on vulnerabilities above a specified severity:

`npm audit --audit-level=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">info|low|moderate|high|critical</span>
