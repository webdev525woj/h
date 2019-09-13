# -*- coding: utf-8 -*-

from __future__ import unicode_literals
import pytest

from h.config import configure


@pytest.mark.parametrize(
    "env_var,env_val,setting_name,setting_val",
    [
        ("SECRET_KEY", "dont_tell_anyone", "secret_key", b"dont_tell_anyone"),
        ("SECRET_SALT", "best_with_pepper", "secret_salt", b"best_with_pepper"),
        # There are many other settings that can be updated from env vars.
        # These are not currently tested.
    ],
)
def test_configure_updates_settings_from_env_vars(
    env_var, env_val, setting_name, setting_val
):
    environ = {env_var: env_val} if env_var else {}
    settings_from_conf = {
        # Required settings
        "es.url": "https://es6-search-cluster",
        "secret_key": "notasecret",
        "sqlalchemy.url": "postgres://user@dbhost/dbname",
    }

    config = configure(environ=environ, settings=settings_from_conf)

    assert config.registry.settings[setting_name] == setting_val
