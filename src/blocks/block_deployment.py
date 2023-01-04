"""Deployments for Custom Prefect Blocks"""
import logging

from src.blocks.sentry_block import SentryBlock, SENTRY_BLOCK_NAME

logging.getLogger().setLevel(logging.INFO)

base_flow_block = SentryBlock()

base_block_document_id = base_flow_block.save(SENTRY_BLOCK_NAME, overwrite=True)
logging.info(f"Successfully deployed sentry block with document id '{base_block_document_id}'.")
