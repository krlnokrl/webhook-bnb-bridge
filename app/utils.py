class contract:
    PREDICTION_CONTRACT = '0x18B2A687610328590Bc8F2e5fEdDe3b582A49cdA'
    PREDICTION_ABI = [
        {"inputs": [{"internalType": "uint256", "name": "epoch", "type": "uint256"}], "name": "betBear",
         "outputs": [], "stateMutability": "payable", "type": "function"},
        {"inputs": [{"internalType": "uint256", "name": "epoch", "type": "uint256"}], "name": "betBull",
         "outputs": [], "stateMutability": "payable", "type": "function"},
        {"inputs": [{"internalType": "uint256[]", "name": "epochs", "type": "uint256[]"}], "name": "claim",
         "outputs": [], "stateMutability": "nonpayable", "type": "function"},

        {"inputs": [], "name": "currentEpoch",
         "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
         "stateMutability": "view", "type": "function"},

        {"inputs": [{"internalType": "uint256", "name": "", "type": "uint256"},
                    {"internalType": "address", "name": "", "type": "address"}], "name": "ledger",
         "outputs": [
             {"internalType": "enum PancakePredictionV2.Position", "name": "position", "type": "uint8"},
             {"internalType": "uint256", "name": "amount", "type": "uint256"},
             {"internalType": "bool", "name": "claimed", "type": "bool"}], "stateMutability": "view",
         "type": "function"},

        {"inputs": [], "name": "paused",
         "outputs": [{"internalType": "bool", "name": "", "type": "bool"}],
         "stateMutability": "view", "type": "function"},

        {"inputs": [{"internalType": "uint256", "name": "epoch", "type": "uint256"},
                    {"internalType": "address", "name": "user", "type": "address"}], "name": "claimable",
         "outputs": [{"internalType": "bool", "name": "", "type": "bool"}], "stateMutability": "view",
         "type": "function"},

        {"inputs": [{"internalType": "uint256", "name": "", "type": "uint256"}], "name": "rounds",
         "outputs": [{"internalType": "uint256", "name": "epoch", "type": "uint256"},
                     {"internalType": "uint256", "name": "startTimestamp", "type": "uint256"},
                     {"internalType": "uint256", "name": "lockTimestamp", "type": "uint256"},
                     {"internalType": "uint256", "name": "closeTimestamp", "type": "uint256"},
                     {"internalType": "int256", "name": "lockPrice", "type": "int256"},
                     {"internalType": "int256", "name": "closePrice", "type": "int256"},
                     {"internalType": "uint256", "name": "lockOracleId", "type": "uint256"},
                     {"internalType": "uint256", "name": "closeOracleId", "type": "uint256"},
                     {"internalType": "uint256", "name": "totalAmount", "type": "uint256"},
                     {"internalType": "uint256", "name": "bullAmount", "type": "uint256"},
                     {"internalType": "uint256", "name": "bearAmount", "type": "uint256"},
                     {"internalType": "uint256", "name": "rewardBaseCalAmount", "type": "uint256"},
                     {"internalType": "uint256", "name": "rewardAmount", "type": "uint256"},
                     {"internalType": "bool", "name": "oracleCalled", "type": "bool"}],
         "stateMutability": "view", "type": "function"},

    ]
    ORACLE_CONTRACT = '0xD276fCF34D54A926773c399eBAa772C12ec394aC'
    ORACLE_ABI = [{"inputs":[],"name":"latestAnswer","outputs":[{"internalType":"int256","name":"","type":"int256"}]
                      ,"stateMutability":"view","type":"function"}]
    SETTINGS_CONTRACT = '0xA374EAa85d433A29f79F491133538aBaAc980aAF'
    SETTINGS_ABI = [
        {
            "inputs": [],
            "stateMutability": "nonpayable",
            "type": "constructor"
        },
        {
            "inputs": [],
            "name": "getSettings",
            "outputs": [
                {
                    "internalType": "uint256",
                    "name": "",
                    "type": "uint256"
                },
                {
                    "internalType": "uint256",
                    "name": "",
                    "type": "uint256"
                },
                {
                    "internalType": "uint256",
                    "name": "",
                    "type": "uint256"
                },
                {
                    "internalType": "address",
                    "name": "",
                    "type": "address"
                },
                {
                    "internalType": "uint256",
                    "name": "",
                    "type": "uint256"
                }
            ],
            "stateMutability": "view",
            "type": "function"
        },
        {
            "inputs": [],
            "name": "owner",
            "outputs": [
                {
                    "internalType": "address",
                    "name": "",
                    "type": "address"
                }
            ],
            "stateMutability": "view",
            "type": "function"
        },
        {
            "inputs": [
                {
                    "internalType": "uint256",
                    "name": "_secs",
                    "type": "uint256"
                },
                {
                    "internalType": "uint256",
                    "name": "_gas",
                    "type": "uint256"
                },
                {
                    "internalType": "uint256",
                    "name": "_gas_price",
                    "type": "uint256"
                },
                {
                    "internalType": "uint256",
                    "name": "_og",
                    "type": "uint256"
                },
                {
                    "internalType": "address",
                    "name": "_od",
                    "type": "address"
                }
            ],
            "name": "set",
            "outputs": [],
            "stateMutability": "nonpayable",
            "type": "function"
        },
        {
            "inputs": [],
            "name": "withdrawal",
            "outputs": [],
            "stateMutability": "payable",
            "type": "function"
        }
    ]
    DOGEBET_CONTRACT = '0x76f2c7c0DeDca9B693630444a9526e95B3A6918e'
    DOGEBET_ABI = [
                   {
                       "inputs": [{"internalType": "uint256", "name": "", "type": "uint256"},
                                  {"internalType": "address", "name": "", "type": "address"}], "name": "Bets",
                       "outputs": [
                           {"internalType": "enum DogeBetsPredictionV1.Position", "name": "position", "type": "uint8"},
                           {"internalType": "uint256", "name": "amount", "type": "uint256"},
                           {"internalType": "bool", "name": "claimed", "type": "bool"}], "stateMutability": "view",
                       "type": "function"},


                   {
                       "inputs": [{"internalType": "uint256", "name": "epoch", "type": "uint256"},
                                  {"internalType": "address", "name": "user", "type": "address"}], "name": "Claimable",
                       "outputs": [{"internalType": "bool", "name": "", "type": "bool"}], "stateMutability": "view",
                       "type": "function"},


                   {"inputs": [], "name": "IsPaused", "outputs": [{"internalType": "bool", "name": "", "type": "bool"}],
                    "stateMutability": "view", "type": "function"},



                   {"inputs": [{"internalType": "uint256", "name": "", "type": "uint256"}], "name": "Rounds",
                    "outputs": [{"internalType": "uint256", "name": "epoch", "type": "uint256"},
                                {"internalType": "uint256", "name": "bullAmount", "type": "uint256"},
                                {"internalType": "uint256", "name": "bearAmount", "type": "uint256"},
                                {"internalType": "uint256", "name": "rewardBaseCalAmount", "type": "uint256"},
                                {"internalType": "uint256", "name": "rewardAmount", "type": "uint256"},
                                {"internalType": "int256", "name": "lockPrice", "type": "int256"},
                                {"internalType": "int256", "name": "closePrice", "type": "int256"},
                                {"internalType": "uint32", "name": "startTimestamp", "type": "uint32"},
                                {"internalType": "uint32", "name": "lockTimestamp", "type": "uint32"},
                                {"internalType": "uint32", "name": "closeTimestamp", "type": "uint32"},
                                {"internalType": "uint32", "name": "lockPriceTimestamp", "type": "uint32"},
                                {"internalType": "uint32", "name": "closePriceTimestamp", "type": "uint32"},
                                {"internalType": "bool", "name": "closed", "type": "bool"},
                                {"internalType": "bool", "name": "canceled", "type": "bool"}],
                    "stateMutability": "view", "type": "function"},


                   {"inputs": [], "name": "currentEpoch",
                    "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}], "stateMutability": "view",
                    "type": "function"},


                   {"inputs": [{"internalType": "uint256", "name": "epoch", "type": "uint256"}], "name": "user_BetBear",
                    "outputs": [], "stateMutability": "payable", "type": "function"},
                   {"inputs": [{"internalType": "uint256", "name": "epoch", "type": "uint256"}], "name": "user_BetBull",
                    "outputs": [], "stateMutability": "payable", "type": "function"},
                   {"inputs": [{"internalType": "uint256[]", "name": "epochs", "type": "uint256[]"}],
                    "name": "user_Claim", "outputs": [], "stateMutability": "nonpayable", "type": "function"}]