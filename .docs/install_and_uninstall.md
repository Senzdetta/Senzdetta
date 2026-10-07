# INSTALL AND UNINSTALL

## Installation
`install.sh` optional options (can be used together):
- `--home=<path>`
- └── override `$HOME` value.
- `--backup`
- └── create a backup of the existing senzdetta installation before replacing it.

### Usage
```bash
git clone https://github.com/Senzdetta/Senzdetta
bash Senzdetta/install.sh <option>
```

## Uninstallation
`uninstall.sh` optional options (can be used together):
- `--home=<path>`
- └── override `$HOME` value.
- `--remove-backup`
- └── remove all backup found.

### Usage
```bash
export prefix="${PREFIX:-/usr}"
bash $prefix/opt/senzdetta/uninstall.sh <option>
```