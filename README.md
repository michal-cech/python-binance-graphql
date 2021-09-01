# python-binance-graphql package

## About
Wrapper over Binance API. The advantages of this package are the following:
1) defined interfaces: ALL reponses are modeled as dataclasses. This means that if you decide to use this package, you do not need to worry about parsing JSON. All resposponses are properly modeled as corresponding dataclasses, hence you can work with objects.
2) GraphQL compliant: this package is GraphQL ready, you can use this client in your GraphQL schema without any issues. Example can be found in my [WiP investing-dashboard repository](https://github.com/michal-cech/investing-dashboard)

## Roadmap
- [ ] Support all Binance API endpoints
  - [x] Wallet
  - [x] Fiat
  - [x] C2C 
  - [ ] Market Data
  - [ ] Savings
  - [ ] Spot
  - [ ] Mining
  - [ ] Futures
  - [ ] BSwap
  - [ ] BLTV
  - [ ] User Data Streams
  - [ ] Websocket Market Streams
  - [ ] Sub-Account 
- [ ] Add tests
  - [ ] Wallet
  - [ ] Fiat
  - [ ] C2C 
  - [ ] Market Data
  - [ ] Savings
  - [ ] Spot
  - [ ] Mining
  - [ ] Futures
  - [ ] BSwap
  - [ ] BLTV
  - [ ] User Data Streams
  - [ ] Websocket Market Streams
  - [ ] Sub-Account 
- [ ] Add documentation
- [ ] Add premade schemas
- [ ] Add asynchronicity
