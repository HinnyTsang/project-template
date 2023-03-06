# Template project for pyspark

It is a recommended file structure for project including the following:
1. Airtable
2. Pyspark
3. Oracle SQL

```
├── .env.template
├── .gitignore
├── README.md
├── config
│   └── airtable.yaml
├── logs
│   └── README.md
├── poetry.lock
├── pyproject.toml
├── requirements.txt
├── scripts
│   └── pack-venv.sh
├── shell.nix
└── src
    ├── logger
    │   ├── __init__.py
    │   ├── config.yaml
    │   ├── formatter.py
    │   └── logger.py
    └── utils
        ├── __init__.py
        ├── airtable.py
        └── utils.py
```

## Non-nix user

Below are the options

### Using Poetry

```bash
poetry install
```

### Using other package managers venv
```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Nix

1. Update channel
    ```bash
    nix-channel --add https://nixos.org/channels/nixpkgs-22.11-darwin nixpkgs
    nix-channel --update
    ```

2. Activate nix shell
    ```bash
    nix-shell
    ```

3. Install packages with Poetry
    ```bash
    poetry install
    ```