def test_hash_validator_accepts_valid_sha1():
    from witness.cloud.w11_hash_validator import is_valid_sha1
    assert is_valid_sha1("5f2d17a9c7d5d4e8a6b7c9d2a8d7f6c1e2a3b4c")


def test_hash_validator_rejects_fake_hash():
    from witness.cloud.w11_hash_validator import is_valid_sha1
    assert not is_valid_sha1("a1b2c3d")
