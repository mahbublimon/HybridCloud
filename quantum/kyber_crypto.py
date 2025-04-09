from pqcrypto.kem.kyber512 import generate_keypair, encrypt, decrypt

def run_kyber():
    print("[Kyber] Generating key pair...")
    public_key, private_key = generate_keypair()
    ciphertext, shared_secret = encrypt(public_key)
    decrypted_secret = decrypt(ciphertext, private_key)
    print("[Kyber] Secret successfully encrypted and decrypted.")
    assert shared_secret == decrypted_secret, "Decryption failed!"
