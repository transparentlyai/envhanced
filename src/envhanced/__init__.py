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
        cwd: str = ".",
        defaults: str = "",
        environ: str = "",
        secrets: str = "",
        additional: dict = {},
    ):
        """
        Initialize the Config object.

        Args:
            pwd (str, optional): The working directory path. Defaults to ".".
            defaults (str, optional): The filename of the defaults file. Defaults to "defaults.env".
            environ (str, optional): The filename of the environment variables file. Defaults to "environ.env".
            secrets (str, optional): The filename of the secrets file. Defaults to "secrets.env".
        """
        self.additional = additional
        self.defaults_path = defaults or f"{cwd}/defaults.env"
        self.environ_path = environ or f"{cwd}/environ.env"
        self.secrets_path = secrets or f"{cwd}/secrets.env"
        self.secrets_path = secrets or f"{cwd}.secrets.env"
        self.reload()

    def reload(self):
        """
        Reloads the environment variables by updating the 'values' dictionary with the latest values.
        The 'values' dictionary is updated by merging the default values, environment variables,
        secrets, and additional environment variables.
        """
        self.defaults = dotenv_values(self.defaults_path)
        self.environ = dotenv_values(self.environ_path)
        self.secrets = dotenv_values(self.secrets_path)
        self.env_vars = dict(os.environ)
        self.values = {**self.defaults, **self.environ, **self.secrets, **self.env_vars, **self.additional}

        # Set the configuration settings as attributes for language server
        # autocompletion instedd of retriving at __getattr__
        for key, value in self.values.items():
            # If the value is a JSON, parse it
            if value and (value.startswith("[") or value.startswith("{")):
                value = json.loads(value)
            # If the value is a boolean, parse it
            if value == "true" or value == "True":
                value = True
            if value == "false" or value == "False":
                value = False
            # If the value is a string, parse it to a number if possible
            if type(value) == str:
                value = convert_string_to_num(value)
            setattr(self, key, value)


def convert_string_to_num(value: str):
    """
    Converts a string to a numeric value.

    If the string can be converted to an integer, the integer value is returned.
    If the string can be converted to a float, the float value is returned.
    If the string cannot be converted to a numeric value, the original string is returned.

    Args:
        value (str): The string to be converted.

    Returns:
        int or float or str: The converted numeric value or the original string.
    """
    try:
        return int(value)
    except ValueError:
        pass
    
    # Try to convert to float
    try:
        return float(value)
    except ValueError:
        pass
    
    return value