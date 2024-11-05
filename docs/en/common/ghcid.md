---
layout: page
title: common/ghcid (English)
description: "Simple and efficient CLI IDE for Haskell that reloads code on file changes."
content_hash: 0a7bf9e77aa2e20c2a0b1bb3b26fddfe67bdf4d0
last_modified_at: 2024-11-05
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/ghcid.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># ghcid

Simple and efficient CLI IDE for Haskell that reloads code on file changes.
Continuously displays compile errors, warnings, and test results.
More information: <https://github.com/ndmitchell/ghcid>.

- Start `ghcid` and monitor a Haskell file for changes:

`ghcid `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/Main.hs</span>

- Start `ghcid` with a specific command, such as loading a Stack or Cabal project:

`ghcid --command "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">stack ghci Main.hs</span>`"`

- Run an action (default `main`) on each file save:

`ghcid --run=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">action</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/Main.hs</span>

- Set maximum height and width (default to console height and width):

`ghcid --height=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">height</span>` --width=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">width</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/Main.hs</span>

- Write full GHC compiler output to a file:

`ghcid --outputfile=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output_file.txt</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/Main.hs</span>

- Execute REPL commands (eg. `-- $> 1+1`) on each file save:

`ghcid --allow-eval `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/Main.hs</span>
