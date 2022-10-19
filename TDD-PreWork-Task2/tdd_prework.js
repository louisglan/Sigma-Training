export function capitalise(name) {
  let nameArr = name.split("");
  const newNameArr = nameArr.map((item) => {
    return item.toUpperCase();
  });
  return newNameArr.join("");
}

console.log(capitalise("John"));
