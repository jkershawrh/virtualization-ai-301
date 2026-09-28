# Immutable release receipt

Successful workflow run
[`36497374230`](https://github.com/jkershawrh/virtualization-ai-301/actions/runs/36497374230)
built exact source revision `91e30a4af72bb4a15a4e5dfe2f29abb5692c698f`
for Linux/AMD64.

| Component | Exact image | Critical | High | Medium |
|---|---|---:|---:|---:|
| Presentation | `ghcr.io/jkershawrh/virtualization-ai-301-presentation@sha256:012c22404725b03c5c5b3d8bb3234e608da334af72762e10e158031b505506fa` | 0 | 0 | 4 |
| Adapter | `ghcr.io/jkershawrh/virtualization-ai-301-adapter@sha256:6da66231992bd9db8a31cdc08b3912b7d6c797e1ed42a064c06eea686d579d07` | 0 | 0 | 6 |

For both images the workflow generated an SPDX JSON SBOM, used GitHub OIDC for
a keyless signature, attached and verified SPDX plus SLSA provenance
attestations, removed the tag, pulled the exact digest, verified AMD64, and
verified the embedded source-revision label.

The earlier run `36497276278` was an invalid-workflow parse check and produced
no image or supply-chain artifact. It is not release evidence.

This receipt is committed after the source build. The release workflow is
manual, so adding the receipt does not rebuild or relabel the published images.
Supply-chain success is not OpenShift runtime proof or Launchpad certification.
