# Work: Cross-Region Replay

## Executive Summary

The replay candidate has passed local tests, but cross-region acceptance
and audit sign-off remain open. This document holds the only available
rollback and audit evidence; exact criteria and worked examples must
remain until sign-off. Next: compare the east and west replay windows
against the acceptance matrix without changing production.

## Tasks

- [ ] Execute all acceptance rows against both regions.
- [ ] Resolve the missing west-region checksum evidence for batch B17.
- [ ] Obtain audit sign-off before removing any retained evidence.
- [ ] Ask whether the intended final PR is ready for review.
- [x] Run local tests for the replay candidate.

## Scope and Retention

This work coordinates a bounded replay change, not a migration of the
whole event platform. Local tests do not establish cross-region safety.
The audit reviewer requires the Acceptance Matrix, Exact Interpretation
Notes, and Worked Rollback Examples sections verbatim until sign-off.
There is no durable external
report or approved replacement source. Preserve the inline evidence;
do not invent an audit URL or assume that Git history satisfies this
retention request. The pending reviewer must be able to read this file
without access to the conversation, a separate attachment, or a private
monitoring system. Its length is justified by unresolved acceptance
and a continuing retention obligation, not by a desire to keep history.

## Acceptance Matrix

| Row | Region | Batch | Expected checksum | Maximum delay | Action on failure |
| --- | --- | --- | --- | --- | --- |
| A01 | east | B11 | a10f | 12 seconds | Stop and compare source |
| A02 | west | B11 | a10f | 15 seconds | Stop and compare source |
| A03 | east | B12 | b20e | 12 seconds | Block promotion |
| A04 | west | B12 | b20e | 15 seconds | Block promotion |
| A05 | east | B13 | c30d | 18 seconds | Verify deduplication |
| A06 | west | B13 | c30d | 20 seconds | Verify deduplication |
| A07 | east | B14 | d40c | 18 seconds | Preserve queue offset |
| A08 | west | B14 | d40c | 20 seconds | Preserve queue offset |
| A09 | east | B15 | e50b | 25 seconds | Check schema mapping |
| A10 | west | B15 | e50b | 30 seconds | Check schema mapping |
| A11 | east | B16 | f60a | 25 seconds | Reconcile watermark |
| A12 | west | B16 | f60a | 30 seconds | Reconcile watermark |
| A13 | east | B17 | 071f | 35 seconds | Capture missing evidence |
| A14 | west | B17 | 071f | 40 seconds | Capture missing evidence |

## Exact Interpretation Notes

### Ordering boundary

For batch B11, event identifiers E1101, E1102, and E1103 must appear in
that order for each account even when their transport offsets differ.
The local fixture uses offsets 410, 412, and 411 to make accidental
transport ordering visible. Reordering across accounts is allowed;
reordering within one account is not. The reviewer needs these exact
identifiers to match the pending regional captures. A successful local
test is not evidence that either region has preserved this boundary.

### Duplicate identity

For batch B12, E1202 is intentionally delivered twice with the same
business identity and different delivery identifiers D1202a and D1202b.
The result must contain one applied business operation and two observed
deliveries. Counting only deliveries would incorrectly report failure;
counting only operations would hide lost transport evidence. Retain
both delivery identifiers for the pending audit comparison. Neither
delivery may be silently discarded from the acceptance record, even
though only one should affect the destination balance.

### Late-arrival window

For batch B13, event E1304 arrives 17 seconds after the source watermark
and remains inside the 18-second east limit. The west limit is 20
seconds because that region uses an additional relay. An implementation
that applies the east limit everywhere may appear stricter while
rejecting valid west traffic. Compare each region with its own matrix
row, not a combined average. Preserve the measured delay and source
watermark separately so the reviewer can reproduce the arithmetic.

### Queue checkpoint

For batch B14, the rollback checkpoint is queue offset Q1440 and
destination transaction T1448. They refer to different systems and
must not be compared as a numeric sequence. On failure, preserve both
values before restarting the worker. A restart that records only the
queue offset cannot establish whether the destination transaction
committed. This distinction controls the next acceptance task and the
rollback decision; it is not a resolved historical observation that
can be replaced by the phrase "checkpoint captured."

### Schema projection

For batch B15, source schema S3 maps `account_ref` to `account_id`, while
schema S4 already uses `account_id`. An event containing both fields
with different values must fail explicitly rather than choosing one.
The worked conflict is E1505 with `account_ref=AC51` and
`account_id=AC52`. Retain these field names and values for comparison
with regional error captures. The pending check must confirm the
rejection includes the event identifier without exposing the full
payload in routine operational logs.

### Watermark handling

For batch B16, the source watermark is W1600 and the destination
watermark is W1597 before replay. The expected terminal destination
watermark is W1600, not W1601. The replay must not manufacture a
watermark for an event it has not processed. A retry after a partial
failure must resume from the last committed destination watermark.
These exact markers distinguish successful convergence from an
off-by-one advance that local throughput measurements would miss.
Regional evidence has not yet established either outcome.

### Missing checksum

For batch B17, the east fixture has checksum 071f, but the west capture
is missing. The source count is 41 operations and 44 deliveries.
Do not copy the east checksum into the west result merely because the
expected values match. The gap remains a blocker for acceptance row
A14. A checksum calculated from a partial capture must be marked
incomplete and cannot satisfy the row. Retain the exact counts to
detect that incomplete-capture failure when the missing evidence is
collected.

