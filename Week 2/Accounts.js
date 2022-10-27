class Person {
	constructor(firstName, lastName, accounts) {
		this.firstName = firstName;
		this.lastName = lastName;
		this.accounts = accounts;
	}
​
	getAccount(id) {
		return this.accounts.find((account) => account.id === id);
	}
​
	get name() {
		return `${this.firstName} ${this.lastName}`;
	}
​
	set name(name) {
		this.firstName = name.firstName;
		this.lastName = name.lastName;
	}
}
​
class Transaction {
	constructor(amount, type, balance) {
		this.date = new Date();
		this.type = type;
		this.amount = amount;
		this.balance = balance;
	}
​
	print() {
		return `${this.date.toUTCString()}\t${this.type}     ${
			this.amount
		}\t\tbalance:${this.balance}`;
	}
}
​
class Account {
	constructor(type, balance, id) {
		this.type = type;
		this.balance = balance;
		this.id = id;
		this.transactions = [];
	}
​
	get accountDetails() {
		return `${this.type}\t${this.id}`;
	}
​
	withdraw(amount) {
		this.balance -= amount;
		this.transactions.unshift(
			new Transaction(amount, "withdrawal", this.balance)
		);
	}
​
	deposit(amount) {
		this.balance += amount;
		this.transactions.unshift(new Transaction(amount, "deposit", this.balance));
	}
​
	statement() {
		console.log("----STATEMENT----");
		this.transactions.forEach((transaction) => {
			console.log(transaction.print());
		});
		console.log("----END STATEMENT----");
	}
}
​

class currentAccount extends Account {
    constructor(balance, id, overdraft) {
        super("current", balance, id)
        // this.overdraft = overdraft
    }

    withdraw(amount) {
        if (this.balance-amount < 0) {
            try {
                const cont = prompt('This transaction will make you overdrawn. Do you wish to continue? ("yes" or "no"')
                if (cont === 'yes') {
                    super.withdraw(amount)
                } else{
                    throw new Error('transaction cancelled')
                }
            } catch(err) {
                console.log(err.toString())
            }
        }
    }

}


const accounts = [new Account("savings", 100, 1), new Account("current", 0, 2)];
const sonali = new Person("Sonali", "Singh", accounts);
​
sonali.name = { firstName: "Biraj", lastName: "Pantha" };
console.log(sonali.name);
​
const SAVINGS = 1;
const CURRENT = 2;
​
const savingsAcc = sonali.getAccount(SAVINGS);
const currentAcc = sonali.getAccount(CURRENT);
​
savingsAcc.withdraw(50);
savingsAcc.deposit(25);
currentAcc.deposit(100);
// console.log(sonali.accounts[SAVINGS].balance());
// console.log(savingsAcc);
// console.log(currentAcc);
// savingsAcc.statement();
​
// Utility classes
//
// class Utility {
// 	// constructor() {}
// 	static sayHello(name) {
// 		return `hello ${name}`;
// 	}
// }
​
// // const utility = new Utility()
// // utility.sayHello()
// // console.log(Utility.sayHello("Sonali"));