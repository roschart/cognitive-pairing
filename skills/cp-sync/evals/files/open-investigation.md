# Work: Exporter Investigation

## Executive Summary

Duplicate histogram samples are confirmed at the application's original
exporter, not introduced by the proxy. A candidate fix is deployed to
staging, but validation is pending. Next: capture OpenMetrics responses
and compare them with scrape warnings before claiming resolution.

## Tasks

- [ ] Validate the staging patch with OpenMetrics 1.0 responses and
    matching scrape warnings over 30 minutes.
- [ ] Identify why two meter providers remain active in worker restarts.
- [ ] Prepare the final PR only after both checks pass.
- [x] Reproduce duplicates before proxy merging.

## Evidence Still Needed

The baseline capture on 2026-07-01 contains 22 extra samples for
`request_duration_seconds`, including `_bucket`, `_sum`, `_count`, and
`_created`. Plain text has 21 extra samples; OpenMetrics has 22.
The labels are `scope="Worker.Core"` and `scope_version="2.4.1"`.
Two `_created` values are `1782864000.125` and `1782864000.150`.
They are metric values, not explicit sample timestamps.

An earlier analyzer incorrectly required different repeated values.
Identical-value duplicates must count too. The original endpoint is
`http://127.0.0.1:8081/metrics`; the proxy endpoint is
`http://127.0.0.1:15020/stats/prometheus`. Both show the same duplicates.
Use `Accept: application/openmetrics-text; version=1.0.0` for comparison.

## Constraints

Do not drop histogram families: the pending latency acceptance check
depends on them. Provider duplication is a hypothesis, not a confirmed
cause. The old capture is the only baseline for the pending comparison.
Staging deployment is confirmed, but no post-deployment metrics have
been observed. Production has not been changed.
