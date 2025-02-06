/*
npm i express
npm i eventsource
*/

const https = require("https");
const fs = require("fs");
const express = require("express");
const app = express();

// Serve static files
app.use(express.static("./"));

app.get("/events", (req, res) => {
  res.setHeader("Content-Type", "text/event-stream"); //!!!!!!!
  res.setHeader("Cache-Control", "no-cache");
  res.setHeader("Connection", "keep-alive");

  let counter = 0;

  const interval = setInterval(() => {
    counter++;
    res.write(
      `data: ${JSON.stringify({
        message: "Hello from server!",
        count: counter,
      })}\n\n`
    );
  }, 3000);

  req.on("close", () => {
    clearInterval(interval);
    console.log("Client disconnected");
  });
});

// Example route
app.get("/api", (req, res) => {
  res.json({ message: "Hello, Secure World!" });
});

const options = {
  key: fs.readFileSync("localhost-key.pem"),
  cert: fs.readFileSync("localhost.pem"),
};

https.createServer(options, app).listen(3000, () => {
  console.log("HTTPS server running at https://localhost:3000");
});
