---
layout: page
title: freebsd/sockstat (English)
description: "List open Internet or UNIX domain sockets."
content_hash: 21297b369bcb64cca176a5883f690032488ce375
last_modified_at: 2024-01-15
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/freebsd/sockstat.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># sockstat

List open Internet or UNIX domain sockets.
More information: <https://man.freebsd.org/cgi/man.cgi?sockstat>.

- View which users/processes are [l]istening on which ports:

`sockstat -l`

- Show information for IPv[4]/IPv[6] sockets [l]istening on specific [p]orts using a specific [P]rotocol:

`sockstat -`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">4|6</span>` -l -P `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">tcp|udp|sctp|divert</span>` -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">port1,port2...</span>

- Also show [c]onnected sockets, not resolving [n]umeric UIDs to user names and using a [w]ider field size:

`sockstat -cnw`

- Only show sockets that belong to a specific [j]ail ID or name in [v]erbose mode:

`sockstat -jv`

- Display the protocol [s]tate and the remote [U]DP encapsulation port number, if applicable (these are currently only implemented for SCTP and TCP):

`sockstat -sU`

- Display the [C]ongestion control module and the protocol [S]tack, if applicable (these are currently only implemented for TCP):

`sockstat -CS`

- Only show Internet sockets if the local and foreign addresses are not in the loopback network prefix 127.0.0.0/8, or do not contain the IPv6 loopback address ::1:

`sockstat -L`

- Do not show the header ([q]uiet mode), showing [u]nix sockets and displaying the `inp_gencnt`:

`sockstat -qui`
