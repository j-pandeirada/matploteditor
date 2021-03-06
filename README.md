# MatPlotEditor

The GUI plot editor we all deserved for Matplotlib.

## How to use the Repo

Please install all the requirements with your preferred python virtual environment with the following bash command:

```console
python3 -m venv venv
echo "export PYTHONPATH="${PYTHONPATH}:$PWD/src/"" >> ./venv/bin/activate
source venv/bin/activate
python3 -m pip install -r requirements.txt
```

Note: Depending on your environment you may need to update your 'setuptools' to install dependencies: 'python3 -m pip install -U setuptools'.

Run formatter with the following command:

```console
make format
```

Run lint with the following command:

```console
make lint
```

