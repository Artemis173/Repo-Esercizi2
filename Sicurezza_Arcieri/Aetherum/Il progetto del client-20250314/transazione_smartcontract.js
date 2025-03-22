"use strict";

// Deploying 'bs721'
// truffle migrate --reset --compile-all --network sepolia
// -----------------
// > transaction hash:    0x2531df4ac58fe932387d905a995bde8c52497c6d31448bcf0db2198a237ab552
// > Blocks: 0            Seconds: 9
// > contract address:    0xAddC0871b990359779E7d7D9b1CE061dE0d48bbe
// > block number:        2536826
// > block timestamp:     1671785352
// > account:             0xf53d15Ca271bBe0a02528D6F930bBb5d12DeB53a
// > balance:             0.05973089572
// > gas used:            3077154
// > gas price:           0.04 gwei
// > value sent:          0 ETH
// > total cost:          0.00012308616 ETH

import Web3 from 'web3';
import fs from "fs";
import axios from "axios";

/***********************************************/
/*************** CODICE GENERALE ***************/
/***********************************************/

//Path compilation, from the compiled contract in build/contracts/bs721.json (only the section "abi")
const bs721_json = "../MetaCoin/build/contracts/MetaCoin.json";

//Load the configurations (network, addresses, keys and contract)
let bs712_config = null;
let network = null;

//HttpProvider Endpoint
let web3 = null;

//Owner and contract
let contract_owner = null;
let contractAddress = null;
let contract_owner_pk = null;

//Le modifiche qui marcate come //SDC2223 sono per accedere a ganache

try {
  console.log("Uno");
  bs712_config = JSON.parse(fs.readFileSync("bs721-config.json"));
  console.log("Due");
  network = bs712_config["network"]; //Qui la configurazione del nodo di accesso alla blockchain
  console.log("A6");

  web3 = new Web3(
    new Web3.providers.HttpProvider(bs712_config[network]["infura"])
  );
  console.log("A7");
  contract_owner = bs712_config[network]["contract_owner"];
  contractAddress = bs712_config[network]["contractAddress"];
  contract_owner_pk = bs712_config[network]["contract_owner_pk"];
  console.log("A8");
} catch (err) {
  console.log(JSON.stringify({ result: false, code: err.toString() }));
  process.exit(1);
}

console.log("A9");

//Just to check if lost something
if (!network || !contract_owner || !contractAddress || !contract_owner_pk) {
  console.log(
    JSON.stringify({ result: false, code: "error in bs721-config.json" })
  );
  process.exit(1);
}
console.log("A1");

/*
  JUST TO REMEMBER...
1 Ether                                      1,000,000,000,000,000,000 WEI = 1 (EXA)WEI
1 (MILLI)ETHER = 0.001 ETHER                     1,000,000,000,000,000 WEI = 1 (PETA)WEI
1 (MICRO)ETHER = 0.000001 ETHER                      1,000,000,000,000 WEI = 1 (TERA)WEI
1 (Nano)ETHER  = 0.000000001 ETHER                       1,000,000,000 WEI = 1 (GIGA)WEI
1 (PICO)ETHER  = 0.000000000001 ETHER                        1,000,000 WEI = 1 (MEGA)WEI
1 (FEMTO)ETHER = 0.000000000000001 ETHER                         1,000 WEI = 1 (KILO)WEI
1 (ATTO)ETHER  = 0.000000000000000001 ETHER                          1 WEI

1 ETHER => 225 EUROs
       1 GWEI = 0.000000001*225 = .000000225 Euro
     100 GWEI = 0.000022500 euro
 1000000 GWEI = 0.225 euro
10000000 GWEI = 2.250 euro

*/
//Questo ovviamente funziona solo su reti pubbliche (ropsten o ethereum mainnet)
async function getCurrentGasMediumPrice(network) {
  if (
    network === null ||
    typeof network === "undefined" ||
    network === "sepolia"
  ) {
    //console.log("Ropsten and others for development");
    let gasLimit = web3.utils.toHex(30000000);
    let gasPrice = web3.utils.toHex(web3.utils.toWei("1", "gwei"));
    return { gasPrice: gasPrice, gasLimit: gasLimit };
  }

  try {
    let response = await axios.get(
      "https://ethgasstation.info/json/ethgasAPI.json"
    );
    let prices = {
      low: response.data.safeLow / 10,
      medium: response.data.average / 10,
      high: response.data.fast / 10,
    };

    let highwei = web3.utils.toWei((3 * prices.high).toString(), "gwei");
    return {
      gasPrice: web3.utils.toHex(highwei),
      gasLimit: web3.utils.toHex(8000000),
    };
  } catch (err) {
    return {
      gasPrice: web3.utils.toHex(web3.utils.toWei("20", "gwei")),
      gasLimit: web3.utils.toHex(8000000),
    };
  }
}

