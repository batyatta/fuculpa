def get_tx_data(wallet, CHAIN):
    """
    Get transaction data from the wallet.

    Args:
        wallet (Wallet): The wallet to get the transaction data from.
        CHAIN (str): The chain to get the transaction data from.

    Returns:
        dict: The transaction data.
    """

    # Get the transaction data from the wallet.
    tx_data = wallet.get_tx_data(CHAIN)

    # Return the transaction data.
    return tx_data

