from challenges.challenge_encrypt_message import encrypt_message
import pytest


def test_encrypt_message():
    # Testando se ao passar o numero par ele inverte a string
    key = 2
    message = 'Mundo'
    encrypt = encrypt_message(message, key)
    assert encrypt == 'odn_uM'

    # Testando se ao passar o numero ímpar ele inverte a string
    message = 'Paralelepípedo'
    key = 3
    encrypt = encrypt_message(message, key)
    assert encrypt == 'raP_odepípelela'

    # Testar se passar uma key muito grande ele inverte a menssage
    message = 'vamo'
    key = 5
    encrypt = encrypt_message(message, key)
    assert encrypt == 'omav'

    # Testando se passar uma str no parametro da key retorna o erro
    message = 'Ola'
    key = 'a'
    with pytest.raises(TypeError, match="tipo inválido para key"):
        encrypt_message(message, key)
    # Testando se na messagem não foi passado uma string
    message = 3
    key = 2
    with pytest.raises(TypeError, match="tipo inválido para message"):
        encrypt_message(message, key)

    # Testando se passar string vazia returna vazia

    message = ''
    key = 5
    encrypt = encrypt_message(message, key)
    assert encrypt == ""
