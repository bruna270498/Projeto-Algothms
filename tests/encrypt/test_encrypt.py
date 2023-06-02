from challenges.challenge_encrypt_message import encrypt_message


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

    # Testando se passar uma str no parametro da key retorna o erro
    message = 'Ola'
    key = 'a'
    try:
        encrypt_message(message, key)
    except TypeError as error:
        assert str(error) == "tipo inválido para key"
    else:
        assert False