async function main(request) {
  console.log("A2");
  if (request === null || request.length === 0) {
    return { result: false, code: "request " + request + " not found" };
  }
  console.log("A3");


  /***********************************************/
  /*************** CODICE SPECIFICO  *************/
  /***********************************************/

  //Legge abi del contratto
  console.log("Tre");
  const contract_raw = fs.readFileSync(bs721_json, "UTF-8");
  console.log("4");
  const contract_json = JSON.parse(contract_raw);
  console.log("5");
  const contractABI = contract_json.abi;
  console.log("6");

  let account = null;
  try {
    // Add account from private key
    account = web3.eth.accounts.privateKeyToAccount("0x" + contract_owner_pk);
    web3.eth.accounts.wallet.add(account);
    web3.eth.defaultAccount = account.address;
  } catch (err) {
    return { result: false, code: err.toString() };
  }
  console.log("A4");

  //si collega al contratto
  const contract = await new web3.eth.Contract(contractABI, contractAddress);

  //se ci sono transazioni pending e se la richiesta è di aggiornamento (mint e setTokenUri, aspetta)
  if (request[0] == "mint" || request[0] == "setTokenURI") {
    const pending = await web3.eth.getTransactionCount(
      contract_owner,
      "pending"
    );
    const notpending = await web3.eth.getTransactionCount(contract_owner);
    if (pending - notpending > 0) {
      return { result: false, err: "pending" };
    }
  }

  //Dovrebbe essere serializable e firmata? Ci pensa web3!
  let tx = {
    // from: account1,
    // to: account2,
    // gasLimit: web3.utils.toHex(4700000),
    // gasPrice: web3.utils.toHex(web3.utils.toWei('100', 'gwei')),
  };

  try {
    switch (
      request[0] //command name
    ) {
      case "price": {
        const price = await getCurrentGasMediumPrice(network);
        return { result: true, data: { price: price } };
      }
      case "name":
        {
          let name = await contract.methods.name().call(tx);
          return { result: true, data: { name: name } };
        }
        break;
      case "symbol":
        {
          let symbol = await contract.methods.symbol().call(tx);
          return { result: true, data: { symbol: symbol } };
        }
        break;
      case "mint":
        {
          if (request.length != 4) {
            return { result: false, code: "mint address tokenid tokenURI" };
          }
          let gasprices = await getCurrentGasMediumPrice(network);
          tx.gasPrice = gasprices.gasPrice;
          tx.gasLimit = gasprices.gasLimit;
          tx.to = request[1];
          tx.from = contract_owner;

          let to = request[1];
          let tokenId = request[2];
          let tokenURI = request[3];
          try {
            let result = await contract.methods
              .mintWithTokenURI(to, tokenId, tokenURI)
              .send(tx);
            return { result: true, data: { mint: true } };
          } catch (err) {
            return { result: false, code: err.toString() };
          }
        }
        break;
      case "setTokenURI":
        {
          if (request.length != 3) {
            return { result: false, code: "seTokenURI tokenid tokenURI" };
          }
          let gasprices = await getCurrentGasMediumPrice(network);
          tx.gasPrice = gasprices.gasPrice;
          tx.gasLimit = gasprices.gasLimit;
          tx.from = contract_owner;
          let tokenId = request[1];
          let tokenURI = request[2];
          try {
            await contract.methods.setTokenURI(tokenId, tokenURI).send(tx);
            return { result: true, data: { setTokenURI: true } };
          } catch (err) {
            return { result: false, code: "error in setTokenURI" };
          }
        }
        break;
      case "addone":
        {
          if (request.length != 2) {
            return { result: false, code: "addone number" };
          }
          let num = request[1];
          let ret = await contract.methods.addone(num).call(tx);
          return { result: true, data: { number: ret } };
        }
        break;
      case "tokensOfOwner":
        {
          if (request.length != 2) {
            return { result: false, code: "tokensOfOwner address" };
          }
          let address = request[1];
          let tokens = await contract.methods.tokensOfOwner(address).call(tx);
          return { result: true, data: { tokensOfOwner: tokens } };
        }
        break;
      case "countTokensOf":
        {
          if (request.length != 2) {
            return { result: false, code: "countTokensOf address" };
          }
          let address = request[1];
          let balance = await contract.methods.balanceOf(address).call(tx);
          return { result: true, data: { countTokensOf: balance } };
        }
        break;
      case "balanceOf":
        {
          if (request.length != 2) {
            return { result: false, code: "balanceOf address" };
          }
          let address = request[1];
          let balance = await web3.eth.getBalance(address);
          //console.log(typeof(balance), ": ", balance);
          balance = web3.utils.fromWei(balance.toString(), "ether");
          return { result: true, data: { balanceOf: balance } };
        }
        break;
      case "ownerOf":
        {
          if (request.length != 2) {
            return { result: false, code: "ownerOf tokenId" };
          }
          let tokenId = request[1];
          let owner = await contract.methods.ownerOf(tokenId).call(tx);
          return { result: true, data: { ownerOf: owner } };
        }
        break;
      case "exists": {
        if (request.length != 2) {
          return { result: false, code: "exists tokenId" };
        }
        let tokenId = request[1];
        let ret = await contract.methods.exists(tokenId).call(tx);
        return { result: true, data: { exists: ret } };
      }
      case "tokenURI":
        {
          if (request.length != 2) {
            return { result: false, code: "tokenURI tokenId" };
          }
          let tokenId = request[1];
          let uri = await contract.methods.tokenURI(tokenId).call(tx);
          //console.log(uri);
          return { result: true, data: { tokenURI: uri } };
        }
        break;
      case "transferFrom":
        {
          if (request.length != 4) {
            return { result: false, code: "transferFrom from to tokenId" };
          }
          let from = request[1];
          let to = request[2];
          let tokenId = request[3];

          let gasprices = await getCurrentGasMediumPrice(network);
          tx.gasPrice = gasprices.gasPrice;
          tx.gasLimit = gasprices.gasLimit;
          tx.from = contract_owner;

          let ret = await contract.methods
            .transferFrom(from, to, tokenId)
            .send(tx);
          console.log(ret);
          return { result: true, data: { transferFrom: ret } };
        }
        break;
      case "approve":
        {
          if (request.length != 5) {
            return {
              result: false,
              code: "approve operator-address owner-id owner-key tokenId",
            };
          }
          let address = request[1];
          let id = request[2];
          let pkey = request[3];
          let tokenId = request[4];
          // Add account from private key
          let account = web3.eth.accounts.privateKeyToAccount("0x" + pkey);
          web3.eth.accounts.wallet.add(account);
          web3.eth.defaultAccount = account.address;

          //si collega al contratto
          let contract = await new web3.eth.Contract(
            contractABI,
            contractAddress
          );

          let gasprices = await getCurrentGasMediumPrice(network);
          tx.gasPrice = gasprices.gasPrice;
          tx.gasLimit = gasprices.gasLimit;
          tx.to = address;
          tx.from = id;

          //Esegue il contratto
          let ret = await contract.methods.approve(address, tokenId).send(tx);
          console.log(ret);
          return { result: true, data: { approve: ret } };
        }
        break;
    }
  } catch (err) {
    return { result: false, code: err.toString() };
  }
}

main(process.argv.slice(2)).then(
  (ret) => {
    console.log(JSON.stringify(ret));
  },
  (err) => {
    console.log(JSON.stringify({ result: false, code: err.toString() }));
  }
);
