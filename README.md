
# Envhanced

Load configuration files and enviroment variables for easy access in different environments,
secrets and default configs.

Example usage

```python 
from envhanced import Config

cfg = Config()

app_name = cfg.APP_NAME # from defaults.env file
db_host = cfg.DB_HOST # default value from the environ.env file
api_key = cfg.API_KEY # from the secrets.env file
user = cfg.USER # from the secrets.env file
password = cfg.PASSWORD # from the secrets.env file
```

Once inititaslized all the config values are available as attributes of the Config object.
## Environment File Loading Priorities

The files are loaded in a specific order of priority, ensuring that the most critical
and environment-specific settings are applied correctly.

Priority Order:

1. Environment Variables:
   - Highest priority.
   - Overrides all settings in all environment files.

2. secrets.env:
    - Second-highest priority.
    - Contains sensitive information and secrets.
    - Overrides settings in `environ.env` and `defaults.env`.
    - Overridden by environment variables.
    - Should NOT be under source control. (!! Add to .gitignore !!)

3. environ.env:
    - Third level of priority.
    - Typically holds environment-specific settings (useful for development/testing envs).
    - Overrides settings in `config.env`.
    - Overridden by `secrets.env` and environment variables.
    - Acceps json values as strings.
    - It can be under source control.

4. defaults.env:
    - Lowest priority.
    - Contains default settings.
    - Overridden by `local.env`, `secrets.env`, and environment variables.
    - Accepts json values as strings.
    - Should be in source control.

## NOTES
- All initial parameters are optional and have default values of `pwd="."`, `environ="environ.env"`, `secrets="secrets.env"`, and `defaults="defaults.env"`.
- Any file can be omitted if it's not needed. For example, if you don't have any secrets, you can omit `secrets.env` file.
- All values can be accessed as attributes of the Config instance. i.e. `cfg.DB_HOST`, `cfg.API_KEY`, etc.
- The Config object can be initialized with a different directory path to load the environment files from a different location. i.e. `cfg = Config(pwd="/path/to/env/files")`.
    You may want to do this if you have a different directories containing separate configurations for each environment (e.g. dev, test, prod).
- Alternatively, you can specify the path for each environment file individually (the path is relative to pwd). 
    i.e. `cfg = Config(defaults="new.defaults.env", environ="DEVDIR/dev.env", secrets="secrets.env")`
    in this case, the `environ.env` file will be loaded from the `DEVDIR` directory and the rest from the current directory and defaults has a different name. 
    Note that the path is relative to the `pwd` parameter so do not start with a `/` or `./` or `../`.



