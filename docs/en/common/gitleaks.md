---
layout: page
title: common/gitleaks (English)
description: "Detect secrets and API keys leaked in Git repositories."
content_hash: 981d3fdd9dd02893e11d9f72f8ba9efd54ab21b5
last_modified_at: 2024-04-25
tldri18n_status: 2
---
# gitleaks

Detect secrets and API keys leaked in Git repositories.
More information: <https://github.com/gitleaks/gitleaks>.

- Scan a remote repository:

`gitleaks detect --repo-url `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://github.com/username/repository.git</span>

- Scan a local directory:

`gitleaks detect --source `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/repository</span>

- Output scan results to a JSON file:

`gitleaks detect --source `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/repository</span>` --report `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/report.json</span>

- Use a custom rules file:

`gitleaks detect --source `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/repository</span>` --config-path `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/config.toml</span>

- Start scanning from a specific commit:

`gitleaks detect --source `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/repository</span>` --log-opts `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">--since=commit_id</span>

- Scan uncommitted changes before a commit:

`gitleaks protect --staged`

- Display verbose output indicating which parts were identified as leaks during the scan:

`gitleaks protect --staged --verbose`
