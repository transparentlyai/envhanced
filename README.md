# Envhanced

Envhanced a simple, yet effective and intuitive, configuration management library designed to facilitate the seamless integration of configuration files and environment variables into your Python applications. It enables easy access to configurations across different environments, handling secrets, and default configurations with ease.

## Example Usage

To use Envhanced, simply import the `Config` class and access your configuration as object attributes:

```python
from envhanced import Config
cfg = Config()

# Accessing configurations:
server_ip = cfg.IP_ADDRESS  # Loaded from environment variable
app_name = cfg.APP_NAME    # Default value from defaults.env file
db_host = cfg.DB_HOST      # Loaded from environ.env file
api_key = cfg.API_KEY      # Loaded from secrets.env file
user = cfg.USER            # Loaded from secrets.env file
password = cfg.PASSWORD    # Loaded from secrets.env file
```

Upon initialization, all the configuration values become readily accessible as attributes of the `Config` object.

## Environment File Loading Priorities

Envhanced prioritizes configuration sources to ensure that the most critical and environment-specific settings take precedence:

1. **Environment Variables:** Highest priority. These override all other settings.
2. **secrets.env:** Contains sensitive information. Overrides `environ.env` and `defaults.env` but is overridden by environment variables. Should not be tracked in source control (add to `.gitignore`).
3. **environ.env:** Holds environment-specific settings, overriding `defaults.env` but is overridden by `secrets.env` and environment variables. Accepts JSON values as strings and can be under source control.
4. **defaults.env:** Contains default settings, overridden by all other sources. Accepts JSON values as strings and should be tracked in source control.

## Notes and Best Practices

- **Initialization Parameters:** All are optional with default values (`pwd="."`, `environ="environ.env"`, `secrets="secrets.env"`, `defaults="defaults.env"`). You can omit any file if not needed.
- **Accessing Values:** Configuration values are accessed as attributes (e.g., `cfg.DB_HOST`).
- **Custom Configuration Paths:** Initialize `Config` with a different directory path to load files from another location, useful for managing configurations across environments (development, testing, production).
- **Multiline JSON Strings:** Supported for complex configurations. Ensure valid JSON formatting.
- **Boolean Conversion:** Strings `true` and `false` are converted to `True` and `False` respectively.
- **Centralized Configuration:** It's advisable to instantiate the `Config` object once and import it across your application for consistency and ease of management.
- **ADD sectrets to gitignore** 

### Example: Centralized Configuration

Create a `config.py` file for a centralized configuration object:

```python
from envhanced import Config

cfg = Config()
```
#### If you have multiple configuration environments you could configure as follows:
```python
import os
from envhanced import Config

#ENV is an environement variable containing the name of the config
ENV = os.environ["ENV"]
cfg = Config(
    defaults="config/defaults.env",
    environ=f"config/{ENV}-env/environ.env",
    secrets=f"config/{ENV}-env/secrets.env",
)
```

Then, in your application files, import and use the centralized configuration:

```python
from config import cfg

server_ip = cfg.IP_ADDRESS  # Loaded from environment variable
app_name = cfg.APP_NAME    # Default value from defaults.env file
# ... and so on
```

This approach simplifies configuration management across your application, ensuring consistency and ease of updates.

## Install 
`pip install envhanced@git+https://github.com/transparentlyai/envhanced.git`