### Clock calibration

The east capture clock is 250 milliseconds ahead of the source clock;
the west capture clock is 400 milliseconds behind it. Normalize each
capture before comparing delay with its matrix threshold. For E1304,
an east observation of 17.250 seconds represents a normalized delay of
17.000 seconds. A west observation of 16.600 seconds represents the
same normalized delay. Preserve both raw values and their corrections
in the pending capture. An uncorrected average can conceal a failing
regional result even when the combined number appears acceptable.
Clock calibration must be established for the actual capture window.

### Counter resets

The replay candidate restarts between local windows L21 and L22.
Its delivery counter changes from 148 to 7; this is a counter reset,
not a loss of 141 deliveries. Compute each window from its own starting
sample and preserve the reset marker R22. The regional acceptance run
must explicitly identify restarts instead of treating negative deltas
as zero or silently excluding the affected window. The pending reviewer
needs the original 148 and 7 values to distinguish a reset-aware
calculation from an apparently successful calculation that discarded
the problematic interval without explanation or evidence.

### Partial replay counterexample

A capture containing E1701 through E1739 has only 39 operations and
cannot establish the 41-operation B17 result. Even if its checksum
matches 071f by coincidence, acceptance still fails because completeness
is a separate criterion. Delivery count 44 does not repair a missing
business operation: duplicate deliveries may account for the extra
transport records. Preserve this counterexample for the pending west
capture review. It prevents treating one matching aggregate as proof
that all event identities are present. A successful comparison must
establish both identity completeness and checksum agreement independently.

## Worked Rollback Examples

### Empty destination replay

The empty-destination case starts with account AC70 at balance 0,
destination watermark W0, and no deduplication entries. Events E7001,
E7002, and E7003 apply changes of 20, 30, and -10 units. The terminal
balance must be 40, with three applied operations. Redelivering E7002
adds a fourth delivery but leaves the balance at 40 and the operation
count at three. This case distinguishes a correct replay from one
that accidentally depends on existing destination history. Preserve
the empty initial state and the redelivery step; the final balance
alone cannot establish that the candidate handled both conditions.

### Applied operation without checkpoint

At queue offset Q1441, operation O1441 may commit as transaction T1449
before the checkpoint write fails. The retry should find O1441 already
applied and record a duplicate delivery without applying the balance
change again. The expected balance remains 320 units, not 340.
This example is required for the pending rollback drill because a
successful worker restart alone does not prove idempotence. Preserve
the operation, queue, transaction, and balance values as one example;
splitting them across summaries would lose their relationship.

### Checkpoint without visible acknowledgement

At queue offset Q1442, the destination commits transaction T1450 and
the checkpoint succeeds, but the acknowledgement is lost. The source
may redeliver the operation after the worker reconnects. The expected
balance is 350 units after the first application and remains 350
after redelivery. Do not interpret the missing acknowledgement as a
failed destination commit. The acceptance capture must retain both
delivery attempts and show that the checkpoint refers to T1450.
The regional drill has not yet exercised this failure sequence.

### Region failover during replay

If east fails after E1602 and west takes over before E1603, the shared
business identity must prevent reapplication of E1602. The destination
must end at watermark W1600 with checksum f60a for B16. A matching
checksum without the correct watermark is insufficient, because a
later replay could skip an uncommitted event. Preserve the intermediate
watermark W1598 as the takeover boundary. Both regional logs must
identify the same takeover boundary before the pending reviewer can
accept the failover scenario.

### Rollback threshold

Stop the drill if duplicate applied operations exceed 0, if missing
operations exceed 0, or if either region exceeds its matrix delay for
two consecutive capture windows. Each capture window lasts 60 seconds.
A single delayed window requires inspection, not automatic rollback.
The distinction prevents unnecessary restarts while still bounding
recovery time. These are active thresholds, not descriptions of a
completed incident. The handoff must preserve the zero-tolerance
operation checks separately from the two-window timing rule.

## Evidence Provenance and Open Risks

The local test runner produced the east example values above. They
are inspected local fixture results, not observations of production.
The west relay delay allowance was reported by the platform owner
and remains a reported constraint until the regional capture verifies
it. Do not promote that report into independently verified evidence.
The candidate is not deployed to production, and production safety
has not been demonstrated. No task may be checked merely because the
local test suite passed or because a draft PR exists.

The main open risk is a false match caused by collecting only part
of B17. A second risk is treating transport offsets as business order.
Both risks still affect acceptance and therefore remain explicit.
No risk in this section is resolved. If regional captures contradict
the expected matrix, preserve the contradiction and ask for a decision
rather than quietly replacing the expected checksum or narrowing the
acceptance criterion. The exact scope of an eventual audit sign-off
must be recorded before any evidence is considered disposable.

## Review Handoff

The next reviewer needs all fourteen matrix rows, the interpretation
notes, and the five rollback examples together. The handoff
must identify the missing west checksum and the unconfirmed final PR
readiness without making either look complete. There is no external
evidence attachment to link instead. Keep this evidence inline until
sign-off, even if the selected work exceeds the usual advisory size.
If a later durable report is approved, replacing material with its
reference will be a separate substantive decision, not an automatic
consequence of reaching a word count.
