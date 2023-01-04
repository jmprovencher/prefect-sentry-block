"""Block that initializes Sentry."""
import os
import git

from textwrap import dedent

from prefect import get_run_logger
from prefect.context import get_run_context
from prefect.blocks.core import Block
from sentry_sdk import init, set_context, set_tag
from dotenv import load_dotenv

SENTRY_BLOCK_NAME = "sentry-block"


def _get_git_changeset():
    repo = git.Repo(search_parent_directories=True)
    return repo.head.object.hexsha


class SentryBlock(Block):
    """Block that bootstraps Sentry with metadata related to Prefect flow runs."""

    _code_example = dedent(
        """\
        ```python
        from src.blocks.sentry_block import SentryBlock, SENTRY_BLOCK_NAME

        sentry_block: SentryBlock = SentryBlock.load(SENTRY_BLOCK_NAME)
        sentry_block.initialize_sentry_block()
        ```"""
    )

    def initialize_sentry_block(self):
        """Initialize the sentry block."""
        logger = get_run_logger()
        load_dotenv()

        try:
            logger.info(f"Initializing Sentry...")
            sentry_dsn = os.getenv("SENTRY_DSN")
            environment = os.getenv("ENVIRONMENT")
            region = os.getenv("REGION")

            init(
                sentry_dsn, environment=environment, release=_get_git_changeset()
            )

            set_tag("region", region)

            run_context = get_run_context()

            set_tag("flow_name", run_context.flow.name)
            set_tag("flow_run_name", run_context.flow_run.name)
            set_tag("flow_run_version", run_context.flow_run.flow_version)
            set_context("flow_parameters", run_context.flow_run.parameters)

            logger.info("Sentry was successfully initialized.")

        except Exception as exception:
            logger.error("Failed to initialized Sentry. Inner exception: %s", exception)
