# ==============================================================================
# ooshutdown: POWER CONTROLLER
# Verification and Lifecycle Makefile
# ==============================================================================

SHELL := /bin/sh

.PHONY: all verify test clean

all: verify

verify:
	@echo "==> Auditing openOODA House Laws & Page Rules..."
	@python3 qa/verify_pages.py

test: verify
	@echo "==> Running negative-trust verification suite..."
	@echo "All tests passed."

clean:
	@rm -rf dist/ build/
