import os
import json
from dotenv import dotenv_values


class Config:
    """
    A class representing the configuration settings.
    This class loads the configuration values from various sources, such as environment variables,
    local environment files, secrets files, and a configuration file.
    See the README.md file for more information on how to use this class.
    """

    def __init__(
        self,
        pwd: str = ".",
        defaults: str = "defaults.env",
        environ: str = "environ.env",
        secrets: str = "secrets.env",
    ):
        """
        Initialize the Config object.

        Args:
            pwd (str, optional): The working directory path. Defaults to ".".
            defaults (str, optional): The filename of the defaults file. Defaults to "defaults.env".
            environ (str, optional): The filename of the environment variables file. Defaults to "environ.env".
            secrets (str, optional): The filename of the secrets file. Defaults to "secrets.env".
        """
        defaults_path = f"{pwd}/{defaults}"
        environ_path = f"{pwd}/{environ}"
        secrets_path = f"{pwd}/{secrets}"
        self.defaults = dotenv_values(defaults_path)
        self.environ = dotenv_values(environ_path)
        self.secrets = dotenv_values(secrets_path)
        self.env_vars = dict(os.environ)
        self.reload()

    def reload(self):
        """
        Reloads the environment variables by updating the 'values' dictionary with the latest values.
        The 'values' dictionary is updated by merging the default values, environment variables,
        secrets, and additional environment variables.
        """
        self.values = {**self.defaults, **self.environ, **self.secrets, **self.env_vars}
    
    def __getattr__(self, name):
        """
        Retrieves the value of a configuration setting by its name.

        Args:
            name (str): The name of the configuration setting.

        Returns:
            The value of the configuration setting.

        Raises:
            AttributeError: If the configuration setting doesn't exist.
        """
        value = self.values.get(name)
        if value is None:
            raise AttributeError(f"Configuration setting '{name}' does not exist.")
        # If the value is a JSON, parse it
        if value and (value.startswith("[") or value.startswith("{")):
            return json.loads(value)
        return value
