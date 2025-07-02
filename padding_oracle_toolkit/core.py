"""Logique d'attaque Padding Oracle."""
def decrypt_block(oracle, cipher_block, previous_block):
    # Implémentation d’un déchiffrement CBC bloc à bloc
    # Utilise l’oracle pour tester chaque octet et reconstituer le message
    pass

def full_decrypt(oracle, ciphertext):
    # Découpe en blocs et appelle decrypt_block pour chaque bloc
    pass