
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#
#   Copyright 2023 Valory AG
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.
#
# ------------------------------------------------------------------------------

"""Recreate wallet"""

from web3 import Account
import json
import time
from pathlib import Path


if __name__ == "__main__":
    mnemonic = input("Enter space-separated list of BIP39 mnemonic seed words: ").strip()
    passphrase = input("Enter a password: ").strip()

    Account.enable_unaudited_hdwallet_features()
    account = Account.from_mnemonic(mnemonic=mnemonic)

    timestamp = int(time.time())
    file_name = f"ethereum_{timestamp}.txt"
    path = Path(file_name)

    path.write_text(
        data=json.dumps(
            Account.encrypt(
                private_key=account._private_key,
                password=passphrase,
            ),
            indent=2,
        ),
        encoding="utf-8",
    )

    print("----------------------------")
    print(f"File '{file_name}' created.")
    print("")
    print(f"Please, backup './memeooorr/wallets/ethereum.txt' and replace it by '{file_name}'.")
    print("")
    print(f"Ensure you have not modified your './memeooorr/wallets/ethereum.json' file. It should look like this:")

    data = {
        "address": account.address,
        "safe_chains": [5],
        "ledger_type": 0,
        "safes": {
            "5": "0x0123456789abcdef0123456789abcdef0123"
        },
        "safe_nonce": 12345678912345678912345678912345678912345678912345678912345678912345678912345
    }
    print(json.dumps(data, indent=2))
    print("----------------------------")
