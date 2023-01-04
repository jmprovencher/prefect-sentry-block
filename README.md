# prefect-sentry-block
Sample code on how to create a Sentry integrated block with Prefect

## Getting started

This project is using Python runtime version 3.9.0. If this runtime is not currently installed on your computer, it's recommended to use [pyenv](https://github.com/pyenv/pyenv) to manage your Python installations. It is also recommended to use a virtual environment like [venv](https://docs.python.org/3/library/venv.html) to manage your Python environment.

To install python dependencies run the following command:

```bash
pip install -r requirements.txt
```

This project is using ``python-dotenv`` to manage environment variables. Copy and paste the [.env-example](./env-example) file, rename it to .env and make sure to replace it with the appropriate environment variables values.

Also, make sure you are properly authenticated with the Prefect CLI using the documentation available [here](https://docs.prefect.io/ui/cloud-getting-started/?h=login#create-an-api-key).

## Creating block

To create the Sentry block, run the following command.

```bash
python -m src.blocks.block_deployment
```

## Run the flow to test the Sentry Block

```bash
python -m src.flows.sample_flow
```

