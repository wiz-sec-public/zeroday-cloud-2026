import http from "node:http";
import React from "react";
import { renderToString } from "react-dom/server";


function App() {
  return React.createElement(
    "main",
    null,
    React.createElement("h1", null, "zeroday.cloud React target"),
    React.createElement("p", null, "Rendered on the server by React."),
  );
}


const server = http.createServer((request, response) => {
  if (request.url === "/health") {
    response.writeHead(200, { "content-type": "text/plain" });
    response.end("ok\n");
    return;
  }

  if (request.url !== "/") {
    response.writeHead(404, { "content-type": "text/plain" });
    response.end("not found\n");
    return;
  }

  const body = renderToString(React.createElement(App));
  response.writeHead(200, { "content-type": "text/html; charset=utf-8" });
  response.end(`<!doctype html><html lang="en"><head><meta charset="utf-8"><title>React target</title></head><body>${body}</body></html>`);
});

server.listen(3000, "0.0.0.0");
