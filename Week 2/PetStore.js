class Dog {
  constructor(name, weight) {
    this.name = name;
    this.weight = weight;
  }

  bark() {
    if (this.weight >= 100) {
      console.log("WOOF");
    } else {
      console.log("woof");
    }
  }
}

class PetStore {
  constructor(pets) {
    this.pets = pets;
  }

  addPet(pet) {
    const dogNo = this.pets.reduce((acc, val) => {
      if (this.pets[val] instanceof Dog) {
        acc++;
      }
      return acc;
    }, 0);
    if (!(pet instanceof Dog)) {
      throw new Error("New pet is not a dog");
    } else if (dogNo !== 8) {
      this.pets.push(pet);
    }
  }

  petsForSale() {
    return this.pets;
  }
}
