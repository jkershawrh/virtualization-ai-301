# Virtualization + AI 301

**Earned outcome:** Modernize VMs with Governed AI.

This Red Hat × Intel level-301 candidate extends the immutable Virtualization +
AI 201 contract. Learners qualify workload identity, the allowed network path,
declared-versus-observed placement, correlated evidence, failure/refusal
behavior, and human authority together.

The adapter returns `ALLOW_REVIEW`, `REFUSE`, or `ABSTAIN`; only a named human
reviewer may accept evidence and authorize later action. The model cannot
deploy, migrate, promote, certify, or mutate a VM or cluster.

## Evidence boundary

- Factory results are deterministic `REHEARSAL`, not live VM, networking,
  placement, Intel hardware, or inference claims.
- Read-only inventory observed OpenShift 4.18.16, Kubernetes 1.31.8, KubeVirt
  APIs, and a Linux/AMD64 server on 2026-09-28. No 301 workload was deployed;
  node/vendor visibility was not established.
- `LIVE` requires a current-session record with every runtime observation
  required by the contract.
- Performance, capacity, cost, migration-success, and certification claims are
  excluded.

## Candidate contents

- a seven-scene, 5–7 minute Triforce presentation;
- a separate 90–120 minute Showroom construction lab;
- JSON Schema and OpenAPI governance contracts;
- deterministic allow, refusal, abstention, and model-unavailable paths;
- Helm resources for identity, Service, NetworkPolicy, placement intent,
  observability, and Secret references;
- factory, visual, chart, packaging, supply-chain, and zero-residue gates; and
- a noncertifying Launchpad handoff proposal.

## Verify locally

```sh
npm ci
python3 -m pip install -r requirements-test.txt
npm run check
npm run test:visual
```

Run the adapter with `ADAPTER_MODE=rehearsal python3 -m workload.app`, then the
presentation with `npm run dev -- --host 127.0.0.1 --port 4179`.

## Source lineage

- canonical prerequisite: `virtualization-ai-201@70a35189cce95b87240734ec7961a67685d4cb27`;
- 101 boundary: `virtualization-ai-foundations@d84eabdd709f573caaf781763b361018e9ec04a6`;
- supplemental discovery only: `ocp-virt-roadshow-2026-showroom@5d296c9c9fbe773af09c16935c78b89baebd1f81`.

Only focused roadshow concepts were used: VM scheduling controls, pod-network
masquerade, Service/label discovery, NetworkPolicy, VM utilization/events, and
guest-agent visibility. The roadshow was not copied.

Passing factory checks or publishing signed images is not Launchpad
certification. Launchpad must independently validate cluster, model service,
identity, placement labels, network enforcement, resource use,
restart/resume/reclaim behavior, and human approval.
