# Cognitive Pairing Skills — Makefile
#
# Self-documenting Makefile for deploying skills to user directories.
# Run `make` or `make help` to see available targets.

.DEFAULT_GOAL := help
.PHONY: help deploy deploy-copilot deploy-codex sync sync-copilot sync-codex clean-deprecated

# ==============================================================================
# Configuration
# ==============================================================================

SKILLS_DIR := skills
COPILOT_DEST := $(HOME)/.copilot/skills
CODEX_DEST := $(HOME)/.codex/skills

# Skills to deploy (all skill directories except _template)
SKILLS := $(filter-out _template,$(notdir $(wildcard $(SKILLS_DIR)/cp-*)))

# Deprecated skills to remove on sync (add skill names here when deprecating)
DEPRECATED :=

# ==============================================================================
# Help
# ==============================================================================

help: ## Show this help message
	@echo ""
	@echo "Cognitive Pairing Skills — Deployment"
	@echo "======================================"
	@echo ""
	@echo "Skills to deploy: $(SKILLS)"
	@echo ""
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | \
		awk 'BEGIN {FS = ":.*?## "}; {printf "  \033[36m%-20s\033[0m %s\n", $$1, $$2}'
	@echo ""
	@if [ -n "$(DEPRECATED)" ]; then \
		echo "Deprecated (will be removed on sync): $(DEPRECATED)"; \
		echo ""; \
	fi

# ==============================================================================
# Deploy targets
# ==============================================================================

deploy: deploy-copilot deploy-codex ## Deploy skills to both Copilot and Codex

deploy-copilot: ## Deploy skills to ~/.copilot/skills/
	@echo "Deploying skills to $(COPILOT_DEST)..."
	@mkdir -p $(COPILOT_DEST)
	@for skill in $(SKILLS); do \
		echo "  → $$skill"; \
		mkdir -p $(COPILOT_DEST)/$$skill; \
		cp -r $(SKILLS_DIR)/$$skill/* $(COPILOT_DEST)/$$skill/; \
	done
	@echo "✓ Deployed $(words $(SKILLS)) skills to Copilot"

deploy-codex: ## Deploy skills to ~/.codex/skills/
	@echo "Deploying skills to $(CODEX_DEST)..."
	@mkdir -p $(CODEX_DEST)
	@for skill in $(SKILLS); do \
		echo "  → $$skill"; \
		mkdir -p $(CODEX_DEST)/$$skill; \
		cp -r $(SKILLS_DIR)/$$skill/* $(CODEX_DEST)/$$skill/; \
	done
	@echo "✓ Deployed $(words $(SKILLS)) skills to Codex"

# ==============================================================================
# Sync targets (deploy + clean deprecated)
# ==============================================================================

sync: sync-copilot sync-codex ## Sync skills to both Copilot and Codex

sync-copilot: deploy-copilot clean-deprecated-copilot ## Sync skills to Copilot (deploy + remove deprecated)

sync-codex: deploy-codex clean-deprecated-codex ## Sync skills to Codex (deploy + remove deprecated)

# ==============================================================================
# Clean deprecated
# ==============================================================================

clean-deprecated: clean-deprecated-copilot clean-deprecated-codex ## Remove deprecated skills from both destinations

clean-deprecated-copilot: ## Remove deprecated skills from ~/.copilot/skills/
	@if [ -n "$(DEPRECATED)" ]; then \
		echo "Removing deprecated skills from $(COPILOT_DEST)..."; \
		for skill in $(DEPRECATED); do \
			if [ -d "$(COPILOT_DEST)/$$skill" ]; then \
				echo "  ✗ $$skill"; \
				rm -rf $(COPILOT_DEST)/$$skill; \
			fi; \
		done; \
		echo "✓ Cleaned deprecated skills from Copilot"; \
	else \
		echo "No deprecated skills to remove from Copilot"; \
	fi

clean-deprecated-codex: ## Remove deprecated skills from ~/.codex/skills/
	@if [ -n "$(DEPRECATED)" ]; then \
		echo "Removing deprecated skills from $(CODEX_DEST)..."; \
		for skill in $(DEPRECATED); do \
			if [ -d "$(CODEX_DEST)/$$skill" ]; then \
				echo "  ✗ $$skill"; \
				rm -rf $(CODEX_DEST)/$$skill; \
			fi; \
		done; \
		echo "✓ Cleaned deprecated skills from Codex"; \
	else \
		echo "No deprecated skills to remove from Codex"; \
	fi

# ==============================================================================
# Utility targets
# ==============================================================================

list: ## List all skills that will be deployed
	@echo "Skills to deploy:"
	@for skill in $(SKILLS); do \
		echo "  - $$skill"; \
	done

verify: ## Verify all skills have valid SKILL.md files
	@echo "Verifying skills..."
	@errors=0; \
	for skill in $(SKILLS); do \
		if [ ! -f "$(SKILLS_DIR)/$$skill/SKILL.md" ]; then \
			echo "  ✗ $$skill: missing SKILL.md"; \
			errors=$$((errors + 1)); \
		elif ! grep -q "^name:" "$(SKILLS_DIR)/$$skill/SKILL.md"; then \
			echo "  ✗ $$skill: missing 'name' in frontmatter"; \
			errors=$$((errors + 1)); \
		elif ! grep -q "^description:" "$(SKILLS_DIR)/$$skill/SKILL.md"; then \
			echo "  ✗ $$skill: missing 'description' in frontmatter"; \
			errors=$$((errors + 1)); \
		else \
			echo "  ✓ $$skill"; \
		fi; \
	done; \
	if [ $$errors -gt 0 ]; then \
		echo ""; \
		echo "$$errors error(s) found"; \
		exit 1; \
	fi; \
	echo ""; \
	echo "✓ All $(words $(SKILLS)) skills verified"
