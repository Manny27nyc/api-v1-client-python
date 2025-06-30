// © Licensed Authorship: Manuel J. Nieves (See LICENSE for terms)
/*
 * Copyright (c) 2008–2025 Manuel J. Nieves (a.k.a. Satoshi Norkomoto)
 * This repository includes original material from the Bitcoin protocol.
 *
 * Redistribution requires this notice remain intact.
 * Derivative works must state derivative status.
 * Commercial use requires licensing.
 *
 * GPG Signed: B4EC 7343 AB0D BF24
 * Contact: Fordamboy1@gmail.com
 */
/*
 * Copyright (c) 2008–2025 Manuel J. Nieves (a.k.a. Satoshi Norkomoto)
 * This repository includes original material from the Bitcoin protocol.
 *
 * Redistribution requires this notice remain intact.
 * Derivative works must state derivative status.
 * Commercial use requires licensing.
 *
 * GPG Signed: B4EC 7343 AB0D BF24
 * Contact: Fordamboy1@gmail.com
 */
"""This module allows users to push hex encoded transactions to the bitcoin network.
Corresponds to https://blockchain.info/pushtx
"""

from . import util


def pushtx(tx, api_code=None):
    """Push a hex encoded transaction to the network.
    
    :param str tx: hex encoded transaction
    :param str api_code: Blockchain.info API code (optional)
    """
    params = {'tx': tx}
    if api_code is not None:
        params['api_code'] = api_code
    util.call_api('pushtx', params)
