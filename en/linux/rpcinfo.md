---
layout: page
title: linux/rpcinfo (English)
description: "Makes an RPC call to an RPC server and reports what it finds."
content_hash: 4581ad88e0c3fecf456aa4bc65808169f5772566
---
# rpcinfo

Makes an RPC call to an RPC server and reports what it finds.

- Show full table of all RPC services registered on localhost:

`rpcinfo`

- Show concise table of all RPC services registered on localhost:

`rpcinfo -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">localhost</span>

- Display table of statistics of rpcbind operations on localhost:

`rpcinfo -m`

- Display list of entries of given service name (mountd) and version number (2) on a remote nfs share:

`rpcinfo -l `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">remote_nfs_server_ip</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">mountd</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">2</span>

- Delete the registration for version 1 of the mountd service for all transports:

`rpcinfo -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">mountd</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1</span>
