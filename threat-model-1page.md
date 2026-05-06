# Threat Model - Lab 3

## Thông tin nhóm
- Thành viên 1: Student 1
- Thành viên 2: Student 2

## Assets
- Plaintext message: The original message that needs to be kept confidential.

## Attacker model
- An attacker who can intercept network traffic between Sender and Receiver.
- Can modify packets in transit.
- Has access to the source code and knows the protocol.

## Threats
1. Eavesdropping: Attacker captures the DES key and IV sent in plaintext, then decrypts the ciphertext.
2. Tampering: Attacker modifies the ciphertext, causing wrong decryption or padding errors.
3. Replay: Attacker resends old packets.
4. Wrong key: If attacker provides wrong key, decryption fails.

## Mitigations
1. Use secure key exchange (e.g., Diffie-Hellman) instead of sending key in plaintext.
2. Add message authentication code (MAC) or digital signatures to ensure integrity.
3. Use sequence numbers or timestamps to prevent replay.
4. Implement proper error handling and logging for detection.

## Residual risks
- If the system is deployed as is, the key is sent in plaintext, making it vulnerable to eavesdropping.
- No authentication of sender, so anyone can send messages.
- DES is outdated; better to use AES.
