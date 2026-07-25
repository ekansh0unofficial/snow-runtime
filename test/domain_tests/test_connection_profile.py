import pytest
import uuid

from snow_runtime.domain.entities import ConnectionProfile
from snow_runtime.domain.exceptions import ConfigurationError

def test_valid_profile_is_created():
    profile = ConnectionProfile(
        name="my_profile",
        organization="myorg",
        account="myaccount",
        username="myuser",
    )
    assert profile.name == "my_profile"
    assert profile.account == "myaccount"

def test_blank_account_raises_configuration_error():
      with pytest.raises(ConfigurationError):
        ConnectionProfile(
            name="my_profile",
            organization="myorg",
            account="",
            username="myuser",
        )

def test_whitespace_account_raise_configuration_error():
    with pytest.raises(ConfigurationError):
        ConnectionProfile(
            name="my_profile",
            organization="myorg",
            account = "   ",
            username= "myuser",
        )        

def test_trailing_whitespace_account_name_strip():
    profile = ConnectionProfile(
                name="my_profile",
                organization="myorg",
                account = "my_account   ",
                username= "myuser",
    )
    assert profile.account == "my_account"

def test_blank_username_raises_configuration_error():
      with pytest.raises(ConfigurationError):
        ConnectionProfile(
            name="my_profile",
            organization="myorg",
            account="my_account",
            username="",
        )

def test_whitespace_username_raise_configuration_error():
    with pytest.raises(ConfigurationError):
        ConnectionProfile(
            name="my_profile",
            organization="myorg",
            account = "my_account",
            username= "   ",
        )        

def test_trailing_whitespace_username_strip():
    profile= ConnectionProfile(
                name="my_profile",
                organization="myorg",
                account = "my_account",
                username= "my_user   ",
            )
    assert profile.username == "my_user"

def test_blank_name_raises_configuration_error():
      with pytest.raises(ConfigurationError):
        ConnectionProfile(
            name="",
            organization="myorg",
            account="my_account",
            username="my_user",
        )

def test_whitespace_name_raise_configuration_error():
    with pytest.raises(ConfigurationError):
        ConnectionProfile(
            name="   ",
            organization="myorg",
            account = "my_account",
            username= "my_user",
        )        

def test_trailing_whitespace_name_strip():
    profile= ConnectionProfile(
                name="my_profile   ",
                organization="myorg",
                account = "my_account",
                username= "my_user",
            )
    assert profile.name == "my_profile"    

