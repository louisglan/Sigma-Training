import {
	assertEquals,
	assertStringIncludes,
} from "https://deno.land/std/testing/asserts.ts";

import { deposit, withdraw, statement, balance } from "./bank.js";

const testUser = {
	firstName: "Jane",
	lastName: "Doe",
	balance: 500,
	transactions: testTransactions,
};

// Balance
// We want to check the balance is correct
Deno.test("balance(): the balance returned for a user is correct", () => {
	const user = { ...testUser };
	assertEquals(balance(user), "£500.00");
});

Deno.test("deposit(): adding money updated user balance", () => {
	deposit(testUser, 50);
	assertEquals(user.balance, 550);
});
// Deposit
// We want to test that given a balance, the correct amount gets added
// And the balance total is updated

// Some pretend transactions
const testTransactions = [
	{
		date: new Date(2022, 9, 16, 13, 24, 12, 52),
		type: "deposit",
		amount: 100,
	},
	{
		date: new Date(2022, 9, 15, 11, 48, 35, 17),
		type: "withdrawal",
		amount: 10,
	},
	{ date: new Date(), type: "withdrawal", amount: 50 },
];

// Our pretend user looks like:

const { firstName, lastName } = testUser;
