import pytest
from authenticator import Authenticator

@pytest.fixture
def authenticator():
    auth = Authenticator()
    yield auth


# ユーザー登録のテスト
@pytest.mark.parametrize("username, password", [
    ("user1", "pass1"),
    ("user2", "pass2"),
    ("user3", "pass3")
])
def test_register_success(authenticator, username, password):
    authenticator.register(username, password)
    assert username in authenticator.users
    assert authenticator.users[username] == password

# ユーザー登録のエラーテスト
def test_register_error(authenticator):
    authenticator.register('username1', 'password1')
    with pytest.raises(ValueError, match="エラー: ユーザーは既に存在します。"):
        authenticator.register('username1', 'password1')

# ログインのテスト
@pytest.mark.parametrize("username, password", [
    ("user1", "pass1"),
    ("user2", "pass2"),
    ("user3", "pass3")
])
def test_login_success(authenticator, username, password):
    authenticator.register(username, password)
    result = authenticator.login(username, password)
    assert result == "ログイン成功"

# ログインのエラーテスト
def test_login_error(authenticator):
    authenticator.register('username1', 'password1')
    with pytest.raises(ValueError, match="エラー: ユーザー名またはパスワードが正しくありません。"):
        authenticator.login('username1', 'password0')