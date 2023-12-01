/**
 * @module 9-stock.js
 */
import { createClient } from "redis";
import express from 'express';

const app = express();
const client = createClient()
const PORT = 1245;

const listProducts = [
  {itemId: 1, itemName: 'Suitcase 250', price: 50, initialQuantity: 4},
  {itemId: 2, itemName: 'Suitcase 450', price: 100, initialQuantity: 10},
  {itemId: 3, itemName: 'Suitcase 650', price: 350, initialQuantity: 2},
  {itemId: 4, itemName: 'Suitcase 1050', price: 550, initialQuantity: 5},
]

const getItemById = (id) => {
  for (const product of listProducts) {
    if (product.itemId === id) return product;
  }
  return undefined;
};

const reserveStockById = async (itemId, stock) => {
  await client.connect();
  await client.set(`item.${itemId}`, JSON.stringify(stock));
  await client.quit();
};

const getCurrentReservedStockById = async (itemId) => {
  await client.connect();
  const stockString = await client.get(`item.${itemId}`);
  await client.quit();
  return JSON.parse(stockString);
};

// CONTROLLERS

const listAllAvailableProducts = (req, res) => {
  res.json(listProducts);
};

const listProductById = async (req, res) => {
  const itemId = parseInt(req.params.itemId);
  const retrievedProd = await getCurrentReservedStockById(itemId);
  if (!retrievedProd) {
    return res.json({"status":"Product not found"});
  }
  res.json(retrievedProd);
}

const reserveProductById = async (req, res) => {
  const itemId = parseInt(req.params.itemId);
  const prodToReserve = getItemById(itemId);
  if (prodToReserve === undefined) {
    return res.json({"status":"Product not found"});
  }

  if (prodToReserve.currentQuantity === undefined) {
    prodToReserve.currentQuantity = prodToReserve.initialQuantity;
  } else {
    prodToReserve.currentQuantity -= 1;
  }

  if (prodToReserve.currentQuantity <= 0) {
    return res.json({"status":"Not enough stock available","itemId":itemId});
  }
  await reserveStockById(itemId, prodToReserve)
  res.json({"status":"Reservation confirmed","itemId":itemId});
}

app.use(express.json());

// ROUTES

app.get('/list_products', listAllAvailableProducts);

app.get('/list_products/:itemId', listProductById);

app.get('/reserve_product/:itemId', reserveProductById);

app.listen(PORT);
