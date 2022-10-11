---
layout: page
title: common/aws-route53 (English)
description: "CLI for AWS Route53 - Route 53 is a highly available and scalable Domain Name System (DNS) web service."
content_hash: 941bed44d94b4db508fa6c3178778c95f0eb40f1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># aws route53

CLI for AWS Route53 - Route 53 is a highly available and scalable Domain Name System (DNS) web service.
More information: <https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53/index.html>.

- List all hosted zones, private and public:

`aws route53 list-hosted-zones`

- Show all records in a zone:

`aws route53 list-resource-record-sets --hosted-zone-id `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">zone_id</span>

- Create a new, public zone using a request identifier to retry the operation safely:

`aws route53 create-hosted-zone --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">name</span>` --caller-reference `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">request_identifier</span>

- Delete a zone (if the zone has non-defaults SOA and NS records the command will fail):

`aws route53 delete-hosted-zone --id `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">zone_id</span>

- Test DNS resolving by Amazon servers of a given zone:

`aws route53 test-dns-answer --hosted-zone-id `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">zone_id</span>`  --record-name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">name</span>` --record-type `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">type</span>
