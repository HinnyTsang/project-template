# Template project for pyspark

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