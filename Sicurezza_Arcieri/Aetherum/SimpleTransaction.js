import Web3 from 'web3';

//Questa transazione non è attinente ai Metacoin ma è attinente agli ethereum

// Variables definition
const privKey =
  "0x32d0499ee5bf81bc9711f3044c1fb4d1d0a8a7446defbb6c919ceaa7217fe002";

const addressFrom = "0x92Ed6a976E0ce3e9816283E58AC9530576ACaCEF";
const addressTo = "0xd219C98d8336F19702712517fe0FA0868F3Aa5e7";

const web3 = new Web3("http://127.0.0.1:7545"); // Ganache;

// Create transaction
const deploy = async () => {
  console.log(
    `Attempting to make transaction from ${addressFrom} to ${addressTo}`
  );

  const createTransaction = await web3.eth.accounts.signTransaction(
    {
      from: addressFrom,
      to: addressTo,
      value: web3.utils.toWei("1", "ether"),
      gas: "21000",
    },
    privKey
  );

  // Deploy transaction
  const createReceipt = await web3.eth.sendSignedTransaction(
    createTransaction.rawTransaction
  );
  console.log(
    `Transaction successful with hash: ${createReceipt.transactionHash}`
  );
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