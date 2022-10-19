const basket = [
  { name: "Apple", priceInPence: 50, quantity: 4 },
  { name: "Orange", priceInPence: 80, quantity: 2 },
  { name: "Carrots", priceInPence: 20, quantity: 10 },
  { name: "Strawberries", priceInPence: 150, quantity: 1 },
];

export function calculateTotal(itemList) {
  const totalNo = itemList.reduce((acc, item) => {
    return acc + item.quantity;
  }, 0);
  return totalNo;
}

export function isGrapes(itemList) {
  const isGrps = itemList.some((item) => {
    return item.name === "Grapes";
  });
  return isGrps;
}

export function mapNames(itemList) {
  const nameMap = itemList.map((item) => {
    return item.name;
  });
  return nameMap;
}

export function filterLessThanPound(itemList) {
  const filteredItems = itemList.filter((item) => {
    return item.priceInPence < 100;
  });
  return filteredItems;
}

// Which array method would I need to find the total number of items in my basket? - reduce
// Which array method would I need to see if there are "Grapes" in my basket? - some
// Which array method would I need to get a list of all the item names in my basket? - map
// Which array method would I need to find all the items less than £1 in my basket? - filter
