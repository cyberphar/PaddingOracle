"""Point d'entrée CLI."""
import argparse
from padding_oracle_toolkit import core, http_client, utils

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--url", required=True)
    parser.add_argument("--cipher", required=True)
    args = parser.parse_args()

    ciphertext = bytes.fromhex(args.cipher)
    oracle = lambda block: http_client.query_oracle(args.url, block)
    plaintext = core.full_decrypt(oracle, ciphertext)
    print("Plaintext:", plaintext)