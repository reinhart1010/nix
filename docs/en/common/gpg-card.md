---
layout: page
title: common/gpg-card (English)
description: "Administrate OpenPGP and PIV smart cards."
content_hash: 1110e1082202ffd8e3f062790eb68b50496e5b33
last_modified_at: 2023-12-07
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/gpg-card.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># gpg-card

Administrate OpenPGP and PIV smart cards.
Similar to `gpg --card-edit`.
More information: <https://manned.org/gpg-card>.

- Start in interactive mode:

`gpg-card`

- Invoke one or more commands non-interactively:

`gpg-card `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command1</span>` -- `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command2</span>` -- `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command3</span>

- Show information about a smart card:

`gpg-card list`

- Retrieve the public key using the URL stored on an OpenPGP card:

`gpg-card fetch`

- Set the URL used by the `fetch` command:

`gpg-card url`

- Change or unblock PINs (uses the default action for the card in non-interactive mode):

`gpg-card passwd`

- Toggle the forcesig flag of an OpenPGP card (i.e. require entering the user PIN for signing):

`gpg-card forcesig`

- Factory reset a smart card (i.e. delete all data and reset PINs):

`gpg-card factory-reset`
