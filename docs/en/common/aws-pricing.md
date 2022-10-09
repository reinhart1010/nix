---
layout: page
title: common/aws-pricing (English)
description: "Query services, products, and pricing information from Amazon Web Services."
content_hash: 388c0ebf54c51dea3732f7f35058319c96ac8b99
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># aws pricing

Query services, products, and pricing information from Amazon Web Services.
More information: <https://docs.aws.amazon.com/cli/latest/reference/pricing/>.

- List service codes of a specific region:

`aws pricing describe-services --region `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">us-east-1</span>

- List attributes for a given service code in a specific region:

`aws pricing describe-services --service-code `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">AmazonEC2</span>` --region `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">us-east-1</span>

- Print pricing information for a service code in a specific region:

`aws pricing get-products --service-code `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">AmazonEC2</span>` --region `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">us-east-1</span>

- List values for a specific attribute for a service code in a specific region:

`aws pricing get-attribute-values --service-code `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">AmazonEC2</span>` --attribute-name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">instanceType</span>` --region `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">us-east-1</span>

- Print pricing information for a service code using filters for instance type and location:

`aws pricing get-products --service-code `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">AmazonEC2</span>` --filters "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Type=TERM_MATCH,Field=instanceType,Value=m5.xlarge</span>`" "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Type=TERM_MATCH,Field=location,Value=US East (N. Virginia)</span>`" --region `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">us-east-1</span>
