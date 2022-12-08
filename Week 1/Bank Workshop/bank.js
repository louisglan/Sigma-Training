// Create a banking app
// The user should be able to deposit money
// The user should be able to withdraw money
// The user should be able to view a statement
// The user should be able to keep a track of transactions

// How are we storing this data? What does a user look like?

export function withdraw() {}

export function deposit() {}

export function statement() {}

export function balance(user) {
	return `£${user.balance.toFixed(2)}`;
}
