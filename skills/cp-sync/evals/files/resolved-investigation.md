# Work: Exporter Investigation

## Executive Summary

This work began with duplicate samples in the exporter and several
competing explanations. The baseline was captured, an analyzer was
written, the analyzer was corrected, a patch was drafted, and the patch
was reviewed. The fix is now verified in staging. Next: send the handoff
and ask whether the final PR is ready for review.

## Why This Work Exists

Duplicate histogram samples caused rejected scrapes. The work covers
the application exporter and a bounded patch, not replacement of the
monitoring platform. Production rollout remains outside this work.

## Investigation Trail

The first capture at 09:01 contained 22 extra samples for the API and
180 for the scheduler. A second capture at 09:07 contained the same
counts. A third capture at 09:13 again contained 22 and 180. The sample
scope was `Worker.Core` version `2.4.1`. A discarded baseline from the
week before contained 72 scheduler duplicates; it is superseded.

| Application | Family | Extra samples |
| --- | --- | ---: |
| API | request duration | 22 |
| Scheduler | execution duration | 110 |
| Scheduler | execution delay | 70 |

At 09:20, the original exporter and merged proxy endpoint were compared.
Both contained the same metric names and label sets. The original
endpoint used port 8081 and the merged endpoint used port 15020.
The negotiated protocol was OpenMetrics 1.0. The API response had
two `_created` values, `1782864000.125` and `1782864000.150`.
The baseline had no explicit sample timestamps.

At 09:32, the analyzer initially missed identical-value duplicates.
At 09:41, the analyzer was corrected to group names and label sets
without requiring different values. At 09:48, it counted repeated
`_bucket`, `_sum`, `_count`, and `_created` samples. Plain text showed
21 API duplicates and OpenMetrics showed 22. These baseline details
are superseded by the completed comparison below and are not required
for audit, rollback, or further reproduction.

Initial hypotheses included proxy merging, relabeling, and a protocol
negotiation fault. These were rejected. Temporary family drops and
forcing plain text were considered and rejected. No such mitigation
was applied. The earlier concern about proxy ownership is resolved.

## Confirmed Outcome

Code review confirmed that two service registrations created independent
meter providers exporting the same instruments. The patch consolidates
them into one provider. An inspected automated regression test covers
duplicate registration, including identical-value samples. An inspected
30-minute staging comparison found zero duplicate series and zero
duplicate-sample scrape warnings, with the histogram families still
present. Production has not been validated or changed.

The fix is in [the patch](https://example.org/reviews/exporter-fix).
The [regression result](https://example.org/builds/exporter-regression)
and [staging report](https://example.org/reports/staging-scrape-check)
support the outcome. These are supplied reference links, not a request
to access an external system during sync.

## Decisions and Risks

Keep a single meter provider per process; reintroducing a second
registration would recreate the failure. The production rollback rule
remains active for the handoff: revert the patch if scrape success drops
below 99.5% for 10 minutes. The concern that proxy merging caused this
issue is closed and has no remaining impact.

## Tasks

- [x] Capture the original endpoint.
- [x] Capture the proxy endpoint.
- [x] Record baseline counts at 09:01.
- [x] Repeat the counts at 09:07 and 09:13.
- [x] Compare protocol negotiation.
- [x] Correct the analyzer.
- [x] Reject proxy and relabeling hypotheses.
- [x] Identify the duplicate service registrations.
- [x] Consolidate meter providers.
- [x] Add the regression test.
- [x] Inspect the 30-minute staging comparison.
- [ ] Send the handoff with the active rollback rule and useful links.
- [ ] Ask the human whether the intended final PR is ready for review.

## Next Action

Send the handoff. Final PR readiness is not confirmed; do not archive.
