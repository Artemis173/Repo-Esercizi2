/*
npm i express
npm i eventsource
*/

const http = require("http");
const fs = require("fs");
const express = require("express");
const app = express();

// Serve static files
app.use(express.static("./"));

// Example addizionatore
app.get("*", (req, res) => {
  console.log(req.url, req.headers);
  console.log("SONO HONEYPOT");
  res.send("OK");
  });

let options = {};

let host = "172.26.193.163";
let port = 4000;

http.createServer(options, app).listen(port, host, () => {
  console.log("HTTP server running at http://localhost:3000");
});