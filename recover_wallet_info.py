# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#
#   Copyright 2024 Valory AG
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
"""Recover wallet info."""

import getpass
from pathlib import Path

from operate.cli import OperateApp
from operate.types import (
    ChainType,
    LedgerType,
)


REPO_ROOT = Path(__file__).resolve().parent
OPERATE_HOME = REPO_ROOT / ".memeooorr"


def main() -> None:
    """Main method."""

    print("")
    print("-------")
    print("WARNING")
    print("-------")
    print(
        "This script will display sensitive wallet information on screen, "
        "including private keys. Ensure you run this script "
        "in a secure, offline environment and do not share the output with anyone."
    )
    print("")
    response = input("Do you want to continue? (yes/no): ").strip().lower()
    print("")
    if response not in ("yes", "y"):
        print("Exiting the script. No information has been displayed.")
        return

    operate = OperateApp(
        home=OPERATE_HOME,
    )
    operate.setup()

    if operate.user_account is None:
        print("There is no user account created.")
        return

    password = getpass.getpass("Enter local user account password: ")
    if not operate.user_account.is_valid(password=password):
        print("")
        print("WARNING: Invalid password!")
        input("Press any key to continue...")
        print("")

    operate.password = password
    manager = operate.service_manager()
    wallet = operate.wallet_manager.load(ledger_type=LedgerType.ETHEREUM)

    print("")
    print("------------------------------")
    print("Master Wallet and Master Safes")
    print("------------------------------")
    print("Master Wallet (EOA):")
    print(f"  * Address: {wallet.address}")

    try:
        print(f"  * Private key: {wallet.crypto.private_key}")
    except Exception:
        print("  * Private key cannot be recovered. Please import the wallet using the seed phrase.")
    
    print("")
    print("Master Safe(s):")
    for operate_chain_id, safe_address in wallet.safes.items():
        chain_name = ChainType(operate_chain_id).name
        safe_app_chain_id = "gno" if chain_name == "GNOSIS" else chain_name.lower()
        print(f"  * Safe {chain_name}: https://app.safe.global/home?safe={safe_app_chain_id}:{safe_address}")
    print("")

    print("--------")
    print("Services")
    print("--------")

    for service in manager.json:
        print(f"  * Service {service['name']}:")

        print("    - Service Agent(s):")
        for i, key in enumerate(service['keys'], start=1):
            print(f"      - Agent {i} address (EOA): {key['address']}")
            print(f"        Agent {i} private key: {key['private_key']}")

        print("")
        print("    - Service Safe(s):")
        for chain_id, chain_config in service['chain_configs'].items():
            chain_name = ChainType.from_id(int(chain_id)).name
            safe_app_chain_id = "gno" if chain_name == "GNOSIS" else chain_name.lower()
            print(f"      - Safe {chain_name}: https://app.safe.global/home?safe={safe_app_chain_id}:{chain_config['chain_data']['multisig']}")
            print(f"        Olas Registry {chain_name}: https://registry.olas.network/{chain_name.lower()}/services/{chain_config['chain_data']['token']}")
            print("")
        print("")


if __name__ == "__main__":
    main()
