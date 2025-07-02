"""Utilitaires divers."""

def split_blocks(ciphertext, block_size=16):
    return [ciphertext[i:i+block_size] for i in range(0, len(ciphertext), block_size)]
