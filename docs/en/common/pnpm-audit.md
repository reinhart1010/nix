---
layout: page
title: common/pnpm-audit (English)
description: "Scan project dependencies."
content_hash: e6fb3f060a1e20b3a82a944efa8dca5838715d6b
last_modified_at: 2024-03-04
tldri18n_status: 2
---
# pnpm audit

Scan project dependencies.
Check for known security issues with the installed packages.
More information: <https://pnpm.io/cli/audit>.

- Identify vulnerabilities in the project:

`pnpm audit`

- Automatically fix vulnerabilities:

`pnpm audit fix`

- Generate a security report in JSON format:

`pnpm audit --json > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/audit-report.json</span>

- Audit only [D]ev dependencies:

`pnpm audit --dev`

- Audit only [P]roduction dependencies:

`pnpm audit --prod`

- Exclude optional dependencies from the audit:

`pnpm audit --no-optional`

- Ignore registry errors during the audit process:

`pnpm audit --ignore-registry-errors`

- Filter advisories by severity (low, moderate, high, critical):

`pnpm audit --audit-level `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">severity</span>
