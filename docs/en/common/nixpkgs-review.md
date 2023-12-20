---
layout: page
title: common/nixpkgs-review (English)
description: "Review pull requests in the NixOS packages repository (nixpkgs)."
content_hash: 9f460d4b300bff5647fd5193809d6ab7d21145b7
last_modified_at: 2023-12-20
tldri18n_status: 2
---
# nixpkgs-review

Review pull requests in the NixOS packages repository (nixpkgs).
After a successful build, a `nix-shell` with all built packages is started.
More information: <https://github.com/Mic92/nixpkgs-review#usage>.

- Build changed packages in the specified pull request:

`nixpkgs-review pr `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pr_number|pr_url</span>

- Build changed packages and post a comment with a report (requires setting up a token in `hub`, `gh`, or the `GITHUB_TOKEN` environment variable):

`nixpkgs-review pr --post-result `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pr_number|pr_url</span>

- Build changed packages and print a report:

`nixpkgs-review pr --print-result `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pr_number|pr_url</span>

- Build changed packages in a local commit:

`nixpkgs-review rev `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">HEAD</span>

- Build changed packages that haven't been committed yet:

`nixpkgs-review wip`

- Build changed packages that have been staged:

`nixpkgs-review wip --staged`
