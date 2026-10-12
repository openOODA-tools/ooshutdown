# ooshutdown: House Laws & Agent Engineering Standards (v1)

This document is the **single canonical source of truth** for all code, architecture, and system integration standards across `ooshutdown`. Every human contributor and AI agent must strictly follow these rules without exception.

---

## 1. The Page Rule (Code Layout & Sizing)

A **page** is one committed `.oo` or `.oot` file. Every page holds one idea, fits in one head, and carries its own weight. This rule is enforced by automated verification under `make verify`: red pages fail the build.

### Hard Sizing Invariants
- **16–256 Lines**: Every committed source file must be between **16 and 256 lines**, counted as exact line breaks (blank lines and comments count).
- **Shim Exemption (Floor Only)**: A file is a shim when every non-comment line is an import or re-export (`import "..."`). Shims skip the 16-line floor. The **256-line ceiling still strictly applies**.
- **Directory Density (<= 8 files)**: At most **8 `.oo` files per directory**, tests included. Crowded directories must split into functional subdirectories grouped by domain.
- **Banned File Names (Name the function, not the drawer)**:
  `util.oo`, `utils.oo`, `helper.oo`, `helpers.oo`, `common.oo`, `misc.oo`, `shared.oo`, `base.oo`, `core.oo`.

### Splitting, Folding, and Naming
- **Over 256 lines**: Split along functional boundaries into a new subdirectory with an `anchor.oo` shim. One page = one verb or one wholly owned noun.
- **Under 16 lines (and not a shim)**: Fold into its closest sibling or caller. Never pad lines with artificial whitespace or comments to reach 16.

---

## 2. The 4-Element Academy Header (Mandatory on Every Page)

Every committed `.oo` file must begin with the standard 4-element Academy docstring within its first 7 lines:

```oo
// # Component Name - Subtitle
//
// Logline: Single-sentence imperative summary of functional responsibility.
//
// Setup: Preconditions, wired capability tokens, imported contracts.
//
// Beats:
//   1. First sequential phase of execution.
//   2. Next phase.
//   3. Final phase / exit state.
```

- **ASD-STE100 Compliance**: Clear, concise English. No filler or ambiguous verbs.
- **Imports**: All imports must be relative string literals. Never use `::` namespaces.

---

## 3. Capability Security & Negative-Trust Discipline

`ooshutdown` operates under the Object-Capability (OCap) security model in the **System & Monitor** functional domain:

### Capability Contracts
- **Explicit Tokens**: Demands explicit `&ProcCap, &SysInfoCap, &McpCap` tokens. Zero ambient authority.
- **Negative-Trust Boundaries**: Inputs, paths, and operational parameters are validated before admittance.
- **Subprocess Safety**: Never invoke unverified host shells. Syscall boundaries are strictly capability-gated.

---

## 4. Model Context Protocol (MCP) Surface

When invoked with `--mcp`, `ooshutdown` runs a JSON-RPC 2.0 stdio server implementing native tools for AI coding agents:
- `ooshutdown_exec`: Executes primary bounded capability under negative-trust constraints.
- `ooshutdown_inspect`: Inspects state, schema, or metadata without ambient leakage.

---

## 5. Verification Commands

Before committing, run:
```bash
make verify    # Runs Page Rule, Academy header, and line-limit audits
make test      # Executes hermetic unit & negative-trust integration tests
```

---

## 7. Multi-Engine Audit Protocol (Pre-Release)

Advisory tiered audit run before tagging releases, budgeted by token capacity:
1. **`mcode`** (Abundant tokens): Full codebase scan for contract mismatches, packaging specs, and CI gates.  
   `mcode exec --permission full "<prompt>"`
2. **`vibe`** (Moderate tokens): Adversarial diff inspection for subtle regressions, security bypasses, and API validity.  
   `vibe -p "<prompt>" --trust --auto-approve`
3. **`grok`** (Strict quota): High-value referee and final sanity check on critical release diffs.  
   `grok -p "<prompt>" --always-approve`

**Rule:** External audits are strictly advisory; all findings must be verified against source code. External LLMs never gate CI—the §5 Verification Ladder is the sole canonical authority.
