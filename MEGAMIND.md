# DeepResearchAgent as a Megamind Execution Body

DeepResearchAgent supplies hierarchical planning, browser research, tool calling, and bounded Python execution. It is mounted around Megamind specialists rather than becoming their identity.

## Agent mapping

- **Stealth Sherlock Alpha:** provenance, retrieval, contradiction testing, and evidence synthesis.
- **Core Think:** difficult decomposition and analytical planning.
- **Stealth Supernova:** broad system sweep and process recovery.
- **Stealth Microwave / Lil Omni:** bounded parallel subtasks.

## Static readiness

```bash
python scripts/megamind_healthcheck.py
```

The check verifies Python 3.11+, expected entry files, the environment template, and parseable top-level Python syntax. It deliberately does not read `.env`, install packages, launch Chromium, call an API, or run arbitrary tools.

## Controlled setup

```bash
make install-requirements
playwright install chromium --with-deps --no-shell
python scripts/megamind_healthcheck.py
```

Configure either scoped provider credentials or a controlled local vLLM endpoint using the repository documentation. Never commit credentials or private mission content.

## Controlled launch

```bash
python main.py
```

Start with a bounded smoke mission using public, non-sensitive information. Require explicit approval before enabling broad network access, local code execution, private repositories, or confidential evidence.

## Research receipt

A completed mission should preserve:

- exact repository revision and configuration profile;
- research question and decomposition;
- source URI and retrieval time for every material source;
- claims linked to supporting sources;
- conflicts, unknowns, and failed searches;
- generated artifacts and hashes;
- selected model route and tool inventory;
- exit status and human approvals.

## Truth boundary

A passing static check proves only that the Megamind adapter and expected repository structure are present. Runtime readiness requires dependency installation, browser setup, a valid model route, and a successful bounded research test.
