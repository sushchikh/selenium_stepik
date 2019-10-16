def test_substring(full_string, substring):
    # ваша ре  ализация, напишите assert и сообщение об ошибке
    assert substring in full_string, f"expected '{substring}' to be substring of '{full_string}'"

test_substring('abcdef', 'abcc')