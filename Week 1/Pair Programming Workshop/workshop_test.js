import { assertEquals } from "https://deno.land/std/testing/asserts.ts";
import { calculateTotal } from "./Pair_Programming_WS.js";
import { isGrapes } from "./Pair_Programming_WS.js";
import { mapNames } from "./Pair_Programming_WS.js";
import { filterLessThanPound } from "./Pair_Programming_WS.js";

const basket = [
  { name: "Apple", priceInPence: 50, quantity: 4 },
  { name: "Orange", priceInPence: 80, quantity: 2 },
  { name: "Carrots", priceInPence: 20, quantity: 10 },
  { name: "Strawberries", priceInPence: 150, quantity: 1 },
];

Deno.test("Finding the total number of items in the basket", () => {
  assertEquals(calculateTotal(basket), 17);
});

Deno.test("Seeing if there are grapes in the basket", () => {
  assertEquals(isGrapes(basket), false);
});

Deno.test("List names in basket", () => {
  assertEquals(mapNames(basket), [
    "Apple",
    "Orange",
    "Carrots",
    "Strawberries",
  ]);
});

Deno.test("List names in basket", () => {
  assertEquals(filterLessThanPound(basket), [
    { name: "Apple", priceInPence: 50, quantity: 4 },
    { name: "Orange", priceInPence: 80, quantity: 2 },
    { name: "Carrots", priceInPence: 20, quantity: 10 },
  ]);
});
