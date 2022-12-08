function askUserForPhoneNumber() {
  const userInput = prompt("What is the phone number to validate?")
  return userInput
}

function main() {
  const phoneNo = askUserForPhoneNumber();
  const blockNo = phoneNo.replace(" ", "");
  const formattedNumber = convertPhoneToUKFormat(phoneNo);
  if(formattedNumber.length) {
    console.log(formattedNumber)
  } else {
    throwInvalidInputError();
  }
}

function isNumberValidLength(phoneNo) {
   return phoneNo.length === 11;
}

function isUKNo(phoneNo) {
    console.log(phoneNo)
  return phoneNo.slice(0,1) = "07";
}

function hasCountryCode(phoneNo) {
  return phoneNo.includes("+44")
}

function convertPhoneToUKFormat(input) {
  let phoneArray = []
  if(hasCountryCode(input)) {
    input.replace("+44", "07");
  }
  if(isNumberValidLength(input) && isUKNo(input)) {
    let phoneArray = convertStringToPhoneFormat(input)
  }
  return phoneArray;
}

function convertStringToPhoneFormat(phoneStr) {
   const phoneA = phoneStr.split(0,5)
   const phoneB = phoneStr.split(6)
   return [phoneA, phoneB]
}

function throwInvalidInputError() {
  console.log("This is an invalid UK number. Please try again.")
}

main();