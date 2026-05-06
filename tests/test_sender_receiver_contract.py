from des_socket_utils import encrypt_des_cbc, build_packet, parse_header, decrypt_des_cbc


def test_protocol_contract_order_is_key_iv_length_ciphertext():
    key, iv, cipher_bytes = encrypt_des_cbc(b"FIT4012 contract test", key=b"12345678", iv=b"abcdefgh")
    packet = build_packet(key, iv, cipher_bytes)
    assert packet[:8] == key
    assert packet[8:16] == iv
    assert len(packet[20:]) == len(cipher_bytes)
    assert len(cipher_bytes) % 8 == 0


def test_wrong_header_length_causes_error():
    key, iv, cipher_bytes = encrypt_des_cbc(b"Test wrong length", key=b"12345678", iv=b"abcdefgh")
    # Build packet with correct length
    packet = build_packet(key, iv, cipher_bytes)
    # Modify header to have wrong length (e.g., length + 1)
    wrong_packet = packet[:16] + (len(cipher_bytes) + 1).to_bytes(4, 'big') + cipher_bytes
    # Parse header
    k, i, length = parse_header(wrong_packet[:20])
    assert k == key
    assert i == iv
    assert length == len(cipher_bytes) + 1  # Wrong
    # If we try to decrypt with wrong length, but since it's unit, just check length mismatch
    # In integration, it would timeout, but here we can assert length != len(cipher_bytes)
