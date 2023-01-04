"""Sample Prefect2 showcasing Sentry Block capabilities"""
from prefect import flow, task, get_run_logger

from src.blocks.sentry_block import SentryBlock, SENTRY_BLOCK_NAME


@task(name="Failure")
def task_always_failing():
    logger = get_run_logger()
    logger.info("The task will fail soon! 🙈")

    raise Exception("Oh no!")


@flow(timeout_seconds=60)
def sample_flow():
    base_block: SentryBlock = SentryBlock.load(SENTRY_BLOCK_NAME)
    base_block.initialize_sentry_block()
    task_always_failing()


if __name__ == "__main__":
    sample_flow()