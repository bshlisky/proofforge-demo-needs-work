# ProofForge Demonstration Fixture: Needs Work

This repository is a demonstration fixture designed specifically to exercise **ProofForge Stage 0** readiness assessment and validate that the scoring engine accurately identifies manageable engineering gaps and produces appropriate **Readiness Conditions**.

## Intentional Rubric Gaps
- **Missing Lockfile**: Uses a loose `requirements.txt` with unpinned ranges rather than a locked dependency manifest, triggering `"Add lockfiles for full reproducibility"`.
- **Incomplete Build Definition**: Relies solely on runtime package installation without a formalized build automation file (`Makefile`, `Dockerfile`), reducing build reproducibility score.
- **Omitted CI/CD Configuration**: Lacks `.github/workflows/` metadata, triggering `"Provide CI/CD metadata if applicable"`.
- **External Dependency**: Includes a `docker-compose.yml` declaring an external PostgreSQL dependency, triggering `"Document external dependency governance"`.

## Functionality
A basic FastAPI telemetry ingestion endpoint with unit tests.

*Demonstration Data Notice: Created solely for ProofForge Stage 0 validation.*
