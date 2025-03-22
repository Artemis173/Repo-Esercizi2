import Web3 from 'web3';

//Questa transazione non è attinente ai Metacoin ma è attinente agli ethereum

// Variables definition
const privKey =
  "0xa33cfbd7f7c21f251712bc53336862c1a0268edae94c9ec34088b715e307d5aa";

const addressFrom = "0x649A1d956aF5BaFc38A19aE7cCAAcBA252189B86";
const addressTo = "0x954B2fe5cc46DA87Af55B3348F10b6d7456fCE39";

//const web3 = new Web3(new Web3.providers.HttpProvider('http://localhost:7545'));

//const web3 = new Web3(new Web3.providers.HttpProvider('http://127.0.0.1:7545'));
const web3 = new Web3("http://127.0.0.1:7545/"); // Ganache;

// Create transaction
const deploy = async () => {
  try {
    console.log(
      `Attempting to make transaction from ${addressFrom} to ${addressTo}`
    );

    const transactionObject = {
      from: addressFrom,
      to: addressTo,
      value: web3.utils.toWei("1", "ether"),
    };

    // Estimate gas
    const gasEstimate = await web3.eth.estimateGas(transactionObject);

    // Add gas to transaction object
    transactionObject.gas = gasEstimate;

    // EIP-1559 gas parameters (adjust values as needed)
    const maxPriorityFeePerGas = web3.utils.toWei('1', 'gwei'); // Example value
    const maxFeePerGas = web3.utils.toWei('2', 'gwei'); // Example value

    transactionObject.maxPriorityFeePerGas = maxPriorityFeePerGas;
    transactionObject.maxFeePerGas = maxFeePerGas;
    

    const createTransaction = await web3.eth.accounts.signTransaction(
      transactionObject,
      privKey
    );

    // Deploy transaction
    const createReceipt = await web3.eth.sendSignedTransaction(
      createTransaction.rawTransaction
    );
    console.log(
      `Transaction successful with hash: ${createReceipt.transactionHash}`
    );
  } catch  (error) {
    console.error("Error during deployment:", error);
  }
};

deploy();

/* From truffle console */
/*
const privKey = "0x7ce93f8606bbdb6358ed39a138001c4aee8ef08ea20955497007f62f97ca0aac"

const addressFrom = '0xD586D7346f3da5D48B76FD6053f992Ca796aB6A5'
const addressTo = '0xF8D24Ac5546C3279C04596adf58AB538C573Fb4F'
const createTransaction = await web3.eth.accounts.signTransaction({"from": addressFrom,"to": addressTo,"value": web3.utils.toWei('1', 'ether'),"gas": '21000',},privKey)
const createReceipt = await web3.eth.sendSignedTransaction(createTransaction.rawTransaction)
createReceipt.transactionHash
*/
